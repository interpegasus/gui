gui
===
Python Django GUI + User Authentication System


Django Installation & Tutorial
==============================
- https://www.djangoproject.com/download/
- https://docs.djangoproject.com/en/1.4/intro/tutorial01/


Database Setup (MySQL)
======================
  CREATE DATABASE gui DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; CREATE USER 'gui'@'%' IDENTIFIED BY 'gui'; GRANT ALL PRIVILEGES ON gui . * TO 'gui'@'%';


Server Setup
============
  python manage.py syncdb
  python manage.py runserver
