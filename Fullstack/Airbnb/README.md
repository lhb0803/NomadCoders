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

# 3. Django Basics
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

# 4. Django Apps
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

## 4.4 Documentation
* [Django document](https://www.djangoproject.com/)
    * A lot of fields

# 5. Users App
## 5.0 Introductions
* Django's vanila user admin model provides various functions
* But, we need to customize it
    * Option 1. We will create `Profile` model using `User` model in Django
* If you use default `User` model, it is very difficult to change in the mid of the project

## 5.1 Custom Model
```
python manage.py startapp users
```
* import from default [user model](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)
    * inherit AbstractUser
* delete db and all migrations
    * notice not migration dir, just `000x_xxxx.py`
* re create super user by `python manage.py createsuperuser`


## 5.2 Custom Fields
* customize abstract user model
* make ghost field (necessary in AbstractUser model, but not in Custom User model)
    * `editable = False`
* Whenever you change models.py, you need to **make migration and migrate**

## 5.3 Defaults
* We should sync Django code and Database -> migration
* Cuase of migration error: non-nullable field `is_host`
    * if no default option: when add `is_host` column value to existing row, Django asks you to select what the value would be
    * `null = True` option: nullable

## 5.4 Custom Admin
* to see customizable option in Admin panel, you should customize UserAdmin

## 5.5 Foreign Keys
* How we can connect each models
* Django automatically creates `id` (aka `pk`)
* `models.ForeignKey("users.User", on_delete=models.CASCASE)`

## 5.6 Super Mega Recap
* `defaults`: when add new column, how handle pre-existing data
* relationship of each model
* VScode extensions: SQLite Viewer -> make db.sqlite3 viewable table form

# 6. Models and Admin
## 6.0. User Model
* `models.ImageField()`
    ```
    poetry add Pillow
    ```
* optional CharField: make class inheriting from `models.TextChoices`
* `blank = True` allows empty data (different than allowing null)

## 6.1. Room Model
```
python manage.py startapp rooms
```
* many to many relationship

## 6.2 Many to Many
* `auto_now_add = True`: added when object is created
* `auto_now = True`: added when updated
* copy paste? -> No!
    * use common model
    * `class Meta: abstract = True`: make the model not visible in database

## 6.3 Recap
* Many to Many
* `CommonModel`
    * `abstract = True`: Django ignores the model (not add to database)
* How to add `Amenity` object

## 6.4 Rooms Admin
* `__str__(self)`: can customize print name
* `verbose_name_plural`
* change column name -> run `python manage.py makemigrations` again

## 6.5 Experiences
* recap for making models and admins

## 6.6 Categories
* category choices -> Rooms, Experiences

## 6.7 Reviews
* can be included in Rooms, Experiences

## 6.8 Wishlists
* a wishlist can include many rooms or experiences => ManyToManyField
* a wishlist is owned by a single user => ForeignKey

## 6.9 Bookings
* a booking model is owned by a single user => ForeignKey
    * a user can have many booking models
* a booking model can have a single room => ForeignKey
* `blank = True`: for Django admin

## 6.10 Medias
* `OneToOneField`: unique
    * video - experience is one-to-one
    * usage example: payment information

## 6.11 Direct Messages
* you can check config name in `/apps.py`
* related_name argument error: error when a same name user **has same Foreign Key**
* `/apps.py`: can customize verbose_name

# 7. ORM
## 7.0 Introductions
* ORM: Object Relational Mapper
    * When you build database, Django provides database-abastraction API that lets you create, retrieve, update and delete objects
    * Now, we learn **how we talk with database**
    * Not using admin panel, but with **Python code**!
* `python manage.py shell`: opens console (configured Django: all aplications installed)
    ```python
    from rooms.models import Room

    Room.objects.all() # get all Room objects
    room = Room.objects.get(name="First Home") # get by name
    room.pk # primary key
    room.id # room's id
    room.owner # room's owner (user)
    room.owner.email # room's owner's email
    room.price = 3000
    room.save() # given by Django
    ```

## 7.1 filter, get, create, delete
* Manager (=`.objects`): interface that talks to database
    * `objects.all()`: get all models
    * `objects.get()`: get unique model (when 0, 2+ returns error)
    * `objects.filter()`: get certain model with condition => very powerful
        * `__gt`: greater than
        * `__gte`: greater than or equal
        * `__contains`: string that contains certain word
    * `objects.create()`: creates data => you don't have to use admin panel
        ```python
        from rooms.models import Amenity
        Amenity.objects.create(name='Amenity from the console', description='How cool is this')
        ```
    * `model.delete()`
        ```python
        to_delete = Amenity.objects.get(pk=4)
        to_delete.delete()
        ```

## 7.2 QuerySets
* `QuerySet`: allows chain operation
    * example) double filtering
    ```python
    Room.objects.filter(pet_friendly=True).exclude(price__lt=15).filter(name__contains="서울")
    ```
* `QuerySet` is lazy: only gives you specific data when you actually read it (use it)
    * hit database with **less traffic**

## 7.3 Admin Methods
* `filter method`: Lookups method ([link](https://docs.djangoproject.com/en/4.1/topics/db/queries/))
* when you add column in `list_display` or `list_filter`, Django is trying to look for that columns inside model: **Django looks for _attribute_ or _method_**
    * Option 1. add `total_amenities` method in `models.py`
    * Option 2. add `total_amenities` method in `admin.py`

## 7.4 ForeignKey Filter
* reverse acessors: to know "Who is pointing to me?"
    * if foreign key, __operation can work with foriegn key's field
        ```python
        # rooms created by "hyobae"
        Room.objects.filter(owner__username="hyobae")
        ```
    * `review.user` vs `user.reviews`

## 7.5 Reverse Accessors
* `xxx_set`: reverse accessors
    ```python
    from users.models import User
    me = User.objects.get(pk=1)
    dir(me) # returns all attributes and methods
    me.room_set.all() # all rooms created from me
    ```
* when you assign a foreign key to a model, **the foreign key will recieve `xxx_set` automatically**

## 7.6 related_name
* customize reverse accessors
* model B assigns model A as foreign key => model A automaticall receives `B_set`
* in `rooms.models.py`
    ```
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")
    ```

## 7.7 Recap
* Rooms -> User
* User <- Rooms

# 8. Power Admin
## 8.0 Methods
* How to optimize querying database
    * Not recommended
        ```python
        self.reviews.all()
        ```
        -> because, return all fields even we do not use
    * Recommended
        ```python
        self.reviews.all().values("rating")
        ```

## 8.1 Search Fields
* `search_fields`: Django looks contains that word
    * how to change startswith?
        * use '^'
    * how to change exact?
        * use '='
* search by foreignkey
    * `owner__username`

## 8.2 Admin Actions
* delete action
* decorator: `@admin.action()`
    * request option: can assure whether the user is superuser or not
* `actions = (action_func, )`

## 8.3 Custom Filters
* with postfix `__`, you can use the model's field (by relationship)
* When you want to make your own filter: Custom Filter
* make class in `admin.py` which inherits `admin.SimpleListFilter`
    1. `title`: filter name
    2. `paramter_name`: parameter name which receives value from `lookups()` function
    3. define function `lookups()`
        - `lookups()` takes three arguments: `self`, `request`, `model_admin`
    4. define function `queryset()`
        - `queryset()` takes three arguments: `self`, `request`, `query_set`
        - **`query_set` can be filtered and chained**

### Code Challenge!
* filter that returns bad score reviews

## 8.4 Recap
* Search Fields
* Admin Action
* Custom Filter

# 9. URLs and Views
## 9.0 Views
* `config/urls.py`: the file Django is looking at when a user goes to specific url
* First option: add all url in `urlpatterns`
* Second option: add url for every application (divide and conquer)
* `models/views.py`: view is a funciton when a user goes to specific url
    * **name doesn't have to be "view"**: Django doesn't look `views.py`
    * function `say_hello` automatically receives request object: can know who request and what request
    * function `say_hello` should return http response
* `urlpatterns` list in urls.py: `path(url, function executed when user enters the url)`

## 9.1 include
* divide and conquer
* `include("rooms.urls")`: Django finds urls.py in rooms directory
    * at `rooms/urls.py`: "rooms/" is considered as root directory so you just write "" in urlpatterns to go to "/rooms"

## 9.2 URL Arguments
* How to pass argument to url
* `path("<int:room_id>", views.see_one_room)`
* need to make argument for `see_one_room` function

## 9.3 render
* How to render a template
    * How to put data to HTML and show users
* `render()`: Django automatically looks for HTML template

## 9.4 Django Templates
* Send content to HTML template and the templates renders with content data
* syntax is a little bit different from python

## 9.5 DoesNotExist
* when pk matching query does not exist
    * should catch the error and render other template
* `try ~ except ... `: use `DoesNotExist`

## 9.6 Django vs React
* We are not going to use Template anymore
* Hard to make Dynamic website with Django Template
* Django is only for Backend, we use React and JS for Frontend
* Django is a good API server
* We will not use `render` in this course anymore
* We start to build REST API

# 10. Django REST Framework
## 10.0 Introduction
* Install Django REST Framework ([main site](https://www.django-rest-framework.org/))
    ```
    poetry add djangorestframework
    ```
* Why we use API?
    * we will give JSON instead of HTML
    * React JS will use the JSON data and show it to use beautifully
    * [Basics of REST API](https://www.youtube.com/watch?v=4DxHX95Lq2U)