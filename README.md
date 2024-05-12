
# Assesment 

This repository contains a simple Management System implemented in Python, utilizing MySQL for data storage. The system includes functionalities for storing Email, Name of user.


## Requirements
=> python
=> Django

## setup
To setup Django application Follow these steps

=> Download the Source Code from the github
=> open the source code in IDE 
=> Install requirements.txt using the command
 -->pip install requirements.txt
## Connecting Database in Django Application
->After installing requirements Go To Project Setting.py file and put MySQL configrations to connect Django ORM to MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost', 
        'PORT': '3306',       
    }
}


## Admin Interface 
After Adding Database Follow these step to Create Admin Interface
1.run command  (py manage.py makemigrations) in the   terminal 
2 run command (py manage.py migrate ) in the terminal
3 run command (py manage.py createsuperuser) in the terminal and enter userid,Email and Password 

## Run Application
to run the Application you should Follow these command in the terminal
1.run command (py manage.py runserver )
2.This command will start server at http://127.0.0.1:8000/
3.than after we can use the Application

## Task 2
Because Django provies ORM so we don't need to write Raw Sql quries django take care of it 
## Git Workflow
1. Clone the Repository:clone the github Repository using command (git clone https://github.com/shubhamg9074/new_app.git) This will create a local copy of the project.
2.Changes. Make the necessary changes to the project files using terimal
3.Commit Changes: commit Changes using command(git commit -m "Message")
4.pushc changes:push the changes in the github Repository using command(git push origin steptech_assignment)
5.create pull Request:Go to the repository on GitHub.Click on "Compare & pull request" for your steptech_assignment branch.Click on "Create pull request" to submit your changes for review.

## Screenshots

![Home](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/home.png?raw=true)

![form](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/form.png?raw=true)

![users_list](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/users_list.png?raw=true)

![one_user](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/oneuser.png?raw=true)

![Admin1](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/admin4.png?raw=true)

![Admin2](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/admin5.png?raw=true)

