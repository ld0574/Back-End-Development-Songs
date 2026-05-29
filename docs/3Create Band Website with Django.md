::page{title="Create Band Website with Django"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/IDSN-logo.png" width="200/">

##

**Estimated time: 90 minutes**

##

Welcome to the **Create Band Website wth Django** hands-on lab. In this lab, you will create the main website for the band. The lab provides a GitHub template repository to get you started.

At the end of the lab, you will:
1. Create the main home page for the band
1. Create the songs page that lists all the titles of the songs
1. Craete the photos page that displays pictures from past events
1. Allow users to log in and:
	1. See concerts they are attending
	1. Change attendance at concerts
1. Allow admin user to create, delete, and edit concerts

## Objectives
In this lab, you will:

- Start a Django Server
- Create and run database migrations
- Create a Django admin user
- Create backend views for the Django application
- Send JSON data to templates
- Create Django models
- Check for authenticated users in Django backend

::page{title="Note: Important Security Information"}

Welcome to the Cloud IDE. This is where all your development will take place. It has all the tools you will need to use, including **Python** and **Flask**.

It is important to understand that the lab environment is ephemeral. It only lives for a short while before it is destroyed. It is imperative that you push all changes made to your own GitHub repository so that it can be recreated in a new lab environment any time it is required.

Also, note that this environment is shared and, therefore, not secure. You should not store any personal information, usernames, passwords, or access tokens in this environment for any purpose.

## Your Task
If you haven\'t generated a GitHub Personal Access Token you should do so now. You will need it to push code back to your repository. It should have `repo` and `write` permissions, and be set to expire in `60` days. When Git prompts you for a password in the Cloud IDE environment, use your Personal Access Token instead. Follow the steps in the [Generating Git Token Lab](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/labs/deployment/git_token.md.html "Generating Git Token Lab") for detailed instructions.

The environment may be recreated at any time, so you may find that you have to perform the Initialize Development Environment each time the environment is created.

## Note on Screenshots
Throughout this lab, you will be prompted to take screenshots and save them on your device. These screenshots are required for AI-graded evaluation and peer-graded review at the end of the course.

Your screenshots must have either a .jpg or .png extension.

To take screenshots, you can use various free screen-capture tools or your operating system's shortcut keys. For example:

- Mac: you can use `Shift + Command + 3 (⇧ + ⌘ + 3)` on your keyboard to capture your entire screen, or `Shift + Command + 4 (⇧ + ⌘ + 4)` to capture a window or area. It will be saved as a .jpg or .png file on your Desktop.

- Windows: you can capture your active window by pressing `Alt + Print Screen` on your keyboard. This command copies an image of your active window to the clipboard. Next, open an image editor, paste the image from your clipboard to the image editor, and save the image as .jpg or .png.

::page{title="Create New Repository from Template"}

1. Click this URL to open the starter code project: https://github.com/ibm-developer-skills-network/sfvih-Back-end-Development-Capstone
2. Use the green **Use this template** button to clone this repository to your own private GitHub account.

	**Do not use Fork; use the Template button.**

	![Create new repository from template](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-fork-template.png "Create new repository from template")

3. Give your repository the name `Back-end-Development-Capstone`. This is the name that graders will be looking for to grade your work.
4. Ensure you select the `Public` option for your repository and then create it.

## Assessment

**Option 1: AI-Graded Submission and Evaluation**: Copy and save the **public GitHub URL of the README.md file** from your repository named `Back-end-Development-Capstone` in a text file for the final project submission and evaluation.

**Option 2: Peer-Graded Submission and Evaluation**: Copy and save the **public GitHub repository URL** (not the template) named `Back-end-Development-Capstone` in a text file for peer review.

::page{title="Initialize Development Environment"}

Because the Cloud IDE environment is ephemeral, it may be deleted at any time. The next time you come into the lab, a new environment may be created. Unfortunately, this means that you will need to initialize your development environment every time it is recreated. This shouldn\'t happen too often as the environment can last for several days at a time, but when it is removed, this is the procedure to recreate it.

## Overview
Each time you need to set up your lab development environment, you will need to run three commands.

Each command will be explained in further detail, one at a time.

The commands include:

```
git clone https://github.com/$GITHUB_ACCOUNT/Back-end-Development-Capstone.git
cd /home/project/Back-end-Development-Capstone
bash ./bin/setup.sh
exit
```

Now, let\'s discuss each of these commands and explain what needs to be done.

## Task 1 - Clone the repository
Initialize your environment using the following steps:

1. Open a terminal with `Terminal` > `New Terminal` if one is not open already.

2. Next, use the export GITHUB_ACCOUNT command to export an environment variable that contains the name of your GitHub account.

   > **Note:** Substitute your real GitHub account for the {your_github_account} placeholder below:

```bash
export GITHUB_ACCOUNT={your_github_account}
```

3. Then use the following commands to clone your repository.

```bash
git clone https://github.com/$GITHUB_ACCOUNT/Back-end-Development-Capstone.git
```

## Task 2 - Initialize the development environment

4. Change to the Back-end-Development-Capstone directory, and execute the `./bin/setup.sh` command.
```bash
cd /home/project/Back-end-Development-Capstone
bash ./bin/setup.sh
```

5. You should see the follow at the end of the setup execution:

	![setup script done](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/get_pics_setup_done.png "setup script done")

6. Finally, use the `exit` command to close the current terminal. The environment will not be fully active until you open a new terminal in the next step.

```bash
exit
```

## Validate
To validate that your environment is working correctly, you must open a new terminal because the Python virtual environment will only activate when a new terminal is created. You should have ended the previous task by using the `exit` command to exit the terminal.

1. Open a terminal with `Terminal` > `New Terminal` and check that everything worked correctly by using the `which python` command:

	Check which Python you are using:

	```bash
	which python
	````

	You should get back:

	![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/image39.png)

	Check the Python version:

	```bash
	python --version
	```

	You should get back some patch level of Python 3.9.18:

	![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/image%20\(38\).png)

This completes the setup of the development environment. Anytime your environment is recreated, you will need to follow this procedure.

::page{title="Project Overview"}

You created the `songs` and the `photos` microservices in the last two modules. You are now asked to create the main `Django` website for the band. An incomplete template has been provided by the previous developer. You have already created a repository in your GitHub account from this template. You will now complete the following exercises to run this Django application locally in the lab environment.

::page{title="Exercise 1: Complete Django Data Models"}

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, and others) into your database schema. They are designed to be mostly automatic, but you will need to know when to make migrations, when to run them, and the common problems you might encounter.

There are several commands which you will use to interact with migrations and Django’s handling of database schema:

- **migrate**, responsible for applying and dissociating migrations.
- **makemigrations**, responsible for creating new migrations based on the changes you have made to your models.
- **sqlmigrate**, displays the SQL statements for a migration.
- **showmigrations**, lists a project\'s migrations and their status.

Before you make and run migrations, you need to finish the data models in the code. The classes are provided and you will fill out the data types in this exercise.

## Your Tasks

### Task 1: Create a branch to work on

1. Change into the project directory.
	```bash
	cd /home/project/Back-end-Development-Capstone
	```

1. Since you are working in GitHub, you must pull the latest changes from the main branch to stay up to date. You can then create a new branch.

	The steps are:
	```
	git checkout main
	git pull
	git checkout -b backend-rest
	```

	> This will switch to the main branch, pull the latest changes, and create a new branch. You will be asked to push all your changes to your GitHub repo and merge all code back into your main branch with a pull request.

You can use the `g&#8203;it branch` command to see your current branch:
```bash
git branch
```

Your output should look something like this:
```
$ git branch
* backend-rest
  main
```

### Task 2: Complete the data model classes
Open the `Back-end-Development-Capstone/concert/models.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/models.py"}

1. You will notice that the previous developer left the `Concert` model properties commented out.
	```
	class Concert(models.Model):
		# concert_name
		# duration
		# city
		# date
	```
1. Let\'s add these properites with the following attributes:
	- `concert_name`: CharField with a max_length of 255
	- `duration`: an IntegerField
	- `city`: CharField with a max_length of 255
	- `date`: DateField with the default time of now

1. Similarly, you will notice the `Photo` model commented out:
	```
	class Photo(models.Model):
		# id
		# pic_url
		# event_country
		# event_state
		# event_city
		# event_date
	```

1. You will fill it out with the following attributes:
	- `id`: IntegerField as a primary key
	- `pic_url`: CharField with max_length of 1000
	- `event_country`: CharField with max_length of 255
	- `event_state`: CharField with max_length of 255
	- `event_city`: CharField with max_length of 255
	- `event_date`: DateField with the default time of now

1. Finally, the `Song`model also needs all the attributes as follows:
	- `id`: IntegerField as a primary key
	- `title`: CharField with max_length of 255
	- `lyrics`: TextField

## Solutions
1. `Concert` model should look as follows:
	<details>
		<summary>Click here for the solution.</summary>

	```
	class Concert(models.Model):
		concert_name = models.CharField(max_length=255)
		duration = models.IntegerField()
		city = models.CharField(max_length=255)
		date = models.DateField(default=datetime.now)
	```
	</details>

1. `Photo` model should look as follows:
	<details>
		<summary>Click here for the solution.</summary>

	```
	class Photo(models.Model):
		id = models.IntegerField(primary_key=True)
		pic_url = models.CharField(max_length=1000)
		event_country = models.CharField(max_length=255)
		event_state = models.CharField(max_length=255)
		event_city = models.CharField(max_length=255)
		event_date = models.DateField(default=datetime.now)

	```
	</details>

1. `Song` model should look as follows:
	<details>
		<summary>Click here for the solution.</summary>

	```
	class Song(models.Model):
		id = models.IntegerField(primary_key=True)
		title = models.CharField(max_length=255)
		lyrics = models.TextField()

	```
	</details>

### Task 3: Make and run migrations
1. Create the initial migrations using the `makemigrations` command.
	<details>
		<summary>Click here for a hint.</summary>

	```bash
	python manage.py makemigrations
	```
	</details>
1. Run the migrate command for the migrations you just created.
	<details>
		<summary>Click here for a hint.</summary>

	```bash
	python manage.py migrate
	```
	</details>

## Assessment:

**Option 1: AI-Graded Submission and Evaluation**: Copy and save the **exact terminal output** showing successful execution of the Django migration command in a **text file named `django-migrate`** for the final project submission and evaluation.

**Option 2: Peer-Graded Submission and Evaluation**: Take a screenshot of the terminal showing successful execution of the Django migration command and save it as `django-migrate.jpg` (or `.png`). The screenshot should show the migration completed successfully.

::page{title="Exercise 2: Run the Django App in the Lab Environment"}

Before you proceed with the rest of the backend exercises, you can run the application locally in the lab enivonrment and see the home page.

## Your Tasks
1. Run the `runserver` command to run the application locally.
	<details>
		<summary>Click here for a hint.</summary>

	```bash
	python manage.py runserver
	```
	</details>
	This should start the Django server at port 8000.
1. Curl `localhost:8000` to see if you get a 200 HTTP code from the running server. Note that you are already running the server in the terminal. Open a new terminal or split the existing terminal to execute the curl command:
	```bash
	curl -s -o /dev/null -w "%{http_code}" http://localhost:8000
	```
	You should see an output of `200`:
	```
	(venv) theia:project$ curl -s -o /dev/null -w "%{http_code}" http://localhost:8000

	200(venv)
	```
1. If you got 200 OK, you can proceed to launch the application by clicking `Launch Applciation` icon on the left bar. Once the tab opens, you can enter port as `8000` and click the `Your Application` button.

	![Launch Django App Locally](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-app-local-launch.png "Launch Django App Locally")

	You should see the application open in a new tab. Note that none of the links on the top of the page are working. The remaining exercises in the lab will guide you on how to get these links and the admin site working.
	![Django Application Running Locally](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/djang-app-tab.png "Django Application Running Locally")

## Assessment:

**For both Option 1: AI-Graded Submission and Evaluation and Option 2: Peer-Graded Submission and Evaluation**:
Take a screenshot of the browser running your Django application and save it as `django-app-browser.jpg` (or `.png`).

::page{title="Exercise 3: Fix Songs page"}

The `Songs` page displays all songs and lyrics for each when the user clicks on a song title. Currently, there is no URL mapped to the songs method in the view file. All the URLs are stored in `concert/urls.py` file. You need to add the URL for the songs.

## Your Tasks

### Task 1 : Fix songs URL

Open the `Back-end-Development-Capstone/concert/urls.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/urls.py"}

1. You should see all the URLs defined in this file:
	```
	urlpatterns = [
		re_path(r"^$", views.index, name="index"),
		path("", views.songs, name="songs"),
		...
	]
	```
1. Replace the first empty string for the songs urlpattern with `song/`
	<details>
	<summary>Click here for a hint.</summary>

	```bash
	path("songs/", views.songs, name="songs"),
	```
	</details>

1. If you click on the songs link now, you will get an error. However, you have made progress. Instead of the link not working at all, you are one step closer to getting it to work.

### Task 2 : Fix songs view

The songs link is working, but the view is still broken. Open the `Back-end-Development-Capstone/concert/views.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/views.py"}

1. Go to the method named `songs`.
	```
	def songs(request):
		# songs = {"songs":[]}
		# return render(request, "songs.html", {"songs": [insert list here]})
		pass
	```
1. You will eventually hook this method with the song microservice you created in the previous lab. For now, let\'s return the following dummy data back to the `songs.html` template.
	```
	[{"id":1,"title":"duis faucibus accumsan odio curabitur convallis","lyrics":"Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis."}]
	```

	<details>
		<summary>Click here for a hint.</summary>

	```
	def songs(request):
		songs = {"songs":[{"id":1,"title":"duis faucibus accumsan odio curabitur convallis","lyrics":"Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis."}]}
		return render(request, "songs.html", {"songs":songs["songs"]})
	```
	> Note that you also need to remove the `pass` statement from the last line of the method.
	</details>

1. You should now see a song dislayed when you click the `Songs` page.

	![Songs page working in django](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-songs-page-working.png "Songs page working in django")

1. You should also see the lyrics pop up when you click the song.
	![Songs lyrics modal working](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/djang-songs-modal-working.png "Songs lyrics modal working")

## Assessment:

**For both Option 1: AI-Graded Submission and Evaluation and Option 2: Peer-Graded Submission and Evaluation**:
Take a screenshot of your application showing the modal dialog along with the single song in the background and save it as `django-song-modal.jpg` (or `.png`).

::page{title="Exercise 4: Fix Photos page"}

The `Photos` page displays pictures from past events by the band in different cities across the world. Currently, there is no URL mapped to the photos method in the view file. All the URLs are stored in `concert/urls.py` file. You need to add the URL for the photos.

## Your Tasks

### Task 1 : Fix photos URL

Open the `Back-end-Development-Capstone/concert/urls.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/urls.py"}

1. You should see all the URLs defined in this file:
	```
	urlpatterns = [
		re_path(r"^$", views.index, name="index"),
		path("songs", views.songs, name="songs"),
		path("", views.photos, name="photos"),
		...
	]
	```
1. Replace the first empty string for the photos urlpattern with `photos`.
	<details>
	<summary>Click here for a hint.</summary>

	```bash
	path("photos/", views.photos, name="photos"),
	```
	</details>

1. If you click on the photos link now, you will get an error. However, again, you have made progress.

### Task 1 : Fix photos view
The photos link is working, but the view is still broken. Open the `Back-end-Development-Capstone/concert/views.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/views.py"}

1. Go to the method named `photos`.
	```
	def photos(request):
		# photos = None
		# return render(request, "photos.html", {"photos": photos})
		pass
	```
1. You will eventually hook this method with the pictures microservice you created in the previous lab. For now, let's return the following dummy data back to the `photo.html` template.
	```
	[{
        "id": 1,
        "pic_url": "http://dummyimage.com/136x100.png/5fa2dd/ffffff",
        "event_country": "United States",
        "event_state": "District of Columbia",
        "event_city": "Washington",
        "event_date": "11/16/2022"
    }]
	```

	<details>
	<summary>Click here for a hint.</summary>

	```
	def photos(request):
		photos = [{
		"id": 1,
		"pic_url": "http://dummyimage.com/136x100.png/5fa2dd/ffffff",
		"event_country": "United States",
		"event_state": "District of Columbia",
		"event_city": "Washington",
		"event_date": "11/16/2022"
		}]
		return render(request, "photos.html", {"photos": photos})
	```
	> Note that you also need to remove the `pass` statement from the last line of the method.
	</details>

1. You should now see a photo dislayed when you click the `photos` page

	![Working photos page](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-photos-page-working.png "Working photos page")

## Assessment:

**For both Option 1: AI-Graded Submission and Evaluation and Option 2: Peer-Graded Submission and Evaluation**:
Take a screenshot of your application showing the single photo on the Photos page and save it as `django-photos.jpg` (or `.png`).

::page{title="Exercise 5: Fix the Sign Up flow"}

The `Signup` flow allows the user to create an account with the site so they can book concerts.

## Your Tasks

### Task 1 : Fix `signup` URL

Open the `Back-end-Development-Capstone/concert/urls.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/urls.py"}

1. You should see all the URLs defined in this file:
	```
	urlpatterns = [
		re_path(r"^$", views.index, name="index"),
		path("songs", views.songs, name="songs"),
		path("photos", views.photos, name="photos"),
		path("", views.login_view, name="login"),
		path("", views.logout_view, name="logout"),
		path("", views.signup, name="signup"),
		...
	]
	```
1. Replace the first empty string for the signup urlpattern with `signup/`.
	<details>
	<summary>Click here for a hint.</summary>

	```bash
	path("signup/", views.signup, name="signup"),
	```
	</details>

1. If you were to click the `Signup` link now, you will get an error. However, again, you have made progress and we will fix this error in the next Task.

### Task 2 : Fix Signup View
The Signup link is working, but the view is still broken. Open the `Back-end-Development-Capstone/concert/views.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/views.py"}

1. Go to the method named `signup`.
	```
	def signup(request):
    	pass
	```
1. This view will handle both use cases when the user is asking for the signup form and also when the user is submitting the signup form after adding their details. Let\'s consider the first. You simply return `signup.html` template with the `SignUpForm` form.
	```
	return render(request, "signup.html", {"form": SignUpForm})
	```
1. The second case is a little more involved. You will have to check if the request is a `POST` request. A `POST` request will indicate the user submitted a form. There are a number of steps after this:
	- get the `username` from the request.
	- get the `password` from the request.
	- look for the user with this username.
	- if the user already exists, return to `Signup`page with the message `user already exists`.
	- if the user does not exist, log in the user wih their new credentials, and return to the index page.

	We have provided the following skeleton code to get you started:
	```
	if request.method == "POST":
        username = {insert code to get username from the request}
        password = {insert code to get password from the request}
        try:
            user = {insert code to find user using User.objects.filter method}
            if user:
				return {insert code to render the signup.html page with the SignUpForm form and a message of "user already exist"}
            else:
                user = {insert code to create a new user using the User.objects.create method. Remmeber to use the make_password method to create the password securely}
                {insert code to log in the user with the django.contrib.aut. module}
                {insert code to return the user back to the index page}
        except User.DoesNotExist:
            return {insert code to render the 'signup.html' page with the 'SignUpForm' form}
    return {insert code to render the 'signup.html' page with the 'SignUpForm' form}
	```

1. If your code works without errors, you should now see a sign up form when you click the `signup` link.

	![Django Sign Up form working](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-signup-working.png "Django Sign Up form working")
1. You should be able to create a new user and sign in. However, once you have signed in, the `logout` link is still broken. We will fix that in the next exercise.

## Final Solution
1. Ensure your solution for the login_view method matches the following:
	<details>
	<summary>Click here for the solution.</summary>

	```
	def signup(request):
		if request.method == "POST":
			username = request.POST.get("username")
			password = request.POST.get("password")
			try:
				user = User.objects.filter(username=username).first()
				if user:
					return render(request, "signup.html", {"form": SignUpForm, "message": "user already exist"})
				else:
					user = User.objects.create(
						username=username, password=make_password(password))
					login(request, user)
					return HttpResponseRedirect(reverse("index"))
			except User.DoesNotExist:
				return render(request, "signup.html", {"form": SignUpForm})
		return render(request, "signup.html", {"form": SignUpForm})
	```
	</details>

::page{title="Exercise 6: Fix Login and Logout"}

The `Login` flow allows the user to log in with their account. They are then able to see the concert page with a list of all concerts. The `Logout` flow will log the user out of the application. If you open the application in its current state, you will see the `Login` button, but nothing happens when you click it. Your task in this exercise is to fix both these views.

## Your Tasks

### Task 1 : Fix Login and Logout URL

Open the `Back-end-Development-Capstone/concert/urls.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/urls.py"}

1. You should see all URLs defined in this file:
	```
	urlpatterns = [
		re_path(r"^$", views.index, name="index"),
		path("songs", views.songs, name="songs"),
		path("photos", views.photos, name="photos"),
		path("", views.login_view, name="login"),
		path("", views.logout_view, name="logout"),
		...
	]
	```
1. Replace the first empty string for the login urlpattern with `login/` and the logout urlpattern with `logout/`.
	<details>
	<summary>Click here for a hint.</summary>

	```
	path("login/", views.login_view, name="login"),
	path("logout/", views.logout_view, name="logout"),
	```
	</details>

1. If you click the `Login` link now, you will get an error. However, again, you have made progress and we will fix this error in the next Task.

### Task 2 : Fix Login View
The Login link is working, but the view is still broken. Open the `Back-end-Development-Capstone/concert/views.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/views.py"}

1. Go to the method named `login_view`.
	```
	def login_view(request):
    	pass
	```
1. This view will handle both use cases when the user is asking for the login form and also when the user is submitting a login form. Let's consider the first. You simply return `login.html` template with the `LoginForm` form.
	```
	return render(request, "login.html", {"form": LoginForm})
	```
1. The second case is a little more involved. You will have to check if the request is a `POST` request. A `POST` request would indicate the user submitted a form. There are a number of steps after this:
	- get the `username` from the request
	- get the `password` from the request
	- if the username and password are correct, send them to the index page
	- if the username or password are incorrect, send them back to the login page

	We have provided the following skeleton code to get you started:
	```
	if request.method == "POST":
        if request.method == "POST":
        username = {insert code to get username from the request}
        password = {insert code to get password from the request}
        try:
            user = {insert code to find the user with the username}

            if {insert code to check the username and password}:
                {insert code to log in the using the django.contrib.auth module}
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return {insert code to render the `login.html` method using the `LoginForm` form}
	```

1. If your code works without errors, you should now see a login form when you click the `Login` button.

	![Django login link working](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-login-working.png "Django login link working")

	You can try logging in with the user you created in the previous task. Alternatively, you can sign up as a new user and log in to ensure your code works.

### Task 3 : Fix Logout View
As noted in the previous exercise, the logout link is still broken. Open the `Back-end-Development-Capstone/concert/views.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/views.py"}

1. Go to the method named `logout_view`.
	```
	def logout_view(request):
    	pass
	```
1. The logout view will simply log out the user using the `django.contrib.auth` module. Additionally, it will redirect the user to the login screen.
	<details>
	<summary>Click here for hint.</summary>

	```
	def logout_view(request):
		{insert code to logout the user using the django.contrib.auth module}
		{insert code to return the user to the login page using the HttpResponseRedirect module}
	```
	</details>

	You can test the logout flow by logging in and then clicking on the `Logout` button.

## Final Solution
1. Ensure your solution for the login_view method matches the following:
	<details>
	<summary>Click here for the solution.</summary>

	```
	def login_view(request):
		if request.method == "POST":
			username = request.POST.get("username")
			password = request.POST.get("password")
			try:
				user = User.objects.get(username=username)

				if user.check_password(password):
					login(request, user)
					return HttpResponseRedirect(reverse("index"))
			except User.DoesNotExist:
				return render(request, "login.html", {"form": LoginForm})
		return render(request, "login.html", {"form": LoginForm})

	def logout_view(request):
		logout(request)
		return HttpResponseRedirect(reverse("login"))
	```
	</details>

::page{title="Exercise 7: Fix the Concert Page"}

The `Concert` page shows a logged in authenticated user and their concerts. The user can either attend a concert or choose not to attend. As before, you will first fix the URL and then fix the concert view. You need to sign in as a valid user to test the tasks below. You can log in with a user you created in the previous exercises or create a brand new user.

## Your Tasks

### Task 1 : Fix concert URL

Open the `Back-end-Development-Capstone/concert/urls.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/urls.py"}

1. You should see all the URLs defined in this file:
	```
	urlpatterns = [
		re_path(r"^$", views.index, name="index"),
		path("songs", views.songs, name="songs"),
		path("photos", views.photos, name="photos"),
		path("login/", views.login_view, name="login"),
		path("logout/", views.logout_view, name="logout"),
		path("signup/", views.signup, name="signup"),
		path("", views.concerts, name="concerts"),
		...
	]
	```
1. Replace the first empty string for the concert urlpattern with `concert/`.
	<details>
	<summary>Click here for a hint.</summary>

	```
	path("concert/", views.concerts, name="concerts"),
	```
	</details>

1. If you click the `Concert` link now after logging in as a valid user, you will get an error. However, again, you have made progress and we will fix this error in the next Task.

### Task 2 : Fix Concert View
The Concert link is working, but the view is still broken. Open the `Back-end-Development-Capstone/concert/views.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/views.py"}

1. Go to the method named `concerts`.
	```
	def concerts(request):
    	pass
	```
1. This view will first check if the user is authenticated and if so, show the list of concerts to the user by rendering the `concerts.html` template with the appropriate data. We have provided the following skeleton code to get you started:
	```
	if {insert code to check if the user is authenticated}:
        lst_of_concert = {insert code to create an empty list}
        concert_objects = {insert code to get all Concerts using the Concert.objects object}
        {insert code to loop through all items in the concert_objects}:
            try:
                status = item.attendee.filter(
                    user=request.user).first().attending
            except:
                status = "-"
            lst_of_concert.append({
                "concert": item,
                "status": status
            })
        return {insert code to render the `concerts.html` page with the data of {"concerts": lst_of_concert}}
    else:
        return {insert code to redirect the user to the login page as the user is not authenticated}
	```

1. If your code works without errors, you should now see the list of concerts when you click the `concert` link after logging in as a valid user.

	![Django Concert Page](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-concerts-2.png "Django Concert Page")

Notice that the concert details are not showing up. You will fix this in the next exercise.

## Final Solution
1. Ensure your solution for the login_view method matches the following:
	<details>
	<summary>Click here for the solution.</summary>

	```
	def concerts(request):
		if request.user.is_authenticated:
			lst_of_concert = []
			concert_objects = Concert.objects.all()
			for item in concert_objects:
				try:
					status = item.attendee.filter(
						user=request.user).first().attending
				except:
					status = "-"
				lst_of_concert.append({
					"concert": item,
					"status": status
				})
			return render(request, "concerts.html", {"concerts": lst_of_concert})
		else:
			return HttpResponseRedirect(reverse("login"))
	```
	</details>

---

::page{title="Exercise 8 - Admin and Models"}

You need to create a super user before you can create concerts.

### Task 1: Create a superuser
1. Open the terminal and change into the project directory
	```bash
	cd /home/project/Back-end-Development-Capstone
	```
1. Create a superuser. Remember the username and password. The lab uses a username of `admin`, an email of `admin@admin.com`, and a password of `admin`.
	```bash
	python manage.py createsuperuser
	```
	The output should look as follows:

	![django create superuser](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-create-superuser.png "django create superuser")

### Task 2 : Register Concert model with the admin interface

If you log into the admin site `/admin` with the superuser username and password, you will see that the concert object does not appear there. In this exercise, register the `concert` model with the admin interface.

![Admin broken site](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/django-admin-broken.png "Admin broken site")

Open the `Back-end-Development-Capstone/concert/admin.py` file in the editor.

::openFile{path="Back-end-Development-Capstone/concert/admin.py"}

1. Register the `Concert model` with the admin interface.

	<details>
		<summary>Click here for a hint.</summary>

	```
	admin.site.register(Concert)
	```
	</details>

::page{title="Exercise 9: Push code back to GitHub"}

Now that you have finished the code for the microservice, you can push the `backend-rest` branch back to your GitHub fork. Since you are the only one working on this project, go ahead and merge the PR and delete the branch. Make sure all your code changes are pushed back to the main branch before proceeding to the next lab.

1. Use the `g&#8203;it commit -am` command to commit your changes with the message "implemented django application", and the `g&#8203;it push` command to push those changes to your repository.
> Note: You will be prompted to set up your git user and email the first time you push:
	```
	git config --local user.name "{your GitHub name here}"
	git config --local user.email {your GitHub email here}
	```

	<details>
		<summary>Click here for a hint.</summary>

	```bash
	git commit -am "{message here}"
	git push --set-upstream origin {branch name here}
	```
	</details>

	<details>
	<summary>Click here for a hint.</summary>

	```bash
	git commit -am "implemented django application"
	git push --set-upstream origin backend-rest
	```
	</details>

1. Create a pull request on GitHub to merge your changes into the main branch, and, since there is no one else on your team, accept the pull request, merge it, and delete the branch.

The main branch, at this point, should have your completed code.

::page{title="Conclusion"}

Congratulations! You have finished the Django project. You fixed the URLs and the various views. You also implemented the models that are used in the views and the admin interface. Note that we are hardcoding the songs and photos service. We will connect the real microservices in the final lab of Capstone.

## Next Steps
You have created all the microservices required for this course. You are well on your way to deploying all the services on the cloud.

## Author(s)
CF

## © Copyright IBM Corporation. All rights reserved.

<!--
## Changelog
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2023-02-04 | 0.1 | CF | Initial version created |
| 2023-02-09 | 0.2 | SH | QA pass with edits |
| 2023-02-21 | 0.3 | SH | QA pass after updates |
| 2023-02-21 | 0.3 | CF | Code fixes |
| 2024-01-30 | 0.4 | Manvi Gupta | updated Python version |
| 2026-01-19 | 0.5 | Nikesh Kumar | Update instructions as per PR and MARK |
-->
