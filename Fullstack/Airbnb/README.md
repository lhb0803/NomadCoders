# 0. Introduction
* Backend: Django
* Frontend: ReactJS

## 0.2 Why Django
* No need to reinvent the wheel (Free, Easy Framework)
    * ex) Admin panel, Database communication, User Authentication...
* Reassuringly secure
* Exceddingly scalable
* Incredibly versatile

## 0.3 Django vs Flask
* Flask is very minimal
* Flask = lego pieces <-> Django = box, full of toys
* Minimalism <-> Maximalism

# 1. Set up
## 1.0 Python3
```
conda create -n "airbnb" python=3.10
conda activate airbnb
```
## 1.1 Poetry
* [Installation](https://python-poetry.org/docs/#installation)
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
* Package Management (like a bubble)
    * [Conda + Poetry](https://stackoverflow.com/questions/70851048/does-it-make-sense-to-use-conda-poetry)
* `poetry shell`: enter the bubble -> `exit`: get outside the bubble
* `poetry.lock`, `pyproject.toml`: two files that make a bubble

## 1.2 Start Project
* start project
    ```
    poetry shell
    django-admin startproject config .
    ```
* vscode gitignore extension

# 2. OOP With Python
* The 4 Pillars of OOP: Abstraction, Encapsulation, Inheritance, Polymorphism

## 2.1 Constructor
* `__init__`: constructor in Python
* `self`: default parameter

## 2.2 Inheritance
* extends class and re-use

## 2.3 `super()`
* `super()`: call parent class
* `super().__init__()`: initialize parent class

## 2.4 Recap
* Django is OOP Framework
* Override
* underscore methods

## 2.5 dir
* underscore method
* internally Python runs `__str__` method
* `print(dir(object))`: print properties and methods of class => very userful when extending class and overriding

# 3 Django Basics
## 3.0 Run Server
```
python manage.py runserver
```
* cannot run `poetry shell` on anaconda env
* 127.0.0.1:8000/admin: error yet

## 3.1 Migrations
* Django is looking at db.sqlite3 (django_sesion) -> looking for admin session
* Django has 18 files somewhere and we run those files and the files will modify our database
* Migration: modification of shape (state) of database
    ```
    python manage.py migrate
    ```
* Now, admin panel is applied
* Migration will be used a lot

## 3.2 Recap
* delete db -> run server again: error messages
    ```
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    ```
* Migration file: files including python code that **transforms database**
* Django has many built-ins

## 3.3 Super User
```
python manage.py createsuperuser
```
* Django create our username to database
* Now, we get admin panel (for free)
* It's not static: it's functional

## 3.4 Framework vs Library
* Django is Framework
* Library is like requests: we import and call
    * We write methods, class and other codes using the library
* Framework calls our code: framework looks our code and call it
    * `config/settings.py`: Django looks the variable `TIME_ZONE` and uses it
    * depending on my code, framework changes its action
    * `config/urls.py` (another example): Django uses the variable to get admin url
    * Django is **always looking at variables**
    * We are in Django house and we should follow Django rules

## 3.5 Apps
* Apps = Folders: Data & Logic
* Django capsulates data + logic of an application
    * should write each capsule for application => capsule: Module
    * each applications link to each other
* Modularity makes application more organizable

## 4.0 Models
* startapp
    ```
    python manage.py startapp houses
    ```
* admin, model
    * model: description of shape of data
    * Django will talk to database for you with model
    * more descriptive, better talk to database
    * Django doesn't know about the model until we add config
        * -> `config/settings.py` -> add `INSTALLED_APPS`

## 4.1 Migrations
* Django will automatically generage admin panel for your custom data
* at `admin.py`, make HouseAdmin class
* no such table error: shape of database doesn't match with what Django wants
    * database doesn't know about House model
    * we should inform database about House model
    * Migration: modeify shape of database
        ```
        python manage.py makemigrations
        python manage.py migrate
        ```

## 4.2 Recap
* Django translates python code to sql

## 4.3 Admin
* framework: write correct property at correct places
* customize House class's string method
* customize HouseAdmin's property
    * list, filter, search