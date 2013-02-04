gui
===

Python Django GUI

**Database Setup**

CREATE DATABASE gui DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
CREATE USER 'gui'@'%' IDENTIFIED BY 'gui';
GRANT ALL PRIVILEGES ON `gui` . * TO 'gui'@'%';

**Server Setup**
python manage.py syncdb
