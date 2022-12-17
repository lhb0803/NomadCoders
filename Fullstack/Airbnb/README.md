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