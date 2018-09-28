# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

# Local
## Setting up a new virtual environment
Install [Virtualenv](https://virtualenv.pypa.io/en/stable/)

    $ pip install virtualenv	

### Create
Replace ENV with whatever you would like your virtual environment to be called.

    $ virtualenv ENV
    
### Activate
#### Windows
    $ cd ENV/Scripts
    $ activate

#### Mac/Linux
    $ cd ENV
    $ source bin/activate

You can tell what environment you are currently in by looking at the name in parenthesis that is now visible on the terminal

    $(ENV) C:/Path/To/Files

## Installing Dependencies

Now that we have the virtual environment set up, dependencies will need to be installed. These are all managed in the requirements.txt document.

Navigate to the projects folder

    aagroup17/

and install the required dependencies

    $(ENV) pip install -r requirements.txt

## Creating a Database
Currently the application uses a simple sqlite3 local database. You will need to generate this first in order for the application to work

Navigate to the project directory

    aaogroup17/
and migrate the database

    $(ENV) python manage.py migrate

this will create a db.sqlite3 file that is located in

    aaogroup17/aao_cutout_api

## Starting the Server
Now that we are in our environment, with dependencies install, and database migrated, we can start the application server.

To start the server

    $(ENV) cd aaogroup17
    $(ENV) python manage.py runserver

In your browser navigate to

    localhost:8000

or alternatively

    localhost:8000/CutoutQuery/

If you would like to stop the server navigate to your open terminal and press

    CTRL + C

If you would like to leave your virtual environment

    $(ENV) deactivate


* Configuration
* Dependencies
	- Python 3.6.5
	- DJango 1.11.4
	- Django Rest Framwork >=3.8.2
	- Pytest >=3.7.3
	- Requests
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact