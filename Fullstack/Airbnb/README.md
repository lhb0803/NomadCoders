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

## 10.1 JsonResponse
* HTTP Methods
    * `GET`: get data from server
    * `POST`: send data to server
    * `PUT`: update data to server
    * `DELETE`: delete data at server
* at real job, you don't make APIs for all methods above
    * you don't allow user to delete data
* at `views.py`, use `JsonResponse` to give client JSON data

## 10.2 api_view
* `serializers`: serialize QuerySet to JSON
* you need to choose which url and view function should be in Django REST Framework
    * **Use Decorator**: `@api_vew()`
    * Django REST framework provides a nice form to use

## 10.3 Serializer
* `Serializer`: Translate Django model to JSON
* inherit from `serializers.Serializer` and make own Serializer
* define which fields the model has: `name`, `kind`, ...
    * the fields defined in the class would be exposed
* very annoying to define all fields that model has -> will do defining automatically

## 10.4 POST Requests
* We need to tell Django REST Framework to allow `POST` method
    * at `@api_view()`, put list `["GET", "POST"]`
* When you get data from user, **You need to validate data**
    * serializers help translating data sent from user to our DB data

## 10.5 is_valid()
* `Serializer` automatically checks data from user, so we don't need to validate it ourselves
    * `is_valid()`: returns whether the data user sends is valid or not
    * field of which `read_only=True`: user doesn't have to specify the field

## 10.6 save()
* `save()`: `Serializer` automatically searches for create method
    * we need to handle creation
* `**` python operator: turns dictionary into `key=value` format

## 10.7 update()
* `PUT` request
* handling error: `rest_framework.exceptions.NotFound`
* `partial=True`: when you only changes partial field
* `save()`: at this time, **you don't call `create()`**
    * the serializer knows that user is trying to update the data because `instance` argument is provided
* dictionary's `get()` method: when you define `default` option (second parameter), `get`returns the `default` value when the key doesn't exist

## 10.8 delete()
* `rest_framework.status` has every status

## 10.9 Recap
* serializer **validates** data
* `POST`: `save()` calls `create()`
* `PUT`: `save()` calls `update()`

## 10.10 APIView
* code deletion begin!: much simpler code with Django REST Framework
* make class `Categories` which inherits APIView
    * define method `get()`, `method()`
* at `urlpatterns`, call methods by calling `Categories.as_view()`
* `get_object()`: Django Framework convention

## 10.11 ModelSerializer
* We will never make Serializer by ourselves!
* at `models.py`, we can infer Serializer
* `ModelSerializer`: automatically determines a set of serializer fields based on the model fields
    * has default `create()`, `update()` implementation
    * by below code, the serializer knows which model is to be serialized
        ```python
        class Meta:
            model = Category
        ```
    * two options to show fields: include or excldue
        1. include: `fields = "__all__"`
        2. exclude: `exclude = (...,)`

## 10.12 ModelViewSet
* Hide all codes for developers ([reference](https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions))
    * delete all previous codes
* make class `CategoryViewSet` which inherits from `ModelViewSet`
* `ModelViewSet` is smarter than our own code
* at `urlpatterns`, map http methods with class methods like below code
    ```python
    path("", views.CategoryViewSet.as_view(
        {
            "get": "list",
            "post": "create",
        }
    ))
    ```

## 10.13 Conclusions
* More simploe code: [Routers](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)
* `ReadOnlyModelViewSet()`: only `list` and `retrieve`
* `mixins`: create own viewset ([reference](https://www.django-rest-framework.org/api-guide/viewsets/#custom-viewset-base-classes))
* `ModelViewset` is great abstraction but makes code less explicit
    * not appropriate for customizing
        - ex1) only get photoes when the user is owner
        - ex2) send emails when deleting
* the instructor prefers `APIView` to `ModelViewset`

# 11. REST API
## 11.0 All Amenities
* id, created_at, updated_at is already read-only in ModelSerializer

## 11.1 Amenity Detail
* make `get_object()` to raise NotFound error

## 11.2 Perks and PerkDetail
* practice again

## 11.3 Rooms
* Authentication, Relationship
* when put object instead of ID (showing relationship with relationship)
    * `depth = 1` at ModelSerializer
    * But, most of time you don't need all data
    * Take care how much data you need
    * `depth = 1` is not customizable

## 11.4 Room Detail
* Customize relationship expansion
* How to tell Django our custom serializer
    * at Serializer, import other models' serializer
    * `owner = TinyUserSerializer()` at `RoomViewSerializer`
    * if array, use `many = True`

## 11.5 Create Room
* create model when there is a relationship
    * field that has relationship should be passed as dictionary
* `owner` should be shape of `TinyUserSerializer`
* but, **this data should not be passed through POST request data**
    * make `owner` read-only
* when you try to post and create room model with manual dictionary data, an error occurs
    ```
    The `.create()` method does not support writable nested fields by default.
    ```

## 11.6 Room Owner
* when you post your data, if the format meets serializer, the serializer.is_valid() is true
    * but because there's no exact data at DB, an error occurs
    * `serializer.save()` -> `.create()` occurs error
* You should write explicit create method
* or make `read_only = True` -> still makes error because some field like `owner` is mandatory when make a room model
* You should somehow find a way to **give serializer the information of `owner`**
* request object has many methods - you can check with `dir()`
* `owner = request.user` -> you should check if the requesting user is authenticated
* `serializer.save(owner=request.user)`
    * **`owner=requets.user` is added to `validated_data`**

## 11.7 Room Category
* pass category id and make the serializer find it and use it to create a room model
* search DB with category pk and pass the data to `serializer.save()`

## 11.8 Room Amenities
* how to handle list of pk (Many to Many field)
* `room.amenities.add()` (different API with foreign key)
* If only Amenities data is wrong, should the process terminated or just failing amenity adding silently: `except: pass`

## 11.9 Transactions
* No Amenity error -> delete room
    * bad logic: waste id
* create and delete is redundant
* Transaction: when code all succeed or all fail -> commit
    ```python
    from django.db import transaction

    with transaction.atomic():
        # for loop
    ```
* only add to db when the whole code runs without any problem

## 11.10 Delete Rooms
* if you are not owner of the room, you cannot delete

## 11.11 SerializerMethodField
* calculated fields
* rating
* make method `get_{property_name}`
    ```python
    potato = serializers.SerializerMethodField()
    def get_potato():
        pass
    ```

## 11.12 Serializer Context
* check the user owns the room or not
* can send context to serializer
    ```python
    serializer = RoomViewSerializer(
        room,
        context={"request": request},
    )
    ```

## 11.13 Reverse Serializers
* recall reverse accessor
    * A-FK(B) => B.A_set
* pagination: if you have many many reviews, you should optimize calling data 

## 11.14 Pagination
* reverse accessor is not good idea when calling many data
* Django includes pagination
    * _?page=1_
* set `page_size`
* QuerySet is lazy: calls data at last
* Homework: make amenities paginated

## 11.15 File Uploads
* at `config/settings.py`, write `MEDIA_ROOT = "uploads"` then the upload directory changes
    * `MEDIA_ROOT` specifies where the file actually exists in your server
    * `MEDIA_URL` specifies what url the media uses when a user trys to access upload directory
* proxy to use your own setting
    ```python 
    from django.conf import settings
    ```
* not very recommended: what you have done is letting your user to upload file next to your code

## 11.16 Upload Photo
* later, will put photo to other server
* Django will only get url of the file hosting server

## 11.17 permission_classes
* can we DELETE from /api/v1/medias/photos/1 ?
* from views in rooms? or in medias?
* make it more organized
* `permission_classes = [IsAuthenticated]` in `APIView`: can replace authentication
* `permission_classes = [IsAuthenticatedOrReadOnly]` in `APIView`: only authenticated users can PUT, POST or DELETE

## 11.18 Reviews
* POST design
    * POST /rooms/1/reviews vs POST /api/v1/reviews
    * the former is more appropriate because one can know which room you upload a photo to
* to make a request valid without `user`
    * make `user` read_only=True

## 11.19 Wishlists
* GET, POST, PUT
* `RoomListSerializer` 'request' KeyError
    * To handle this error, you should pass `context={"request": request}` to `WishlistSerializer()`

## 11.20 Wishlist
* user will send PUT to add room for your wishlist
    * `is_liked()`: toggle which adds or deletes room from your wishlist
* If you write code `object in objects.all()`, you are unnecessarily calling all objects just to check whether it exists or not
    * Just your `.filter().exists()` for efficiency

## 11.21 is_liked
* show user if the room is in wishlist or not
* `Wishlist.objects.filter(user=request.user, rooms__pk=room.pk)`:
    * finds all wishlists that is made by request.user and contains the room 

## 11.22 Bookings
* Design consideration
    * Do we need `get_object()` to call room's bookings?
    * maybe not -> Trust the client to send available room_pk
* filter with time
    * use `django.utils.timezone`
    * `.filter(check_in__gt=now)`

## 11.23 Create a Booking
* **a little logic**: check check_in, check_out to validate booking
* create another serializer
* customize `serializer.is_valid()`
    * create a method `validate_{field_name}(self, value)`

## 11.24 Validate Booking
* validate all fields together: `validate(self, data)`
* logic checking already booked
    * co >= a and ci <= b: already booked (from a to b)

## 11.25 Booking Completed
* create serializer can be different from showing serializer
    * CreateRoomBookingSerializer()
    * PublicBookingSerializer()

# 12. Users API
* GET PUT /me
* GET /users/username
* POST /users
* POST /users/log-in
* PUT /users/change-password

## 12.0 User Profile
* Me APIView

## 12.1 Create User
* `user.set_password(password)`: hash the password
* only admin user can access to Admin Panel

## 12.2 Change Password
* be careful of order when make url `path("<str:username>")`
* handle circluar import
* password is hashed by Django

## 12.3 Log In and Log Out
* `from django.contrib.auth import authenticate, login, logout`
* `authenticate`: authenticate user
* `login`: login
* `logout`: logout

# 13.0 Code Challenge
* experiences API
    * GET POST /experiences [x]
    * GET PUT DELETE /experiences/1 [x]
    * GET /experiences/1/perks [x]
    * GET POST /perks [x]
    * GET PUT DELETE /perks/1 [x]
    * GET POST /experiences/1/bookings [x]
    * GET PUT DELETE /experiences/1/bookings/2 [x]

# 14. GraphQL API
## 14.0 Introduction
* Strawberry library
* Most Django Framework uses REST API, so it is not mandatory to learn GraphQL API with Django

