## Before starting
make sure
- [] Python is installed
- [] django is installed
- [optional] Virtual environment is created
- [for now] PyCharm IDE is setup


## Create project
```
django-admin startproject <project-name>
```

myproj                  [this is just a project container, can be changed]
├── manage.py           [command line utility to interact with django project]
└── myproj              [python package of the project]
    ├── asgi.py         [entry point for ASGI server (Asynchronous Server Gateway Interface)]
    ├── __init__.py     [like constructor, due to this it is package]
    ├── settings.py     [contains configuration of the project]
    ├── urls.py         [contains links of project or path and the function or class to call]
    └── wsgi.py         [entry point for WSGI server (Web Server Gateway Interface)]


## Create App
```
python manage.py startapp <app-name>
```

myproj
├── db.sqlite3
├── manage.py
├── myapp                   [application directory/py package]
│   ├── admin.py        
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations          [DB/ORM to SQL things]
│   │   ├── __init__.py
│   ├── models.py           [uses to create DB table thru Model class]
│   ├── tests.py    
│   ├── urls.py             [routing/links inside the app]
│   └── views.py            [views controller things]
│   └── templates
│  	    └──myapp                   
│   	   ├── template.html   [Actual UI things that shown in browser using DT(jinja)]
└── myproj
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
