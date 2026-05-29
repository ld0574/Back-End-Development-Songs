from . import app
import os
import json
import uuid
from copy import deepcopy
from types import SimpleNamespace
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401
import sys

try:
    import pymongo  # noqa; F401
    from pymongo import MongoClient
    from bson import json_util
    from pymongo.errors import OperationFailure
    from pymongo.results import InsertOneResult
    from bson.objectid import ObjectId
except ModuleNotFoundError:
    MongoClient = None
    json_util = None

    class OperationFailure(Exception):
        pass

    class InsertOneResult:
        pass

    class ObjectId:
        def __init__(self):
            self.value = uuid.uuid4().hex

        def __str__(self):
            return self.value

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "songs.json")
songs_list: list = json.load(open(json_url))

# client = MongoClient(
#     f"mongodb://{app.config['MONGO_USERNAME']}:{app.config['MONGO_PASSWORD']}@localhost")
mongodb_service = os.environ.get('MONGODB_SERVICE')
mongodb_username = os.environ.get('MONGODB_USERNAME')
mongodb_password = os.environ.get('MONGODB_PASSWORD')
mongodb_port = os.environ.get('MONGODB_PORT')

print(f'The value of MONGODB_SERVICE is: {mongodb_service}')

def parse_json(data):
    if json_util is None:
        return convert_object_ids(data)
    return json.loads(json_util.dumps(data))


def convert_object_ids(data):
    if isinstance(data, ObjectId):
        return {"$oid": str(data)}
    if isinstance(data, list):
        return [convert_object_ids(item) for item in data]
    if isinstance(data, dict):
        return {
            key: convert_object_ids(value)
            for key, value in data.items()
        }
    return data


class InMemorySongsCollection:
    """Small Mongo-like fallback used when a local MongoDB service is unavailable."""

    def __init__(self, seed):
        self._documents = []
        self.insert_many(seed)

    def _matches(self, document, query):
        return all(document.get(key) == value for key, value in query.items())

    def drop(self):
        self._documents = []

    def insert_many(self, documents):
        for document in documents:
            self.insert_one(document)

    def count_documents(self, query):
        return len([doc for doc in self._documents if self._matches(doc, query)])

    def find(self, query):
        return [deepcopy(doc) for doc in self._documents if self._matches(doc, query)]

    def find_one(self, query):
        for document in self._documents:
            if self._matches(document, query):
                return deepcopy(document)
        return None

    def insert_one(self, document):
        stored = deepcopy(document)
        stored.setdefault("_id", ObjectId())
        self._documents.append(stored)
        return SimpleNamespace(inserted_id=stored["_id"])

    def update_one(self, query, update):
        for document in self._documents:
            if self._matches(document, query):
                modified = False
                for key, value in update.get("$set", {}).items():
                    if document.get(key) != value:
                        modified = True
                    document[key] = value
                return SimpleNamespace(modified_count=1 if modified else 0)
        return SimpleNamespace(modified_count=0)

    def delete_one(self, query):
        for index, document in enumerate(self._documents):
            if self._matches(document, query):
                del self._documents[index]
                return SimpleNamespace(deleted_count=1)
        return SimpleNamespace(deleted_count=0)


class InMemorySongsDB:
    def __init__(self, seed):
        self.songs = InMemorySongsCollection(seed)


def connect_database():
    if not mongodb_service or MongoClient is None:
        app.logger.warning(
            "Missing MongoDB server in MONGODB_SERVICE; using in-memory songs store"
        )
        return InMemorySongsDB(songs_list)

    service = mongodb_service
    if mongodb_port and ":" not in service:
        service = f"{service}:{mongodb_port}"

    if mongodb_username and mongodb_password:
        url = f"mongodb://{mongodb_username}:{mongodb_password}@{service}"
    else:
        url = f"mongodb://{service}"

    print(f"connecting to url: {url}")

    try:
        client = MongoClient(url, serverSelectionTimeoutMS=2000)
        client.admin.command("ping")
        database = client.songs
        database.songs.drop()
        database.songs.insert_many(deepcopy(songs_list))
        return database
    except OperationFailure as e:
        app.logger.error(f"Authentication error: {str(e)}")
    except Exception as e:
        app.logger.error(f"MongoDB unavailable: {str(e)}")

    app.logger.warning("Using in-memory songs store")
    return InMemorySongsDB(songs_list)


db = connect_database()

######################################################################
@app.route("/health")
def healthz():
    return jsonify(dict(status="OK")), 200


@app.route("/count")
def count():
    count = db.songs.count_documents({})
    return {"count": count}, 200


@app.route("/song", methods=["GET"])
def songs():
    results = list(db.songs.find({}))
    return {"songs": parse_json(results)}, 200


@app.route("/song/<int:id>", methods=["GET"])
def get_song_by_id(id):
    song = db.songs.find_one({"id": id})
    if not song:
        return {"message": f"song with id {id} not found"}, 404
    return parse_json(song), 200


@app.route("/song", methods=["POST"])
def create_song():
    song_in = request.get_json(silent=True) or {}

    if "id" not in song_in:
        return {"message": "song id is required"}, 400

    song = db.songs.find_one({"id": song_in["id"]})
    if song:
        return {
            "Message": f"song with id {song_in['id']} already present"
        }, 302

    insert_id: InsertOneResult = db.songs.insert_one(song_in)
    return {"inserted id": parse_json(insert_id.inserted_id)}, 201


@app.route("/song/<int:id>", methods=["PUT"])
def update_song(id):
    song_in = request.get_json(silent=True) or {}

    song = db.songs.find_one({"id": id})
    if song is None:
        return {"message": "song not found"}, 404

    result = db.songs.update_one({"id": id}, {"$set": song_in})

    if result.modified_count == 0:
        return {"message": "song found, but nothing updated"}, 200

    return parse_json(db.songs.find_one({"id": id})), 201


@app.route("/song/<int:id>", methods=["DELETE"])
def delete_song(id):
    result = db.songs.delete_one({"id": id})
    if result.deleted_count == 0:
        return {"message": "song not found"}, 404
    return "", 204
######################################################################
