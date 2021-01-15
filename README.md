# [Botsi: A Linguist Portal Management System](https://botsi-manager.herokuapp.com/)

<img src="https://github.com/Julia-IO/Linguist_Portal/blob/master/static/img/mockup.png" width="800">

Need to manage complex localization projects? I've also been there!<br> [Botsi - Linguist Portal](https://botsi-manager.herokuapp.com/) is a place to simplify and improve processes for you and your team. This platform allows linguists and project managers to simplify and improve processes for you and your team. This platform allows linguists and project managers to monitor their current and previous projects.
<br>
Please, note registering and access is not free as this app is intended for closed professional teams.<br> In order to access you need to use the following details. <br>
For login as an admin:<br>
Username: admin<br>
Password: project_admin<br>

Once logged as an admin you can create your own Linguist Profile. Also, you can used one of the following already created Linguists' profiles:<br>
Linguist 1:<br>
username: jdiezes<br>
password: eslinguist01<br>

Linguist 2:<br>
username: vlenyfr<br>
password: frlinguist01<br>
<br>
Linguist3: <br>
username: rlamsfussde<br>
password: delinguist01<br>

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Icons**](#icons)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)
    - [**Front-End Technologies**](#front-end-technologies)
    - [**Back-End Technologies**](#back-end-technologies)

4. [**Testing**](#testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)
    - [**Known Issues**](#known-issues)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

This project is part of my [Code Institute](https://codeinstitute.net/) Full Stack Software Development studies, specifically the **Data Centric Development** module. The objective for this milestone project is to create a web application that allows to simplify and improve localization processes", using the **CRUD** operations of **C**reate, **R**ead, **U**pdate, and **D**elete for their projects.

I have decided to build a a project based on the localization industry, since I have personally spent years working as a linguist, project manager and QA specialist and I would have liked to have such a system when collaborating on localization projects.

### User Stories

"**_As a user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: *view the site* from **any device** *(mobile, tablet, desktop)*.
- :white_check_mark: *view all projects* as an **Admin**.
- :white_check_mark: *add* new **linguists** as an **Admin**.
- :white_check_mark: *add* new **projects** as an **Admin**.
- :white_check_mark: *edit* **project categories** as an **Admin**.
- :white_check_mark: *delete* **project categories** as an **Admin**.
- :white_check_mark: *delete* completed **projects** as an **Admin**.
- :white_check_mark: *edit* **projects** as an **Admin**.
- :white_check_mark: *view my only assigned projects* as a **Linguist**.
- :white_check_mark: be able to **log out**.
- :white_check_mark: *filter projects* by **linguist assigned to project**.
- :white_check_mark: *filter projects* by **project lead**.
- :white_check_mark: *filter projects* by **project name**.
- :white_check_mark: *filter projects* by **project language pairs**.


### Design

When it comes to project managing, I think it is important to keep it simple and functional.

#### Framework

- [Materialize 1.0.0](https://materializecss.com/)
    - I really like the modern and clean layout of Materialize as a framework, with its simple-to-understand documentation.
- [jQuery 3.5.1](https://code.jquery.com/jquery/)
    - In an effort to keep the JavaScript minimal, I have decided to use jQuery as foundation to my scripts framework.
- [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
    - Flask is a microframework that I've used to render the back-end Python with the front-end Materialize.

#### Color Scheme

I have opted for a clear background scheme using teal, orange and red in certain buttons to add some color. These standard [Materialize Colors](https://materializecss.com/color.html) work quite well for my project.

- ![#424242](https://placehold.it/15/424242/424242) `#424242` (**grey darken-3** - *navs and footbar*)
- ![#f5f5f5](https://placehold.it/15/f5f5f5/f5f5f5) `#f5f5f5` (**grey lighten-4** - *cardpanels*)
- ![#009688](https://placehold.it/15/009688/009688) `#009688` (**teal** - *main action buttons*)
- ![#f44336](https://placehold.it/15/f44336/f44336) `#f44336` (**red** - *reset/edit buttons*)

#### Icons

- [Materialize Icons](https://materializecss.com/icons.html)
    - I've retained only a select few of the standard Materialize Icons.
- [Font Awesome 5.8.1](https://fontawesome.com/)
    - Although Materialize Icons have nearly 1,000 free-to-use icons, I prefer the look of Font Awesome's icons, and they have more to suit my specific needs for this project. 

#### Typography

- I have used [Google Fonts](https://fonts.google.com/). I have stick to one font: 
    - [Ubuntu](https://fonts.google.com/specimen/Ubuntu)


### Wireframes

For my wireframes, I have used sketches on a notebook. It's how I like it the best.

##### back to [top](#table-of-contents)

---


### Existing Features

**Register Account**
- Not everybody can register and create their own unique account. As this app is intended for professional teams, only the Admin will be able to add new linguists to the team (or delete them). All passwords are hashed for security purposes!
In order to check how Linguists Account are created, you'll need to use the following username and user password:
Username: admin
Password: project_admin

The Admin is granted with full permission to get all the info displayed and he/she can also edit, create and delete certain categories.



**Log In to Account**
- Linguists can access using the login details provided by their admin and can only view a dashboard with the projects assigned to them. They can also access to their profile data.

I have created 3 linguists as example:
Linguist 1:
username: jdiezes
password: eslinguist01

Linguist 2:
username: vlenyfr
password: frlinguist01

Linguist3: 
username: rlamsfussde
password: delinguist01


**Log Out of Account**
- Users can easily log out of their account with the click of a button.

**Delete Account**
- Only Admin can delete accounts.

**View All Projectss**
- Only Admin can view All Projects and also edit and/or delete them once completed.

**View Assigned Projectss**
- Linguists can view only their assigned projects.

**Search Projects**
- Search functionality is provided to search by linguist assigned, language pairs, project lead or project name.

**Add a Project/ Category**
- Only available to Admin account.
- [**C**RUD] Create or 'add' a new category/service and or project and or linguist.

**Update a Project**
- Only available to Admin account.
- [CR**U**D] Update or 'edit' categories and/or projects.

**Delete a Recipe**
- Only available to Admin account.
- [CRU**D**] Delete or 'remove' categories and/or projects.


### Features Left to Implement

In an ideal world, there are a couple items that I would've loved to have completed as well, but just didn't have the time or knowledge just yet as to how to implement these features.

- Right now there is just 1 admin, but if teams grow we can expect to have several admins. Approach as to how to grant permissions should be improved so that Project Leads can also have specific permissions.
- I'd like linguists to be able to mark their projects as Completed. Once a project is marked as completed, I'd like automatic mails to be sent to Project Leads.
- I'd like linguists to be able to automate billing process once a project is completed. State of payments should also be displayed in their profiles.
- I'd like to include downloadable files to the Projects Overview and downloadable invoice files to Linguist's profiles.

##### back to [top](#table-of-contents)

---

## Technologies Used

- [VS Code](https://code.visualstudio.com/) - Used as my primary IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code online.
- [Photoshop CS6](https://www.adobe.com/Photoshop) - Used for editing images.
- [TinyPNG](https://tinypng.com/) - Used to compress images for faster loading.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [jQuery 3.5.1](https://code.jquery.com/jquery/) - Used as the primary JavaScript functionality.
- [Materialize 1.0.0](https://materializecss.com/) - Used as the overall design framework.
- [LeafletJS](https://leafletjs.com/): Used for Admin visitor tracking purposes.


### Back-End Technologies

- **Flask**
    - [Flask 1.1.2](http://flask.pocoo.org/) - Used as a microframework.
    - [Jinja 2.11](http://jinja.pocoo.org/docs/2.11/) - Used for templating with Flask.
    - [Werkzeug 1.0.1](https://werkzeug.palletsprojects.com/en/0.16.x/) - Used for password hashing, authentication, and authorization.
- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.
- **Python**    
    - [Python 3](https://www.python.org/) - Used as the back-end programming language.
    - [MongoDB Atlas](https://www.mongodb.com/) - Used to store my database in the 'cloud'.
    - [PyMongo 3.8.0](https://api.mongodb.com/python/current/) - Used as the Python API for MongoDB.

##### back to [top](#table-of-contents)

---

## Testing

**Creating an Account**

I've created1 admin account and 3 linguists accounts in order to confirm authentication and validation worked as expected.

**Add | Edit | Delete a Project**

I've created about 3 projects. These recipes were created the admin account, the only one with the necessary permissions.

**Pagination**

When implementing pagination, I had a lot of manual tests to undergo, in order to make pagination work for multiple scenarios. I needed to test that all aspects of pagination worked with and without the option for searching the database. These included:


**Profile**

As a **linguist user**, there are four profile buttons.

- *View your own assigned projects*:
    - You can check your assigned projects and get all the info you need to start working + contact info of the Project Lead.
- *View your profile*:
    - You can check if all your data is correct (including billing and paypal info) and contact the relevant email address in case you need to update your info.
- *Log out*:
    - You can easily log out from your account with a clear Log Out button in the navbar.


As the **Admin**, you can do the same as the linguists, but you can see ALL THE PROJECTS and also edit and/or delete them. Besides, you can:

- *Add New Project*:
    - You can create a new project providing all the relevant info linguists will need such as project lead, instructions, language pairs, specialization, CAT Tool or software to be used and due date.
- *Add New Linguist to the team*:
    - You can add new linguists to the team including contact, language pairs, billing and paypal info.
- *Manage Categories of services*:
    - You can easily create, edit and/or delete new categories / services offered.

### Validators

**HTML**
- [W3C HTML Validator](https://validator.w3.org) - Unfortunately the W3C Validator for HTML does not understand the Jinja templating syntax, so it therefore shows a lot of errors with regards to `{{ variables }}`, `{% for %} {% endfor %}`, etc. Aside from the Jinja warnings and errors, all of the remaining code is perfectly validating. Also due to the Jinja templating, certain elements cannot be 'beautified' across multiple lines, and must remain on a single line. An example of this is the `<select>` element, which is rather long with specific Materialize classes, and Jinja templating.

**CSS**
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - As I've mostly have used Materialize, my style.css is quite simple and it has been properly validated.

**JavaScript**
- [Beautify Tools](http://beautifytools.com/javascript-validator.php)
    - No syntax errors!

**Python**
- [PEP8 Online](http://pep8online.com/)
    - My `.py` file contains severak E501 errors (line too long (83 > 79 characters) and several 261 errors (at least two spaces before inline comment) that I need to research upon and try to get fixed.)

### Compatibility

To ensure a broad range of users can successfully use this site, I tested it across the 6 major browsers in both desktop and mobile configuration.

- Chrome *v.74*
- Edge *v.18*
- Firefox *v.67*
- Safari *v.12*
- Opera *v.56*
- Internet Explorer *v.11*

### Known Issues

During development, I discovered two issues after committing to GitHub. For both of these bugs, I opened and *issue* on GitHub so I could come back and properly fix them.

- When editing a project as an admin, I wanted the previous info to get displayed. For some reason, the Type of Project is not always displayed.


##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

Please note - in order to run this project locally on your own system, you will need the following installed:
- [Python3](https://www.python.org/downloads) to run the application.
- [PIP](https://pip.pypa.io/en/stable/installing) to install all app requirements.
- Any IDE such as [Microsoft Visual Studio Code](https://code.visualstudio.com).
- [GIT](https://www.atlassian.com/git/tutorials/install-git) for cloning and version control.
- [MongoDB](https://www.mongodb.com) to develop your own database either locally or remotely on MongoDB Atlas.

Next, there's a series of steps to take in order to proceed with local deployment:

- Clone this GitHub repository by either clicking the green *Clone or download* button and downloading the project as a zip-file (remember to unzip it first).
- Navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
- Create a `.env` file with your credentials. Be sure to include your *MONGO_URI* and *SECRET_KEY* values.
- Create a `.flaskenv` file and add the following entries:
    - `FLASK_APP=run.py`
    - `FLASK_ENV=development`
- Install all requirements from the [requirements.txt](https://github.com/Julia-IO/Linguist_Portal/blob/master/requirements.txt) file using this command:
    - `sudo -H pip3 -r requirements.txt`
- Sign up for a free account on [MongoDB](https://www.mongodb.com) and create a new Database called **project_manager**. The *Collections* in that database should be as follows:

**CATEGORIES**
```
_id: <ObjectId>
category_name: <string>
```

**LEADS**
```
_id: <ObjectId>
project_lead: <string>
```

**PROJECTS**
```
_id: <ObjectId>
project_name: <string>
category_name: <string>
project_lead: <string>
assigned_toe: <string>
project_description: <string>
project_languages: <string>
project_specialization: <string>
project_software: <string>
project_due_date: <string>
project_status: <string>
project_is_overdue: <string>
created_by: <string>
```

**STATUS**
```
_id: <ObjectId>
project_status: <string>
```

**USERS**
```
_id: <ObjectId>
full_name: <string>
email_address: <string>
source_language: <string>
target_language: <string>
billing_info: <string>
paypal_account: <string>
username: <string>
password: <string>
is_admin: <string>
```

- You should now be able to launch your app using the following command in your terminal:
    - `flask run`
- The app should now be running on *localhost* on an address similar to `http://127.0.0.1:5000`. Simply copy/paste this into the browser of your choice!

### Remote Deployment

This site is currently deployed on [Heroku](https://www.heroku.com/) using the **master** branch on GitHub. To implement this project on Heroku, the following steps were taken:

1. Create a **requirements.txt** file so Heroku can install the required dependencies to run the app.
    - `sudo pip3 freeze --local > requirements.txt`
    - My file can be found [here](https://github.com/Julia-IO/Linguist_Portal/blob/master/requirements.txt).
2. Create a **Procfile** to tell Heroku what type of application is being deployed, and how to run it.
    - `echo web: python run.py > Procfile`
    - My file can be found [here](https://github.com/Julia-IO/Linguist_Portal/blob/master/Procfile).
3. Sign up for a free Heroku account, create your project app, and click the **Deploy** tab, at which point you can *Connect GitHub* as the Deployment Method, and select *Enable Automatic Deployment*.
4. In the Heroku **Settings** tab, click on the *Reveal Config Vars* button to configure environmental variables as follows:
    - **IP** : `0.0.0.0`
    - **PORT** : `5000`
    - **MONGO_URI** : `<link to your Mongo DB>`
    - **SECRET_KEY** : `<your own secret key>`
    - **MY_ADDRESS** : `<your own email address>`
    - **SEND_TO** : `<recipient email address>`
    - **PASSWORD** : `<you own email password>`
5. Your app should be successfully deployed to Heroku at this point. :tada:


##### back to [top](#table-of-contents)

---

## Credits

### Content

- [*"How to Write a Git Commit Message"*](https://chris.beams.io/posts/git-commit/) by **Chris Beams** (*as recommended by Code Institute assessors on previous projects*)
- [*"Primer on Jinja Templating"*](https://realpython.com/primer-on-jinja-templating/) (*as recommended by Code Institute assessors on this project*)
- [*"Jinja Templating Documentation"*](https://jinja.palletsprojects.com/en/2.11.x/)

### Media

Sources of the images used on this site:

- **Logo** : the Tobetranslated was designed for me by my friends of [*"Nueve Estudio"*](https://www.n-u-e-v-e.com/)

### Code

- I've followed the videos of the Mini Project and I have adapted the code provided to meet my own project requirements.

### Acknowledgements
- Aaron Synnott
    - My mentor. Thanks for e-meeting and give me your opinions and helpful insights.

- [Tim Nelson](https://github.com/TravelTimN)
    - My most recurrent code tutor. I have also used one of your Read Me files as a template of my own.
- Cormac Lawlor
    - Code Institute Tutor: Thanks for helping me with my last-minute deployment issue with Heroku.

##### back to [top](#table-of-contents)
