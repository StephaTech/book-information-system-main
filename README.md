# Book Club Library-information-system
ESSA Final Project 

This repository contains the source code and documentation for the Book Club Library-information-system, a project developed as part of a ESSA class assignment.The system is designed to digitize the manual process of tracking books on a physical bookshelf, enabling members to access and manage their library anytime, anywhere, with just a few clicks.


How to install
Install Django and Python and make sure the version are updated
Download the zip file in your machine

at terminal type below commands
  
django-admin startproject bis_portal     
python manage.py startapp bis_app  
make sure you are on this folder cd bis_portal   
python manage.py runserver    

To create a user for django admin
python manage.py createsuperuser 

Migrations
To create some tables and database
python manage.py makemigrations
python manage.py migrate
