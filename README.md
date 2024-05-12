
# Assesment 

This repository contains a simple Management System implemented in Python, utilizing MySQL for data storage. The system includes functionalities for storing Email, Name of user.


## Requirements
=> python<br>
=> Django

## setup
To setup Django application Follow these steps

=> Download the Source Code from the github<br>
=> open the source code in IDE <br>
=> Install requirements.txt using the command<br>
 -->pip install requirements.txt<br>
## Connecting Database in Django Application
->After installing requirements Go To Project Setting.py file and put MySQL configrations to connect Django ORM to MySQL

DATABASES = {<br>
    'default': {<br>
        'ENGINE': 'django.db.backends.mysql',<br>
        'NAME': 'your_database_name',<br>
        'USER': 'your_mysql_user',<br>
        'PASSWORD': 'your_mysql_password',<br>
        'HOST': 'localhost',<br> 
        'PORT': '3306',<br>       
    }<br>
}<br>


## Admin Interface 
After Adding Database Follow these step to Create Admin Interface
1.run command  (py manage.py makemigrations) in the   terminal <br>
2 run command (py manage.py migrate ) in the terminal<br>
3 run command (py manage.py createsuperuser) in the terminal and enter userid,Email and Password <br>

## Run Application
to run the Application you should Follow these command in the terminal
1.run command (py manage.py runserver )<br>
2.This command will start server at http://127.0.0.1:8000/<br>
3.than after we can use the Application<br>

## Task 2
Because Django provies ORM so we don't need to write Raw Sql quries django take care of it 
## Git Workflow
1. Clone the Repository:clone the github Repository using command (git clone https://github.com/shubhamg9074/new_app.git) This will create a local copy of the project.<br>
2.Changes. Make the necessary changes to the project files using terimal<br>
3.Commit Changes: commit Changes using command(git commit -m "Message")<br>
4.pushc changes:push the changes in the github Repository using command(git push origin steptech_assignment)<br>
5.create pull Request:Go to the repository on GitHub.Click on "Compare & pull request" for your steptech_assignment branch.Click on "Create pull request" to submit your changes for review.<br>

## Screenshots

![Home](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/home.png?raw=true)

![form](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/form.png?raw=true)

![users_list](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/users_list.png?raw=true)

![one_user](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/oneuser.png?raw=true)

![Admin1](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/admin4.png?raw=true)

![Admin2](https://github.com/shubhamg9074/New_App/blob/steptech_assignment/screenshots/admin5.png?raw=true)