## 14.1 Query
* GraphQL quick explanation: [youtube link](https://www.youtube.com/watch?v=EkWI6Ru8lFQ)
* Install Strawberry extensions
* dummy graphql API without Django
* Python is available for typing -> **strawberry makes it mandatory**
* You should **add decorator `@strawberry.field` to make the method as a field**

## 14.2 Query Arguments
* `typing` library
* Learn how to ask for argument for query

## 14.3 Mutation
* `strarwberry.mutation`

## 14.4 Refactor
* Divde and conquer
* move class method, outside

## 14.5 Django Types
* `strawberry.auto` states data type automatically

## 14.6 Type Relationships
* in `RoomType`, declare `owner: "UserType"`
    * you should import `UserType` from `users.types`

## 14.7 Paginated Relationships
* you can create dynamic methods through strawberry

## 14.8 Custom Resolvers
* how to handel error in strawberry
    * we should choose message to show users
    * `typing.Optional[]`
* info parameter
    * `strawberry.types.Info`: contains request object

## 14.9 Permissions
* you should ask for request object explicitly to strawberry
* in `schema.py`, specify `permission_classes` in certain `strawberry.field()`

## 14.10 Code Challenge
* Mutation which allows user to create room
    * divide and conquer

# 15. Authentication
## 15.0 Introduction
* Create own custom authentication token
* Perform JWT authentication
* Django automatically uses cookie when authenticating users
* Install software [postman](https://www.postman.com/)
    * to simulate sending request from iOS or Android

## 15.1 Custom Authentication
* `REST_FRAMEWORK` in settings.py
* Your authentication instance is built before you call APIView instance
* Use postman to send GET request
    * at Headers: "Truest-me": "hyobae"
* at `BaseAuthentication` class, you should return tuple

## 15.2 Recap
* Behind the curtain of authentication
* You can customize authentication with inheriting `BaseAuthentication` class
    * How you can authenticate user
* in `settings.py` add the class you made to `DEFAULT_AUTHENTICATION_CLASSES`
    * Very weak at security, so it is never recommended to build your own authentication

## 15.3 Token Authentication
* install `rest_framework.authtoken` to `settings.py`
* Make an API to create token
    * `rest_framework.authtoken.views.obtain_auth_token`
* Token Authentication Rule
    ```
    Header
    {
        Key: "Authorization", Value: "Token {token_value}"
    }
    ```
* Explain how token authentication works by reading source code of `obtain_auth_token`
    * You can build your own token authentication (ex. KakaoTalk, Github login)

## 15.4 JWT Encode
* JWT(JSON Web Token) doesn't take space in database unlike Auth Token
* JWT has encoded information
* Auth Token has Key-Value relationship
* JWT has user information
    - you cannot force logout user
* install `PyJWT`
    ```
    poetry add pyjwt
    ```
* JWT can be decoded - security weakness

## 15.5 JWT Decode
* make class `JWTAuthentication` and use `jwt.decode()`

## 15.6 Environment Files
* you should Hide `SECRET_KEY` in source code for security!
* Create .env file and hide it from git (add to .gitignore file)
* Add django-envrionment
    ```
    poetry add django-environ
    ```
* add .env path with this script
    ```python
    from pathlib import Path
    import os
    import environ

    env = environ.Env()
    BASE_DIR = Path(__file__).resolve().parent.parent
    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

    SECRET_KEY = env("SECRET_KEY")
    ```
* Other third party apps for token authentication: 
    - Better Security: `django-rest-knox`
    - Simpler: `djangorestframework-simplejwt`

# 16. API Testing
## 16.0 Introduction
* So far: Browser Manual testing 
* we will use `python manage.py test` to use test codes

## 16.1 Our First Test
* `APITestCase`
    * method should start with prefix "`test_`"

## 16.2 Amenities Test
* GET request handler
* `APITestCase` has a lot of methods that are useful (starts with `assert`)
* Django test framework creates tes database and destroys it
    * method `setUp` can define database for testing

## 16.3 Create Amenity Test
* POST request handler

## 16.4 Amenity Detail Test
* GET single amenity test

## 16.5 Test Authentication
* `Rooms`' permission_classes are `[IsAuthenticatedOrReadOnly]`
    * So you can try Authentication Test
* To log-in you should create user in your test case

# 17. Front-End Setup
## 17.0 Introduction
* ReactJS, Chakra UI
* Chakra UI is awesome

## 17.1 Requirements
* Basics of ReachJS
    * jsx, state, props, component
    * How to fetch data in ReactJS
* Basics of Typescript
    * types, interfaces, generics

## 17.2 Setup
* Start!
    ```
    npx create-react-app airbnb-clone-frontend --template=typescript
    ```
* Chakra UI install [official page](https://chakra-ui.com/getting-started)
    ```
    npm i @chakra-ui/react @emotion/react @emotion/styled framer-motion
    ```
* reactouter-dom [official page](https://reactrouter.com/en/main)
    ```
    npm i react-router-dom
    ```
* start!
    ```
    npm run start
    ```
* Chakra UI has awsome various props
    ```typescript
    function App() {
    return <div>
        <Text color={"red.500"} fontSize={"6xl"}>It works!</Text>  
    </div>;
    }
    ```

## 17.3 Router Setup
* react-router-dom
* Explains react-router what our URL in browser shows
    * -> Choose What components to show to users
* all URL but room has their parent URL
* To use react component, you should write extension as .tsx (not .ts)
* `<Outlet />` renders child currently matching with URL

## 17.4 Not Found Page
* 404 page
* `createBrowserRouter` had good property called `errorElement` which shows up when page is not found
* first Chakra experience
* Chakra UI has Pre-defined styles
    * `<VStack>`, `<HStack>`, `<Heading>`, ...

## 17.5 Chakra Tour
* https://chakra-ui.com/docs/components
* Button: color, size, icon, ...
* Input: Login form, Addon, 
* Drawer
* Menu
* Modal
* Layout: Stack

# 18. Chakra UI
## 18.0 Header
* Use Icons [link](https://react-icons.github.io/react-icons/)
    ```
    npm install react-icons --save
    ```
* Use fontawesome icons
    ```typescript
    import { IconName } from "react-icons/fa";
    ```
* You can find default value in Chakra UI official page's [Default Theme](https://chakra-ui.com/docs/styled-system/theme)
    * You can get consistency
    * **rem**: Very nice for measurement unit for responsive design (1rem = 16px)
* `p`: shortcut for `padding`
    * `py`: vertical padding
    * `px`: horiontal padding

## 18.1 Login Modal
* You can specify state using `useDisclosure()`
* Chakra provides beautiful predefiend component suchas `Modal`, `ModalOverlay`, ...

## 18.2 Sign Up Modal
* Separate each component

## 18.3 Dark Mode
* create `theme.ts`
    ```typescript
    const config: ThemeConfig = {
        initialColorMode: "light",
        useSystemColorMode: true // use OS default theme
    }
    ```
* `useColorModeValue`: chakra Hook that allows user to use theme color
    * You don't have to write if-else statement

## 18.4 Rooms Grid
* You can use `Grid` Chakra component to decorate
* Need to be familiar with HTML and CSS grammar

## 18.5 Responsive Design
* Add a heart button on Image
* Responsive design
    * send object to `templateColumns`
    * `base` is for mobile
    * `lg` is for larger screen
* Separate Room Component

## 18.6 Skeletons
* https://chakra-ui.com/docs/components/skeleton
    * (Look Professional)
    ```typescript
    <Box>
        <Skeleton height={280} rounded={"xl"} mb={2}/>
        <SkeletonText noOfLines={3}/>
    </Box>
    ```
* Hover over state

# 19.0 React Query
* Connect Frontend with Backend
## 19.0 Manual Fetching
* CORS errors: your server don't allow fetching
    * handle with installing [django-cors-headers](https://pypi.org/project/django-cors-headers/)
        ```
        poetry add django-cors-headers
        ```
* Typescript grammar
    * When you fetch data, you should specity data type with `interface`

## 19.1 Recap
* Server should be **fetchable**

## 19.2 React Query
* TanStack Query (a.k.a React Query)
    * allow you to fetch in nice way
    * install
        ```
        npm i @tanstack/react-query
        ```
* React Query provides caching
    * Makes application faster

## 19.3 Axios
* recap React Query
    * The page is not refreshed because it is cached in data `["rooms"]` (in memory of browser)
* still fetch -> check whether the URL is right, response, json, ...
* Install axios
    ```
    npm i axios
    ```
* axios will fetch and get json from it by `get()`

## 19.4 Room Detail
* make Room component clickable and practice ReactQuery for fetching data
1. make Link
    * surround `<Vstack>` with `<Link>` (from `react-router` not `chakra-ui`)
2. make `RoomDetail` routes
    * `useQuery()` syntax
        ```typescript
        const { isLoading, data } = useQuery(["dataName"], fetchFunction);
        ```
        * it saves data in `"dataName"` with using `fetchFunction()`
3. make `getRoom()` function in `api.ts`

## 19.5 Devtools and Query Keys
* Install Devtools for tansatack/react-query
    * for debugging: you can figure out how the Query works and saves data
    * install
        ```
        npm i @tanstack/react-query-devtools
        ```
    * add `<ReactQueryDevtools />` at `Root.tsx` to use DevTools for all pages
* Learn How to send variables to Query Funciton

## 19.6 Photos Grid
* Building Room Detail UI
* `<Grid>` and `<GridItem>`

## 19.7 Reviews
* `<Avatar>` has many features
* `getRoomReviews` at `api.ts`

## 19.8 Conclusions
* `<Review>` Component
    * `<Container>`
* Build your own component

# 20. Authentication
## 20.0 useUser
1. create `getMe`
2. use `getMe` in `useQuery()` in `useUser.ts`
    * make sure `retry: false`
3. call useUser() from `Header.tsx`

## 20.1 Credentials
* recap of cookie authentication in Django
    1. Automatically, browser sends cookie(that has session_id) back to website
    2. Domain create cookie that browser saves
        * Browser is looking at Domain and sends cookie to that specific Domain
        * For ex, Google doesn't receive localhost domain's cookie, likewise localhost doesn't receive Google domain's cookie
* Javascript fetching doesn't automatically send cookie to website
    * which means, you have to manually send the cookie to  website
    * need to change our fetcher function (need to modify axios)
    * also, you need to change Django `settins.py` to make backend prepare for using Javascript fetching credentials
        ```python
        CORS_ALLOW_CREDENTIALS = True
        ```
    * **Should use Same Domain**
        ```python
        CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]
        ```