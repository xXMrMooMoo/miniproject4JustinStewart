### INF601 - Advanced Programming in Python
### Justin Stewart
### Mini Project 4

## Description
This project is a web application built using Django that serves as a polling platform. Users can register, log in, and participate in polls by voting on questions. The application includes dynamic features such as user authentication, custom toasts for feedback, and responsive design using Bootstrap.

Administrators can manage polls, questions, and user profiles through the Django admin interface. The project highlights the integration of Django's built-in functionalities with modern web development tools, including Bootstrap for UI enhancements and Django Debug Toolbar for efficient debugging. This app serves as a demonstration of a full-stack web application built with best practices in mind.

### Pip Install Instructions/Dependencies

* Please run the following to install all the packages:
```
pip install -r requirements.txt
```
* To initialize and run the database please run the following:
```
python manage.py makemigrations
python manage.py migrate
```
* To create a user please run the following:
```
python manage.py createsuperuser
```

### Executing program

* In a terminal window, please type the following:
```
 python manage.py runserver
```

### Output
By default, when running, this program will output a link to navigate the user to a html environment:
```
http://localhost:8000/
```

## Authors
Justin Stewart

## Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/)
* [Django Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
* [Bootstrap Modals](https://getbootstrap.com/docs/4.0/components/modal/)




