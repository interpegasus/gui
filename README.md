UI Project
==========
Python Django UI + User Authentication System

INSTALLATION
============
- Clone repository via: 'git clone https://github.com/interpegasus/gui.git'

Django Installation & Tutorial
==============================
- https://www.djangoproject.com/download/
- https://docs.djangoproject.com/en/1.4/intro/tutorial01/


Database Setup (MySQL)
======================
  CREATE DATABASE gui DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; CREATE USER 'gui'@'%' IDENTIFIED BY 'gui'; GRANT ALL PRIVILEGES ON gui . * TO 'gui'@'%';


Server Setup
============
- python manage.py syncdb
- python manage.py runserver

Default Server URL
==================
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/
