# Framework - Django

Django is a powerful Python web framework with a relatively shallow learning curve. You can easily build simple web applications in a short time. Django is also a robust and scalable framework that can be used to create large-scale web applications with complex requirements and integrations. 
We will cover how to create a simple blog application using Django to get a general idea of how the framework works, an understanding of how the different components interact with each other, and the skills to easily create Django projects with basic functionality.
The Blog application with Django that allows users to create, edit, and delete posts. The homepage will list all blog posts, and there will be a dedicated detail page for each individual post.

## Creating an isolated Python environment

1. Create an isolated environment with the following commands:

    ```shell
    mkdir mysite
    cd mysite
    python -m venv my_env
    ```

    > This will create a `my_env/` directory, including your Python environment. Any Python libraries you install while your virtual environment is active will go into the `my_env/lib/python3.8/site-packages` directory. Another advantage of using `venv` is that you won't need any administration privileges to install Python packages.

2. Run the following command to activate your virtual environment:

    ```shell
    source my_env/bin/activate
    ```

    The shell prompt will include the name of the active virtual environment enclosed in parentheses, as follows:

    ```shell
    (my_env)laptop:~ zenx$
    ```

    > You can deactivate your environment at any time with the deactivate command. You can find more information about venv at [`https://docs.python.org/3/library/venv.html`](https://docs.python.org/3/library/venv.html).

## Installing Django with pip

Django comes as a Python package and thus can be installed in any Python environment. The `pip` package management system is the preferred method for installing Django. Python 3.8+ comes with `pip` preinstalled, but you can find pip installation
instructions at [`https://pip.pypa.io/en/stable/installing/`](https://pip.pypa.io/en/stable/installing/).

1. Run the following command at the shell prompt to install Django with pip:

    ```shell
    pip install Django
    ```

    > This will install the **latest** version on Django the Python `site-packages/` directory of your virtual environment.
    > Django can be installed in several other ways. You can find a complete installation guide at [`https://docs.djangoproject.com/en/4.2/topics/install/`](https://docs.djangoproject.com/en/4.2/topics/install/).

## Creating a project

* Installing Django provides a command named `django-admin`.
* `django-admin` is a utility program that we can use to perform various operations related to Django.
* `django-admin` can be used to start a new Django project.

1. Run the following command from your shell:

    ```shell
    django-admin startproject mysite .
    ```

    This  will create a Django project with the name `mysite`. The `.` specifies where the project should be created - in this case the current working directory.

    > Avoid naming projects after built-in Python or Django modules in order to avoid conflicts.

    Let's take a look at the project structure generated:

        ├── mysite/
            ├── mysite/
            │   ├── __init__.py
            │   ├── settings.py
            │   ├── urls.py
            │   ├── wsgi.py
            ├── manage.py

    * `manage.py`: This is a command-line utility used to interact with your project. It is a thin wrapper around the django-admin.py tool. You don't need to edit this file.
    * `mysite/`: This is your project directory, which consists of the following files:
        * `__init__.py`: An empty file that tells Python to treat the mysite directory as a Python module.
        * `asgi.py`: This is the configuration to run your project as ASGI, the emerging Python standard for asynchronous web servers and applications.
        * `settings.py`: This indicates settings and configuration for your project and contains initial default settings.
        * `urls.py`: This is the place where your URL patterns live. Each URL defined here is mapped to a view.
        * `wsgi.py`: This is the configuration to run your project as a **Web Server Gateway Interface (WSGI)** application.

    **`manage.py`: Running a Django Shell**

    * Django comes with a custom Python shell interface where we can do all sorts of ad-hoc testing.
    * The Django shell allows you to write Python statements from the command line as though they're being executed from within the Django Web Framework.
    * The Django shell is an interactive command-line interface shell environment that combines the Django framework functionality with the regular python shell.

    In your terminal run the command:

    ```shell
    python manage.py shell
    ```

    It produces the following output:

    ![Django Shell](example_imgs/django-shell.jpg)

2. Django applications contain a models.py file where data models are defined. Each data model is mapped to a database table. To complete the project setup, you need to create the tables associated with the models of the applications listed in INSTALLED_APPS. Django includes a migration system that manages this. Open the shell and run the following commands:

    ```shell
    python manage.py migrate
    ```

    By applying migrations, the tables for the initial applications are created in the database.

## Running the development server

Django comes with a lightweight web server to run your code quickly, without needing to spend time configuring a production server. When you run the
Django development server, it keeps checking for changes in your code. It reloads automatically, freeing you from manually reloading it after code changes. However, it might not notice some actions, such as adding new files to your project, so you will have to restart the server manually in these cases.

1. Start the development server by typing the following command from your project's root folder:

    ```shell
    python manage.py runserver
    ```

    You should see something like this:

    ```shell
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    January 01, 2020 - 10:00:00
    Django version 3.0, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

    Now open [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) in your browser.:

    ![Development Server](example_imgs\dev-server.png)

    The preceding screenshot indicates that Django is running. If you take a look at your console, you will see the GET request performed by your browser:

    ```shell
    [01/Jan/2020 17:20:30] "GET / HTTP/1.1" 200 16351
    ```

    Each HTTP request is logged in the console by the development server. Any error that occurs while running the development server will also appear in the console.
    You can run the Django development server on a custom host and port, as follows:

    ```shell
    python manage.py runserver 127.0.0.1:8001
    ```

## Project settings

There are several settings that Django includes in this file, but these are only part of all the Django settings available. You can see all the settings and their default values at [`https://docs.djangoproject.com/en/4.2/ref/settings/`](https://docs.djangoproject.com/en/4.2/ref/settings/).

The following settings are worth looking at:

* `DEBUG` is a Boolean that turns the debug mode of the project on and off. If it is set to `True`, Django will display detailed error pages when an uncaught exception is thrown by your application. When you move to a production environment, remember that you have to set it to `False`. Never deploy a site into production with DEBUG turned on because you will expose sensitive
project-related data.
* `ALLOWED_HOSTS` is not applied while debug mode is on or when the tests are run. Once you move your site to production and set `DEBUG` to `False`, you will have to add your domain/host to this setting in order to allow it to serve your Django site.
* `INSTALLED_APPS` is a setting you will have to edit for all projects. This setting tells Django which applications are active for this site. By default, Django includes the following applications:
    * `django.contrib.admin`: An administration site
    * `django.contrib.auth`: An authentication framework
    * `django.contrib.contenttypes`: A framework for handling content types
    * `django.contrib.sessions`: A session framework
    * `django.contrib.messages`: A messaging framework
    * `django.contrib.staticfiles`: A framework for managing static files
* `MIDDLEWARE` is a list that contains middleware to be executed.
* `ROOT_URLCONF` indicates the Python module where the root URL patterns of your application are defined.
* `DATABASES` is a dictionary that contains the settings for all the databases to be used in the project. There must always be a default database. **The default configuration uses an SQLite3 database.**
* `LANGUAGE_CODE` defines the default language code for this Django site.
* `USE_TZ` tells Django to activate/deactivate timezone support. Django comes with support for timezone-aware datetime. This setting is set to True when you create a new project using the `startproject` management command.

## Projects and applications

In Django, a project is considered a Django installation with some settings. An application is a group of models, views, templates, and URLs. Applications interact with the framework to provide some specific functionalities and may be reused in various projects. You can think of a project as your website, which contains several applications, such as a blog, wiki, or forum, that can also be used by other projects.

![Projects vs Application](example_imgs/django-project-and-apps.svg)

## Creating an application

1. From the project's root directory, run the following command:

    ```shell
    python manage.py startapp blog
    ```

    This will create the basic structure of the application, which looks like this:

            └── blog/
                ├── __init__.py
                ├── admin.py
                ├── apps.py
                ├── migrations/
                │   └── __init__.py
                ├── models.py
                ├── tests.py
                └── views.py

    These files are as follows:
    * `admin.py`: This is where you register models to include them in the Django administration site—using this site is optional.
    * `apps.py`: This includes the main configuration of the blog application.
    * `migrations`: This directory will contain database migrations of your application. Migrations allow Django to track your model changes and synchronize the database accordingly.
    * `models.py`: This includes the data models of your application; all Django applications need to have a models.py file, but this file can be left empty.
    * `tests.py`: This is where you can add tests for your application.
    * `views.py`: The logic of your application goes here; each view receives an HTTP request, processes it, and returns a response.

## Activating the application

In order for Django to keep track of your application and be able to create database tables for its models, you have to activate it. To do this, edit the settings.py file and add `blog.apps.BlogConfig` to the `INSTALLED_APPS` setting. It should look like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
]
```

> The `BlogConfig` class is your application configuration. Now Django knows that your application is active for this project and will be able to load its models.

## Designing the data schema

A model is a Python class that subclasses `django.db.models.Model` in which each attribute represents a database field. Django will create a table for each model defined in the `models.py` file. When you create a model, Django will provide you with a practical API to query objects in the database easily.

1. Define a `Post` model. Add the following lines to the `models.py` file of the `blog` application:

    ```python
    from django.db import models
    from django.utils import timezone
    from django.contrib.auth.models import User


    class Post(models.Model):
        STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
        title = models.CharField(max_length=250)
        slug = models.SlugField(max_length=250, unique_for_date='publish')
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
        body = models.TextField()
        publish = models.DateTimeField(default=timezone.now)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
        
        class Meta:
            ordering = ('-publish',)

        def __str__(self):
            return self.title
    ```

    The fields are as follows:

    * `title`: This is the field for the post title. This field is `CharField`, which translates into a `VARCHAR` column in the SQL database.
    * `slug`: This is a field intended to be used in URLs. A slug is a short label that contains only letters, numbers, underscores, or hyphens. You will use the `slug` field to build beautiful, SEO-friendly URLs for your blog posts. You have added the `unique_for_date` parameter to this field so that you can build URLs for posts using their publish date and slug. Django will prevent multiple posts from having the same slug for a given date.
    * `author`: This field defines a many-to-one relationship, meaning that each post is written by a user, and a user can write any number of posts. For this field, Django will create a foreign key in the database using the primary key of the related model. In this case, you are relying on the User model of the Django authentication system. The `on_delete` parameter specifies the behavior to adopt when the referenced object is deleted. This is not specific to Django; it is an SQL standard. Using `CASCADE`, you specify that when the referenced user is deleted, the database will also delete all related blog posts. You can take a look at all the possible options at [`https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.on_delete`](https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.on_delete). You specify the name of the reverse relationship, from `User` to `Post`, with the `related_name` attribute. This will allow you to access related objects easily.
    * `body`: This is the body of the post. This field is a text field that translates into a `TEXT` column in the SQL database.
    * `publish`: This datetime indicates when the post was published. You use Django's timezone `now` method as the default value. This returns the current datetime in a timezone-aware format. You can think of it as a timezone-aware version of the standard Python `datetime.now` method.
    * `created`: This datetime indicates when the post was created. Since you are using `auto_now_add` here, the date will be saved automatically when creating an object.
    * `updated`: This datetime indicates the last time the post was updated. Since you are using `auto_now` here, the date will be updated automatically when saving an object.
    * `status`: This field shows the status of a post. You use a `choices` parameter, so the value of this field can only be set to one of the given choices.

    > You can find all field types at [`https://docs.djangoproject.com/en/4.2/ref/models/fields/`](https://docs.djangoproject.com/en/4.2/ref/models/fields/).

    The `Meta` class inside the model contains metadata. You tell Django to sort results by the `publish` field in descending order by default when you query the database. You specify the descending order using the negative prefix. By doing this, posts published recently will appear first.

    The `__str__()` method is the default human-readable representation of the object. Django will use it in many places, such as the administration site.

    You will need to create an initial migration for your Post model. In the root directory of your project, run the following command:

    ```shell
    python manage.py makemigrations blog
    ```

    You should get the following output:

    ```shell
    Migrations for 'blog':
        blog/migrations/0001_initial.py
            - Create model Post
    ```

    > Django creates a primary key automatically for each model, but you can also override this by specifying `primary_key=True` in one of your model fields. The default primary key is an id column, which consists of an integer that is incremented automatically. This column corresponds to the id field that is automatically added to your models.

    Let's sync your database with the new model. Run the following command to apply existing migrations:

    ```shell
    python manage.py migrate
    ```

    You will get an output that ends with the following line:

    ```shell
    Applying blog.0001_initial... OK
    ```

    You just applied migrations for the applications listed in INSTALLED_APPS, including your blog application. After applying the migrations, the database reflects the current status of your models. If you edit the `models.py` file in order to add, remove, or change the fields of existing models, or if you add new models, you will have to create a new migration using the `makemigrations` command. The migration will allow Django to keep track of model changes. Then, you will have to apply it with the `migrate` command to keep the database in sync with your models.

## Creating an admin site

Django comes with a built-in administration interface that is very useful for editing content. The Django site is built dynamically by reading your model metadata and providing a production-ready interface for editing content. You can use it out of the box, configuring how you want your models to be displayed in it.

The `django.contrib.admin` application is already included in the `INSTALLED_APPS` setting, so you don't need to add it.

1. Create a superuser

    You will need to create a user to manage the administration site. Run the following command:

    ```shell
    python manage.py createsuperuser
    ```

    You will see the following output; enter your desired username, email, and password, as follows:

    ```shell
    Username (leave blank to use 'admin'): admin

    Email address: admin@admin.com
    
    Password: ********
    
    Password (again): ********
    
    Superuser created successfully.
    ```

    Now start the development server with the `python manage.py runserver` command and open [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/) in your browser. You should see the administration login page:

    ![Django Admin Login](example_imgs/django-admin-login.png)

    Log in using the credentials of the user you created. You will see the administration site index page:

    ![Administration Site Index Page](example_imgs/admin-index.png)

    The `Group` and `User` models that you can see in the preceding screenshot are part of the Django authentication framework located in `django.contrib.auth`. If you click on **Users**, you will see the user you created previously.

2. Add models to Admin Site

    Let's add your blog models to the administration site. Edit the `admin.py` file of the `blog` application and make it look like this:

    ```python
    from django.contrib import admin
    from .models import Post


    @admin.register(Post)
    class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'slug', 'author', 'publish', 'status',)
        prepopulated_fields = {'slug': ('title',)}
    ```

    * The `list_display` attribute allows you to set the fields of your model that you want to display on the administration object list page. The `@admin.register()` function registers the ModelAdmin class that it decorates.
    You have told Django to prepopulate the slug field with the input of the `title` field using the `prepopulated_fields` attribute.

    Now reload the administration site in your browser. You should see your Post model on the site:

    ![Post Model added](example_imgs/admin-models-added.png)

    > When you register a model in the Django administration site, you get a user-friendly interface generated by introspecting your models that allows you to list, edit, create, and delete objects in a simple way.

    Click on the **Add** link beside Posts to add a new post. You will note the form that Django has generated dynamically for your model:

    ![Add Post Form](example_imgs/edit-post.png)

    Django uses different form widgets for each type of field. Even complex fields, such as the DateTimeField, are displayed with an easy interface, such as a JavaScript date picker. Fill in the form and click on the SAVE button. You should be redirected to the post list page with a success message and the post you just created:

    ![First Post](example_imgs/first-post.png)

## Creating model managers

There are two ways to add or customize managers for your models: you can add extra manager methods to an existing manager, or create a new manager by modifying the initial QuerySet that the manager returns. The first method provides you with a QuerySet API such as `Post.objects.my_manager()`, and the latter provides you with `Post.my_manager.all()`. The manager will allow you to retrieve posts using `Post.published.all()`.

1. Edit the models.py file of your blog application to add the custom manager:

    ```python
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super(PublishedManager, self).get_queryset().filter(status='published')


    class Post(models.Model):
        # ...
        objects = models.Manager() # The default manager.
        published = PublishedManager() # Our custom manager.
    ```

    The first manager declared in a model becomes the default manager. You can use the `Meta` attribute `default_manager_name` to specify a different default manager. If no manager is defined in the model, Django automatically creates the objects default manager for it. If you declare any managers for your model but you want to keep the objects manager as well, you have to add it explicitly to your model. In the preceding code, you add the default objects manager and the published custom manager to the Post model. The get_queryset() method of a manager returns the QuerySet that will be executed. You override this method to include your custom filter in the final QuerySet.

## Creating list and detail views

You are ready to build the views of the blog application. A Django view is just a Python function that receives a web request and returns a web response. All the logic to return the desired response goes inside the view.

First, you will create your application views, then you will define a URL pattern for each view, and finally, you will create HTML templates to render the data generated by the views. Each view will render a template, passing variables to it, and will
return an HTTP response with the rendered output.

1. Create list view

    Edit the `views.py` file of your `blog` application and make it look like this:

    ```python
    from django.shortcuts import render, get_object_or_404
    from .models import Post


    def post_list(request):
        posts = Post.published.all()
        return render(request, 'blog/post-list.html', {'posts': posts})
    ```

    You just created your first Django view. The `post_list` view takes the `request` object as the only parameter. **This parameter is required by all views.** In this view, you retrieve all the posts with the published status using the published manager that you created previously.

    Finally, you use the `render()` shortcut provided by Django to render the list of posts with the given template. **This function takes the request object, the template path, and the context variables to render the given template.** It returns an HttpResponse object with the rendered text (normally HTML code). The render() shortcut takes the request context into account, so any variable set by the template context processors is accessible by the given template. Template context processors are just callables that set variables into the context.

2. Create the Detail view

    Let's create a second view to display a single post. Add the following function to the `views.py` file:

    ```python
    def post_detail(request, year, month, day, post):
        post = get_object_or_404(Post, slug=post, status='published')
        return render(request, 'blog/post-detail.html', {'post': post})
    ```

    This is the post detail view. This view takes the `slug` and `status` arguments to retrieve a published post with the given `slug`. Note that when you created the Post model, you added the `unique_for_date` parameter to the slug field. This ensures that there will be only one post with a slug for a given date, and thus, you can retrieve single posts using the date and slug. In the detail view, you use the `get_object_or_404()` shortcut to retrieve the desired post. This function retrieves the object that matches the given parameters or an HTTP 404 (not found) exception if no object is found. Finally, you use the `render()` shortcut to render the retrieved post using a template.

## Adding URL patterns for your views

Adding URL patterns for your views URL patterns allow you to map URLs to views. A URL pattern is composed of a string pattern, a view, and, optionally, a name that allows you to name the URL project-wide. Django runs through each URL pattern and stops at the first one that matches the requested URL. Then, Django imports the view of the matching URL pattern and executes it, passing an instance of the HttpRequest class and the keyword or positional arguments.

* URL mapping means matching a specific URL with a specific view (function or class) in our code.
* We have a file views.py where we write our different views.
* The router connects the endpoints (the HTTP points of entry in our application) with the code that will return the HTML.
* Each connection between a particular endpoint and a view is a route (or a path).
* Django’s configuration of the URL dispatcher is called `URLconf` and takes the form of files where paths are defined.
* In Django, the file managing the routing, by default, is called `urls.py`. We can find such a file in our project’s settings directory.

1. Create a urls.py file in the directory of the blog application and add the following lines to it:

    ```python
    from django.urls import path
    from . import views

    app_name = 'blog'

    urlpatterns = [
        # post views
        path('', views.post_list, name='post-list'),
        path('<slug:post>/', views.post_detail, name='post-detail'),
    ]
    ```

    In the preceding code, you define an application namespace with the `app_name` variable. This allows you to organize URLs by application and use the name when referring to them. You define two different patterns using the `path()` function. The first URL pattern doesn't take any arguments and is mapped to the `post_list` view. The second pattern takes the following 1 argument and is mapped to the `post_detail` view:

    > You use angle brackets to capture the values from the URL. Any value specified in the URL pattern as `<parameter>` is captured as a string. You use path converters, such as `<int:id>`, to specifically match and return an integer and `<slug:post>` to specifically match a slug. You can see all path converters provided by Django at [`https://docs.djangoproject.com/en/4.2/topics/http/urls/#pathconverters`](https://docs.djangoproject.com/en/4.2/topics/http/urls/#pathconverters).

    If using path() and converters isn't sufficient for you, you can use re_path() instead to define complex URL patterns with Python regular expressions. You can learn more about defining URL patterns with regular expressions at [`https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path`](https://docs.djangoproject.com/en/4.2/ref/urls/#django.urls.re_path). If you haven't worked with regular expressions before, you might want to take a look at the Regular Expression HOWTO located at [`https://docs.python.org/3/howto/regex.html`](https://docs.python.org/3/howto/regex.html) first.

    > **Creating a `urls.py` file for each application is the best way to make your applications reusable by other projects.**

2. Including the application URLs

    Next, you have to include the URL patterns of the `blog` application in the main URL patterns of the project.
    Edit the `urls.py` file located in the `mysite` directory of your project and make it look like the following:

    ```python
    from django.urls import path, include
    from django.contrib import admin


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls', namespace='blog')),
    ]
    ```

    The new URL pattern defined with `include` refers to the URL patterns defined in the `blog` application so that they are included under the `blog/` path. You include these patterns under the namespace `blog`. **Namespaces have to be unique across your entire project.** Later, you will refer to your blog URLs easily by using the namespace followed by a colon and the URL name, for example, `blog:post_list` and `blog:post_detail`. You can learn more about URL namespaces at [`https://docs.djangoproject.com/en/4.2/topics/http/urls/#url-namespaces`](https://docs.djangoproject.com/en/4.2/topics/http/urls/#url-namespaces).

## Creating Canonical URLs for models

A canonical URL is the preferred URL for a resource. You may have different pages in your site where you display posts, but there is a single URL that you use as the main URL for a blog post. The convention in Django is to add a `get_absolute_url()` method to the model that returns the canonical URL for the object.

You can use the post_detail URL that you have defined in the preceding section to build the canonical URL for Post objects. For this method, you will use the `reverse()` method, which allows you to build URLs by their name and pass optional parameters. You can learn more about the URLs utility functions at [`https://docs.djangoproject.com/en/4.2/ref/urlresolvers/`](https://docs.djangoproject.com/en/4.2/ref/urlresolvers/).

Edit the `models.py` file of the `blog` application and add the following code:

```python
from django.urls import reverse


class Post(models.Model):

# ...

def get_absolute_url(self):
    return reverse('blog:post_detail', args=[self.slug])
```

You will use the `get_absolute_url()` method in your templates to link to specific posts.

## Creating templates for your views

You have created views and URL patterns for the `blog` application. URL patterns map URLs to views, and views decide which data gets returned to the user. Templates define how the data is displayed; they are usually written in HTML in combination with the Django template language. You can find more information about the Django template language at [`https://docs.djangoproject.com/en/4.2/ref/templates/language/`](https://docs.djangoproject.com/en/4.2/ref/templates/language/).

Let's add templates to your application to display posts in a user-friendly manner.

1. Configure the templates settings first.

    Open the project's settings.py file and just below `BASE_DIR` add the route to the template directory as follows.

    ```python
    import os 

    # ....
    TEMPLATES_DIRS = os.path.join(BASE_DIR,'templates')
    ```

    In settings.py scroll to the, `TEMPLATES` which should look like this:

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    ```

    Now add the newly created `TEMPLATES_DIRS`  in the `DIRS`:

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            #  Add  'TEMPLATE_DIRS' here
            'DIRS': [TEMPLATE_DIRS],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    ```

2. Create the following directories and files inside in root directory of your project:

        ├── templates/
            └── blog/
                ├── index.html
                ├── post-detail.html

    Django has a powerful template language that allows you to specify how data is displayed. It is based on template tags, template variables, and template filters:

    * Template tags control the rendering of the template and look like `{% tag %}`
    * Template variables get replaced with values when the template is rendered and look like `{{ variable }}`
    * Template filters allow you to modify variables for display and look like `{{ variable|filter }}`.

    > You can see all built-in template tags and filters at [`https://docs.djangoproject.com/en/4.2/ref/templates/builtins/`](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/).

    1. Add the following code to `index.html`:

        ```html
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home</title>
        <body>
            <header>
                <h4>PythonBugs Blog</h4>
                <hr>
            </header>
            <main>
            <h1>{{ welcome_text|lower }}</h1>
            <h3>This is a list of our posts</h3>
            <ul>
                {% for post in all_posts %}
                    <li>
                        <a href="{{ post.get_absolute_url }}">{{post.title}} - {{post.author}}</a>
                        <p>{{post.body}}</p>
                    </li>
                {% endfor %}
            </ul>
        </main>
        <footer>
            <hr>
            <p>Copyright 2023</p>
            
        </footer>
        </body>
        </html>
        ```

        * `{{ welcome_text|lower }}` returns the variable that was sent as context from the view, the `lower` filter is applied on it to make all the text lowercase.
        * `all_posts` is a list of posts that was returned from the template so in order to display all posts individually we have to iterate(loop) over the list and deisplay each one individually. Hence, `{% for post in all_posts %}` and `{% endfor %}` With most(not all) django template tags (just like html tags) you have to have an opening and closing tag.
        * Dot notation is used to access desired fields of the `Post` model `{{post.title}}`, `{{post.author}}` and `{{post.body}}`.
        * We can access the `get_absolute_url` method we created for the post model in order to generate a link to each post `{{ post.get_absolute_url }}`.

        Open the shell and execute the `python manage.py runserver` command to start the development server. Open [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) in your browser; you will see everything running:

        ![Homepage](example_imgs/initial-landing-page.png)

    2. Add the following code to `post-list.html`:

        ```html
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title></title>
            
        </head>
        <body>
            <header>
                <h4>PythonBugs Blog</h4>
                <hr>
            </header>
            <main>
            <h4>{{ post.title }}</h4>
            <p>{{ post.body }}</p>
            <p> - {{ post.author }}</p>
        </main>
        <footer>
            <hr>
            <p>Copyright 2023</p>
            
        </footer>
        </body>
        </html>
        ```

        * We still use dot notation to access specific fields of the post. There is no need to iterate in this case as we are returning a single post from the view.

        Open the shell and execute the `python manage.py runserver` command to start the development server. Open [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) in your browser; from the homepage click on any link you will see everything running as follows:

        ![Post Page](example_imgs/initial-post-page.png)

    **Template inheritance/extension**

    * The most powerful – and thus the most complex – part of Django’s template engine is template inheritance. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.

    Let’s look at template inheritance by adding a `base.html` file at the root of the `templates` directory:

        ├── templates/
            ├── base.html
            └── blog/
                ├── index.html
                ├── post-detail.html

    The preceding structure will be the file structure for your templates. The `base.html` file will include the main HTML structure of the website and divide the content into the main content area. The `index.html` and `post-detail.html` files will inherit from the `base.html` file to render the blog post list and detail views, respectively.

    1. Edit the `base.html` file and add the following code:

        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            <div id="content">
                {% block content %}
                {% endblock %}
            </div>
        </body>
        </html>
        ```

        There are two `{% block %}` tags. These tell Django that you want to define a block in that area. Templates that inherit from this template can fill in the blocks with content. You have defined a block called title and a block called content.
        > All the block tag does is to tell the template engine that a child template may override those portions of the template.

    2. Let's edit the `index.html` file and make it look like the following:

        ```html
        {% extends "base.html" %}

        {% block title %}My Blog{% endblock %}

        {% block content %}
            <h1>My Blog</h1>
            {% for post in posts %}
                <h2>
                    <a href="{{ post.get_absolute_url }}">
                        {{ post.title }}
                    </a>
                </h2>
                <p>
                    Published {{ post.publish }} by {{ post.author }}
                </p>
                {{ post.body|truncatewords:30|linebreaks }}
            {% endfor %}
        {% endblock %}
        ```

    3. Let's edit the `post-detail.html` file and make it look like the following:

        ```html
        {% extends 'base.html' %}
        {% load static %}

        {% block title%} {{ post.title }} {% endblock%}

        {% block content%}
            <h4>{{ post.title }}</h4>
            <p>{{ post.body }}</p>
            <p> - {{ post.author }}</p>
        {% endblock %}
        ```

        > With the {% extends %} template tag, you tell Django to inherit from the `blog/base.html` template. Then, you fill the title and content blocks of the base template with content. You iterate through the posts and display their title, date, author, and body, including a link in the title to the canonical URL of the post. In the body of the post, you apply two template filters: `truncatewords` truncates the value to the number of words specified, and `linebreaks` converts the output into HTML line breaks. You can concatenate as many template filters as you wish; each one will be applied to the output generated by the preceding one.

    Open the shell and execute the `python manage.py runserver` command to start the development server. Open [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) in your browser; you will see everything running. Note that you need to have some posts with the `Published` status to show them here.

    You should see still see the normal homepage:

    ![Homepage](example_imgs/initial-landing-page.png)

### Referencing static files in templates

Your project is likely to use static resources, including JavaScript, CSS, and images. Because the location of these files might not be known (or might change), Django allows you to specify the location in your templates relative to the `STATIC_URL` global setting.

1. Configuring static files

    * Make sure that `django.contrib.staticfiles` is included in your `INSTALLED_APPS`.

    * In your settings file, define `STATIC_URL`, for example:

        ```python
        STATIC_URL = 'static/'
        ```

2. Create a directory called `static` at the root of your project and copy the [`css`](resources/css/), [`js`](resources/js/) and [`images`](resources/images/) folders from [resources](resources):

        ├── static/
                ├── css/
                └── images/
                └── js/

    > We will use the these files for the development of our blog to make look a bit nicer.

3. Add the CSS and JS files to the `base.html` template:

    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- ADD  CSS STATIC FILES -->
        <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
        <title>{% block title %}  {% endblock %}</title>
    </head>
    <body>
        <header>
            <h4>PythonBugs Blog</h4>
            <hr>
        </header>
        <main>
            {% block content %}
            <!-- Content goes here -->
            {% endblock %}
        </main>
        <footer>
            <hr>
            <p>
                Copyright &copy;
                <script>document.write(new Date().getFullYear());</script>
                PythonBugs
            </p>
            
        </footer>
        <!-- ADD  CSS STATIC FILES -->
        <script src="{% static 'js/jquery-3.4.1.min.js' %}"></script>
        <script src="{% static 'js/popper.min.js' %}"></script>
        <script src="{% static 'js/bootstrap.min.js' %}"></script>
        <script src="{% static 'js/custom.js' %}"></script>
    </body>
    </html>
    ```

    This will add CSS and JavaScript globally to our templates meaning it have to be repeated for each page. Unless there is a static file that is specific to a template.

    * We also add some JavaScript to get the current year in the footer:

        ```html
        <script>document.write(new Date().getFullYear());</script>
        ```

    `{% load static %}` tells Django to load the static template tags that are provided by the `django.contrib.staticfiles` application, which is contained in the `INSTALLED_APPS` setting. After loading them, you are able to use the `{% static %}` template tag throughout this template. With this template tag, you can include the static files, such as the blog.css file

    > We will now be able to style our templates using the CSS and JavaScript with just added

4. Styling the header

    Update the `<header>`  tag of the `base.html` template to look as follows:

    ```html
    <header>
        <div class="container">
            <nav class="site-nav">
              <div class="row justify-content-between align-items-center">
                <div class="d-none d-lg-block col-lg-3 top-menu">
                </div>
                <div class="col-3 d-lg-block col-md-6 col-lg-6 text-lg-center logo">
                  <a href="">Python<span class="text-primary">Bugs</span></a>
                </div>
                <div class="col-9 col-md-6 col-lg-3 text-right top-menu">      
                </div>
              </div>
              <div class="d-none d-lg-block row align-items-center py-3">
                <div class="col-12 col-sm-12 col-lg-12 site-navigation text-center">
                  <ul class="js-clone-nav d-none d-lg-inline-block text-left site-menu">
                    <li><a href="{% url 'blog:home' %}">Home</a></li>
                    <li><a href="#">Contact</a></li>
                  </ul>
                </div>
      
              </div>  
            </nav> <!-- END nav -->
          </div> <!-- END container -->
    </header>
    ```

5. Styling the footer

    Update the `<footer>`  tag of the `base.html` template to look as follows:

    ```html
    <footer class="site-footer">
        <div class="container">
            <div class="row justify-content-center copyright">
                <div class="col-lg-7 text-center">      
                    <div class="widget">
                        <p>
                            Copyright &copy;
                            <script>document.write(new Date().getFullYear());</script>
                            PythonBugs 
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    ```

    Open [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) in your browser; The header and footer should now be styled.

    ![Styled Header and Footer](example_imgs/styled-base.png)

6. Styling the Homepage:

    Update the `index.html` template to look as follows:

    ```html
    {% extends 'blog/base.html' %}
    {% load static %}

    {% block title %} Home {% endblock %}

    {% block content %}
        <div class="section-latest">
            <div class="container">
                <h1>{{ welcome_text|title }}</h1>

                <div class="row gutter-v1 align-items-stretch mb-5">
                    <div class="col-12">
                        <h2 class="section-title">Latest Posts</h2>
                    </div>
                    {% for post in all_posts %}
                        <div class="col-md-9 pr-md-5">
                            <div class="row">
                                <div class="col-12">
                                    <div class="post-entry horizontal d-md-flex">
                                        <div class="media">
                                            <img src="{% static 'images/img_h_3.jpg' %}" alt="Image" class="img-fluid">
                                        </div>
                                        <div class="text">
                                            <div class="meta">
                                                <span>{{post.created}}</span>
                                                <span>&bullet;</span>
                                                <span>{{post.author}}</span>
                                            </div>
                                            <h2>
                                                <a href="{{ post.get_absolute_url }}">
                                                    {{post.title}}
                                                </a>
                                            </h2>
                                            <p>{{ post.body|truncatewords:30|linebreaks }}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                </div>    
            </div>
        </div>
    {% endblock %}
    ```

    Open [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) in your browser; The header and footer should now be styled.

    ![Styled Homepage](example_imgs/styled-homepage.png)

7. Styling the Post Detail page:

    Update the `post-detail.html` template to look as follows:

    ```html
    {% extends 'blog/base.html' %}
    {% load static %}

    {% block title%} {{ post.title }} {% endblock%}

    {% block content%}
        <div class="site-hero py-5 bg-light mb-5">
            <div class="container">
                <div class="row align-items-center justify-content-between">
                    <div class="col-lg-12 text-center">
                        <h1 class="text-black mb-0">{{ post.title }}</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="container article">
            <div class="row justify-content-center align-items-stretch"> 
                <article class="col-lg-8 order-lg-2 px-lg-5">
                    <p>{{ post.body|linebreaks }}</p>
                    <div class="post-single-navigation d-flex align-items-stretch">
                        <a href="#" class="mr-auto w-50 pr-4">
                            <span class="d-block">{{ post.created }}</span>
                            By: {{ post.author|title }}
                        </a>
                    </div> 
                </article>
            </div>
        </div>
    {% endblock %}
    ```

    Open [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) in your browser; Click on one of the posts and you should see:

    ![Styled Homepage](example_imgs/styled-details-page.png)

### Forms

An HTML Form is a group of one or more fields/widgets on a web page, which can be used to collect information from users for submission to a server. Forms are a flexible mechanism for collecting user input because there are suitable widgets for entering many different types of data, including text boxes, checkboxes, radio buttons, date pickers and so on. Forms are also a relatively secure way of sharing data with the server, as they allow us to send data in POST requests with cross-site request forgery protection.

Django has a built-in forms framework that allows you to create forms in an easy manner. The forms framework makes it simple to define the fields of your form, specify how they have to be displayed, and indicate how they have to validate input data. The Django forms framework offers a flexible way to render forms and handle data.
Django comes with two base classes to build forms:

* `Form`: Allows you to build standard forms
* `ModelForm`: Allows you to build forms tied to model instances

**Creating a comment system**

You will build a comment system wherein users will be able to comment on posts. To build the comment system, you need to do the following:

* Create a model to save comments
* Create a form to submit comments and validate the input data
* Add a view that processes the form and saves a new comment to the database
* Edit the post detail template to display the list of comments and the form to add a new comment

1. Let's build a model to store comments. Open the `models.py` file of your `blog` application and add the following code:

    ```python
    class Comment(models.Model):
        post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
        name = models.CharField(max_length=80)
        email = models.EmailField()
        body = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        active = models.BooleanField(default=True)

        class Meta:
            ordering = ('created',)

        def __str__(self):
            return f'Comment by {self.name} on {self.post}'
    ```

    This is the `Comment` model. It contains a `ForeignKey` to associate a comment with a single post. This many-to-one relationship is defined in the `Comment` model because each comment will be made on one post, and each post may have multiple comments. The `related_name` attribute allows you to name the attribute that you use for the relationship from the related object back to this one. After defining this, you can retrieve the post of a comment object using `comment.post` and retrieve all comments of a post using `post.comments.all()`. If you don't define the `related_name` attribute, Django will use the name of the model in lowercase, followed by `_set` (that is, `comment_set`) to name the relationship of the related object to the object of the model, where this relationship has been defined.

    You have included an `active` Boolean field that you will use to manually deactivate inappropriate comments. You use the `created` field to sort comments in a chronological order by default.

    > You can learn more about many-to-one relationships at [`https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/`](https://docs.djangoproject.com/en/4.2/topics/db/examples/many_to_one/).

    The new `Comment` model that you just created is not yet synchronized into the database. Run the following command to generate a new migration that reflects the creation of the new model:

    ```shell
    python manage.py makemigrations blog
    ```

    You should see the following output:

    ```shell
        Migrations for 'blog':
            blog/migrations/0002_comment.py
                - Create model Comment
    ```


    Django has generated a `0002_comment.py` file inside the `migrations/` directory of the `blog` application. Now, you need to create the related database schema and apply the changes to the database. Run the following command to apply existing migrations:

    ```shell
    python manage.py migrate
    ```

    You will get an output that includes the following line:

    ```shell
    Applying blog.0002_comment... OK
    ```

    The migration that you just created has been applied; now a `blog_comment` table exists in the database.

    Open the `admin.py` file of the `blog` application, import the `Comment` model, and add the following `ModelAdmin` class:

    ```python
    from .models import Post, Comment


    @admin.register(Comment)
    class CommentAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'post', 'created', 'active')
        list_filter = ('active', 'created', 'updated')
        search_fields = ('name', 'email', 'body')
    ```

2. Create a `forms.py` file inside the directory of your `blog` application and make it look like this:

    You will need to use the `ModelForm` class because you have to build a form dynamically from your `Comment` model.

    ```python
    from django import forms
    from .models import Comment


    class CommentForm(forms.ModelForm):
        
        class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
    ```

    To create a form from a model, you just need to indicate which model to use to build the form in the `Meta` class of the form. Django introspects the model and builds the form dynamically for you.

    Each model field type has a corresponding default form field type. The way that you define your model fields is taken into account for form validation. By default, Django builds a form field for each field contained in the model. However, you can explicitly tell the framework which fields you want to include in your form using a fields `list`, or define which fields you want to exclude using an exclude list of fields. For your `CommentForm` form, you will just use the `name`, `email`, and `body` fields, because those are the only fields that your users will be able to fill in.

3. Add a view that processes the form and saves a new comment to the database:

    You will use the post detail view to instantiate the form and process it, in order to keep it simple. Edit the `views.py` file, add imports for the `Comment` model and the `CommentForm` form, and modify the `post_detail` view to make it look like the following:

    ```python
    from .models import Post, Comment
    from .forms import CommentForm


    def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post-detail.html', {'post': post,'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
    ```

    You used the `post_detail` view to display the post and its comments. You added a QuerySet to retrieve all active comments for this post, as follows:

    ```python
    comments = post.comments.filter(active=True)
    ```

    You build this QuerySet, starting from the post object. Instead of building a QuerySet for the `Comment` model directly, you leverage the `post` object to retrieve the related `Comment` objects. You use the manager for the related objects that you defined as `comments` using the `related_name` attribute of the relationship in the `Comment` model. You use the same view to let your users add a new comment. You initialize the `new_comment` variable by setting it to `None`. You will use this variable when a new comment is created.

    You build a form instance with `comment_form = CommentForm()` if the view is called by a `GET` request. If the request is done via `POST`, you instantiate the form using the submitted data and validate it using the `is_valid()` method. If the form is invalid, you render the template with the validation errors. If the form is valid, you take the following actions:

    1. You create a new `Comment` object by calling the form's `save()` method and assign it to the `new_comment` variable, as follows:

        ```python
        new_comment = comment_form.save(commit=False)
        ```

        The `save()` method creates an instance of the model that the form is linked to and saves it to the database. If you call it using `commit=False`, you create the model instance, but don't save it to the database yet. This comes in handy when you want to modify the object before finally saving it, which is what you will do next.

        > The `save()` method is available for `ModelForm` but not for `Form` instances, since they are not linked to any model.

    2. You assign the current post to the comment you just created:

        ```python
        new_comment.post = post
        ```

        By doing this, you specify that the new comment belongs to this post.

    3. Finally, you save the new comment to the database by calling its `save()` method:

        ```python
        new_comment.save()
        ```

    Your view is now ready to display and process new comment

4. Edit the post detail template to display the list of comments and the form to add a new comment

    You have created the functionality to manage comments for a post. Now you need to adapt your `post-detail.html` template to do the following things:

    * Display the total number of comments for a post
    * Display the list of comments
    * Display a form for users to add a new comment

    1. add the total comments. Open the `post-detail.html` template and append the following code to the content block:

        ```html
        <div class="pt-5">
            {% with comments.count as total_comments %}
                <h3 class="mb-5">{{ total_comments }} Comment{{ total_comments|pluralize }}</h3>
            {% endwith %}
        </div>
        ```

        You are using the Django ORM in the template, executing the QuerySet `comments.count()`. Note that the Django template language doesn't use parentheses for calling methods. The `{% with %}` tag allows you to assign a value to a new variable that will be available to be used until the `{% endwith %}` tag.

        > The `{% with %}` template tag is useful for avoiding hitting the database or accessing expensive methods multiple times.

        You use the `pluralize` template filter to display a plural suffix for the word "comment," depending on the `total_comments` value. Template filters take the value of the variable they are applied to as their input and return a computed value. The `pluralize` template filter returns a string with the letter "s" if the value is different from 1. The preceding text will be rendered as *0 comments*, *1 comment*, or *N comments*.

    2. Let's include the list of comments. Append the following lines to the `post-detail.html` template below the preceding code:

        ```html
        <ul class="comment-list">
            {% for comment in comments %}
                <li class="comment">
                    <div class="vcard bio">
                        <img src="{% static 'images/img_h_3.jpg' %}" alt="Image placeholder">
                    </div>
                    <div class="comment-body">
                        <h3>{{ comment.name }}</h3>
                        <div class="meta">{ comment.created }}</div>
                        <p>{{ comment.body|linebreaks }}</p>
                    </div>
                </li>
            {% empty %}
                <p>There are no comments yet.</p>
            {% endfor %}
        </ul>
        <!-- END comment-list -->
        ```

        You use the `{% for %}` template tag to loop through comments. You display a default message if the `comments` list is empty, informing your users that there are no comments on this post yet. Then, you display the name of the user who posted the comment, the date, and the body of the comment.

    3. Render the form or display a success message instead when it is successfully submitted. Add the following lines just below the preceding code:

        ```html
        {% if new_comment %}
            <h2> Your comment has been added!</h2>
        {% else %}
        <div class="comment-form-wrap pt-5">
            <h3 class="mb-5">Leave a comment</h3>
            <form method='post'>
                {% csrf_token %}
                {{ comment_form.as_p }}
                <p>
                    <input type="submit" value="Post Comment" class="btn btn-primary btn-md">
                </p>
            </form>
        </div>
        {% endif %}
        ```

        The code is pretty straightforward: if the `new_comment` object exists, you display a success message because the comment was successfully created. Otherwise, you render the form with a paragraph, `<p>`, element for each field and include the CSRF token required for `POST` requests.

        This is the template to display the form or a success message when it's sent. As you will notice, you create the HTML form element, indicating that it has to be submitted by the POST method:

        ```html
        <form method="post">
        ```

        The `{% csrf_token %}` template tag introduces a hidden field with an autogenerated token to avoid **cross-site request forgery (CSRF)** attacks. These attacks consist of a malicious website or program performing an unwanted action for a user on your site. You can find more information about this at ['https://owasp.org/www-community/attacks/csrf'](https://owasp.org/www-community/attacks/csrf).

        The preceding tag generates a hidden field that looks like this:

        ```html
        <input type='hidden' name='csrfmiddlewaretoken' value='26JjKo2lcEtYkGoV9z4XmJIEHLXN5LDR' />
        ```

        > By default, Django checks for the CSRF token in all `POST` requests.Remember to include the `csrf_token` tag in all forms that are submitted via `POST`.

    Open http://127.0.0.1:8000/blog/ in your browser and click on a post title to take a look at its detail page. You will see something like the following screenshot:

    ![Comment Section](example_imgs/comment-section.png)

### Authentication

Django comes with a built-in authentication framework that can handle user authentication, sessions, permissions, and user groups. The authentication system includes views for common user actions such as log in, log out, password change, and password reset.
The authentication framework is located at `django.contrib.auth` and is
used by other Django `contrib` packages.
When you create a new Django project using the `startproject` command, the authentication framework is included in the default settings of your project. It consists of the `django.contrib.auth` application and the following two middleware classes found in the `MIDDLEWARE` setting of your project:

* `AuthenticationMiddleware`: Associates users with requests using sessions
* `SessionMiddleware`: Handles the current session across requests

Middleware are classes with methods that are globally executed during the request or response phase.

The authentication framework also includes the following models:

* `User`: A user model with basic fields; the main fields of this model are `username`, `password`, `email`, `first_name`, `last_name`, and `is_active`
* `Group`: A group model to categorize users
* `Permission`: Flags for users or groups to perform certain actions

The framework also includes default authentication views and forms

1. Create an app for authentication

    Use the following commands create a new application named `account`:

    ```shell
    django-admin startapp account
    ```

    Add the new application to your project by adding the application's name to the `INSTALLED_APPS` setting in the `settings.py` file. Place it in the `INSTALLED_APPS` list before any of the other installed apps:

    ```python
    INSTALLED_APPS = [
        'account.apps.AccountConfig',
        # ...
    ]
    ```

    Django authentication templates will be defined later on. By placing your application first in the `INSTALLED_APPS` setting, you ensure that your authentication templates will be used by default instead of any other authentication templates contained in other applications. Django looks for templates by order of application appearance in the `INSTALLED_APPS` setting.

    Run the next commands to sync the database with the models of the default applications included in the `INSTALLED_APPS` setting:

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Configuring Authentication settings

    Edit the `settings.py` file of your project and add the following code to it:

    ```python
    LOGIN_REDIRECT_URL = 'blog:home'
    LOGIN_URL = 'account:login'
    LOGOUT_URL = 'account:logout'
    ```

    * `LOGIN_REDIRECT_URL`: Tells Django which URL to redirect the user to after a successful login if no next parameter is present in the request
    * `LOGIN_URL`: The URL to redirect the user to log in (for example, views using the login_required decorator)
    * `LOGOUT_URL`: The URL to redirect the user to log out

3. Create authentication URLs

    Django also provides the authentication URL patterns via `django.contrib.auth.urls`. Create a new `urls.py` file in your account application directory and add the following code to it:

    ```python
    from django.urls import path, include

    app_name = "account"

    urlpatterns = [
        path('', include('django.contrib.auth.urls')),
    ]
    ```

    Edit the main urls.py file located in your bookmarks project directory, import include, and add the URL patterns of the account application, as follows:

    ```python
    from django.urls import path, include
    from django.contrib import admin

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('account/', include('account.urls', namespace="account")),
    ]
    ```

    > You can see the authentication URL patterns included at [`https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/urls.py`](https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/urls.py).

4. Create authentication templates

    Create a new directory inside the templates directory and name it `registration`. This is the default path where the Django authentication views expect your authentication templates to be.
    The `django.contrib.admin` module includes some of the authentication templates that are used for the administration site. You have placed the account application at the top of the `INSTALLED_APPS` setting so that Django uses your templates by default instead of any authentication templates defined in other applications. Create a new file inside the templates/registration directory, name it `login.html`, and add the following code to it:

    ```html
    {% extends "base.html" %}

    {% block title %}Login{% endblock %}

    {% block content %}
        <div class="site-hero py-5 bg-light mb-0">
            <div class="container">
                <div class="row align-items-center justify-content-between">
                    <div class="col-lg-12 text-center">
                        <h1 class="text-black mb-0">Login</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="section-grey bg-light">
            <div class="container">
                <div class="block">
                    <div class="row justify-content-center">
                        <div class="col-md-8 col-lg-8 pb-4 text-center">
                            <form method="post">
                                {% csrf_token %}
                                {{ form.as_p }}     
                                <input type="submit" class="btn btn-primary-hover-outline" value="Login">
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    {% endblock %}
    ```

    * Django uses the `AuthenticationForm` form located at `django.contrib.auth.forms` by default. This form tries to authenticate the user and raises a validation error if the login was unsuccessful. In this case, you can look for errors using `{% if form.errors %}` in the template to check whether the credentials provided are wrong.

    Create a `logged_out.html` template inside the `registration` template directory and make it look like this:

    ```html
    {% extends "base.html" %}

    {% block title %}Logged out{% endblock %}

    {% block content %}
        <div class="site-hero py-5 bg-light mb-0">
            <div class="container">
                <div class="row align-items-center justify-content-between">
                    <div class="col-lg-12 text-center">
                        <h1 class="text-black mb-0"> You have successfully logged out!</h1>
                    </div>
                </div>
            </div>
        </div>
        <div class="section-grey bg-light">
            <div class="container">
                <div class="block">
                    <div class="row justify-content-center">
                        <div class="col-md-8 col-lg-8 pb-4 text-center">
                            <a href="{% url 'account:login' %}" class="btn btn-primary-hover-outline"> 
                                Go to login
                            </a>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    {% endblock %}
    ```

    This is the template that Django will display after the user logs out. After adding the URL patterns and the templates for login and logout views, your website is now ready for users to log in using Django authentication views.

    Let's add a way for the user to navigate to login and logout in the `base.html`:

    In the `<header>` tag just after the `<div>` containing "Python

    ```html
        <div class="container">
      <nav class="site-nav">
        <div class="row justify-content-between align-items-center">
            <div class="d-none d-lg-block col-lg-3 top-menu">
            </div>
            <div class="col-3 d-lg-block col-md-6 col-lg-6 text-lg-center logo">
              <a href="">Python<span class="text-primary">Bugs</span></a>
            </div>
            <div class="col-9 col-md-6 col-lg-3 text-right top-menu">
              <div class="d-inline-flex align-items-center">
              {% if request.user.is_authenticated %}
              <a href="{% url 'account:logout' %}" class="d-inline-flex align-items-center">
              <span>Logout</span>
              </a>
              {% else %}
              <a href="{% url 'account:login' %}" class="d-inline-flex align-items-center">
              <span>Login</span>
              </a>
              {% endif %}
              </div>      
            </div>
          </div>
          <div class="d-none d-lg-block row align-items-center py-3">
            <div class="col-12 col-sm-12 col-lg-12 site-navigation text-center">
              <ul class="js-clone-nav d-none d-lg-inline-block text-left site-menu">
                <li><a href="{% url 'blog:home' %}">Home</a></li>
                <li><a href="#">Contact</a></li>
              </ul>
            </div>
          </div>  
        </div>
      </nav> <!-- END nav -->
    </div> <!-- END container -->
    ```

    In the preceding code you check if the is logged in using `{% if request.user.is_authenticated %}` and render the logout link using `{% url 'account:logout' %}` otherwise you render the login link via `{% url 'account:login' %}`

5. User registration

    Let's create a simple view to allow user registration on your website. Initially, you have to create a form to let the user enter a username, their real name, and a password.

    1. Create a `forms.py` file located inside the `account` application directory and add the following code to it:

        ```python
        from django import forms
        from django.contrib.auth.models import User


        class UserRegistrationForm(forms.ModelForm):
            password = forms.CharField(label='Password', widget=forms.PasswordInput)
            password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
            
            class Meta:
                model = User
                fields = ('username', 'first_name', 'email')

            def clean_password2(self):
                cd = self.cleaned_data
                if cd['password'] != cd['password2']:
                    raise forms.ValidationError("Passwords don't match.")
                return cd['password2']
        ```

        You have created a model form for the user model. In your form, you include only the `username`, `first_name`, and `email` fields of the model. These fields will be validated based on their corresponding model fields. For example, if the user chooses a username that already exists, they will get a validation error because `username` is a field defined with `unique=True`.

        You have added two additional fields—`password` and `password2`—for users to set their password and confirm it. You have defined a `clean_password2()` method to check the second password against the first one and not let the form validate if the passwords don't match. This check is done when you validate the form by calling its `is_valid()` method. You can provide a `clean_<fieldname>()` method to any of your form fields in order to clean the value or raise form validation errors for a specific field. Forms also include a general `clean()` method to validate the entire form, which is useful to validate fields that depend on each other. In this case, you use the field-specific `clean_password2()` validation instead of overriding the `clean()` method of the form. This avoids overriding other field-specific checks that the `ModelForm` gets from the restrictions set in the model (for example, validating that the `username` is unique).

        Django also provides a `UserCreationForm` form that you can use, which resides in `django.contrib.auth.forms` and is very similar to the one you have created.

    2. Edit the `views.py` file of the account application and add the following code to it:

        ```python
        from django.shortcuts import render, redirect
        from .forms import UserRegistrationForm


        def register(request):
            if request.method == "POST":
                registration_form = UserRegistrationForm(request.POST)
                if registration_form.is_valid():
                    # Create a new user object without saving it
                    new_user = registration_form.save(commit=False)
                    # Set the user password
                    new_user.set_password(
                        registration_form.cleaned_data['password'])
                    # Save the user object
                    new_user.save()
                    return redirect('account:login')
            else:
                registration_form = UserRegistrationForm()
            
            return render(request, "account/register.html", {"form": registration_form})
        ```

        The view for creating user accounts is quite simple. For security reasons, instead of saving the raw password entered by the user, you use the `set_password()` method of the user model that handles hashing.

    3. Edit the `urls.py` file of your account application and add the following URL pattern:

        ```python
        path('register/', views.register, name='register'),
        ```

    4. Create a new directory called `account` in the template directory, this is where we will store templates for the register view.

        Add a template file in the `account` template directory and name it register.html. Add the following code to it:

        ```html
        {% extends "base.html" %}

        {% block title %}Register{% endblock %}

        {% block content %}
            <div class="site-hero py-5 bg-light mb-0">
                <div class="container">
                    <div class="row align-items-center justify-content-between">
                        <div class="col-lg-12 text-center">
                            <h1 class="text-black mb-0">Register</h1>
                        </div>
                    </div>
                </div>
            </div>
            <div class="section-grey bg-light">
                <div class="container">
                    <div class="block">
                        <div class="row justify-content-center">
                            <div class="col-md-8 col-lg-8 pb-4 text-center">
                                <form method="post">
                                    {% csrf_token %}
                                    {{ form.as_p }}     
                                    <input type="submit" class="btn btn-primary-hover-outline" value="Register">
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        {% endblock %}
        ```

        Now open http://127.0.0.1:8000/account/register/ in your browser. You will see the registration page you have created:

        ![Register Page](example_imgs/register-page.png)

    5. Add register URL to `base.html` template:

        Locate the `{% else %}` tag in the `<header>` and add the following code:

        ```html
        <a href="{% url 'account:register' %}" class="d-inline-flex align-items-center btn btn-primary-hover-outline">
            <span>Register</span>
        </a>
        ```

        Now open http://127.0.0.1:8000/account/register/ in your browser. You will see the button you have added:

        ![Register Page](example_imgs/complete-register.png)

### Sessions

All communication between web browsers and servers is via HTTP, which is stateless. The fact that the protocol is stateless means that messages between the client and server are completely independent of each other — there is no notion of "sequence" or behavior based on previous messages. As a result, if you want to have a site that keeps track of the ongoing relationships with a client, you need to implement that yourself.

Sessions are the mechanism used by Django (and most of the Internet) for keeping track of the "state" between the site and a particular browser. Sessions allow you to store arbitrary data per browser, and have this data available to the site whenever the browser connects. Individual data items associated with the session are then referenced by a "key", which is used both to store and retrieve the data.

Django uses a cookie containing a special session id to identify each browser and its associated session with the site. The actual session data is stored in the site database by default (this is more secure than storing the data in a cookie, where they are more vulnerable to malicious users). You can configure Django to store the session data in other places (cache, files, "secure" cookies), but the default location is a good and relatively secure option.

**Enabling sessions**

Sessions are automatically created when you start a django project.

The configuration is set up in the `INSTALLED_APPS` and `MIDDLEWARE` sections of the projects `settings.py`, as shown below:

```python
INSTALLED_APPS = [
    # …
    'django.contrib.sessions',
    # …
]

MIDDLEWARE = [
    # …
    'django.contrib.sessions.middleware.SessionMiddleware',
    # …
]
```

**Using sessions**

You can access the session attribute within a view from the request parameter (an HttpRequest passed in as the first argument to the view). This session attribute represents the specific connection to the current user (or to be more precise, the connection to the current browser, as identified by the session id in the browser's cookie for this site).

The session attribute is a dictionary-like object that you can read and write as many times as you like in your view, modifying it as wished. You can do all the normal dictionary operations, including clearing all data, testing if a key is present, looping through data, etc. Most of the time though, you'll just use the standard "dictionary" API to get and set values.

The code fragments below show how you can get, set, and delete some data with the key "my_car", associated with the current session (browser).

```python
# Get a session value by its key (e.g. 'my_car'), raising a KeyError if the key is not present
my_car = request.session['my_car']

# Get a session value, setting a default if it is not present ('mini')
my_car = request.session.get('my_car', 'mini')

# Set a session value
request.session['my_car'] = 'mini'

# Delete a session value
del request.session['my_car']
```

> One of the great things about Django is that you don't need to think about the mechanisms that tie the session to your current request in your view. If we were to use the fragments below in our view, we'd know that the information about `my_car` is associated only with the browser that sent the current request.

**Saving session data**

By default, Django only saves to the session database and sends the session cookie to the client when the session has been modified (assigned) or deleted. If you're updating some data using its session key as shown in the previous section, then you don't need to worry about this! For example:

```python
# This is detected as an update to the session, so session data is saved.
request.session['my_car'] = 'mini'
```

If you're updating some information within session data, then Django will not recognize that you've made a change to the session and save the data (for example, if you were to change "wheels" data inside your "my_car" data, as shown below). In this case you will need to explicitly mark the session as having been modified.

```python
# Session object not directly modified, only data within the session. Session changes not saved!
request.session['my_car']['wheels'] = 'alloy'

# Set session as modified to force data updates/cookie to be saved.
request.session.modified = True
```

As a simple real-world example we'll update our blog to tell the current user how many times they have visited the home page.

1. Open `blog/views.py`, and add the lines that contain num_visits into `home():`

    ```python
    # Getting session a session value and setting a default if its not present
    num_visits = request.session.get('num_visits', 0)
    
    # Creating a session variable
    request.session['num_visits'] = num_visits + 1
    ```

    Here we first get the value of the `num_visits` session key, setting the value to `0` if it has not previously been set. Each time a request is received, we then increment the value and store it back in the session (for the next time the user visits the page).

2. Add `num_visits` as a context variable in the render function

    ```python
    return render(request, 'blog/index.html', {"welcome_text": text,
                                               "all_posts": posts,
                                               "num_visits": num_visits})
    ```

     The `num_visits` variable is passed to the template in our context variable.

3. Add `num_visits` to the bottom of the `blog/index.html` template:

    ```html
    <p> You have visited this page {{ num_visits }} times.</p>
    ```

Run the development server using `python manage.py runserver` and navigate to [`http://127.0.0.1:8000/blog/`](http://127.0.0.1:8000/blog/) and you see the following:

![Page Visits counter](example_imgs/page-visits.png)

Refresh the page a few times and you should see the count go up

### Testing

**What does Django provide for testing?**

Testing a website is a complex task, because it is made of several layers of logic – from HTTP-level request handling, to model queries, to form validation and processing, and template rendering.

Django provides a test framework with a small hierarchy of classes that build on the Python standard unittest library. Despite the name, this test framework is suitable for both unit and integration tests. The Django framework adds API methods and tools to help test web and Django-specific behavior. These allow you to simulate requests, insert test data, and inspect your application's output. Django also provides an API (`LiveServerTestCase`) and tools for using different testing frameworks, for example you can integrate with the popular Selenium framework to simulate a user interacting with a live browser.

To write a test you derive from any of the Django (or unittest) test base classes (`SimpleTestCase`, `TransactionTestCase`, `TestCase`, `LiveServerTestCase`) and then write separate methods to check that specific functionality works as expected (tests use "`assert`" methods to test that expressions result in True or False values, or that two values are equal, etc.) When you start a test run, the framework executes the chosen test methods in your derived classes. The test methods are run independently, with common setup and/or tear-down behavior defined in the class, as shown below.

```python
class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)
```

The best base class for most tests is `django.test.TestCase`. This test class creates a clean database before its tests are run, and runs every test function in its own transaction. The class also owns a test Client that you can use to simulate a user interacting with the code at the view level. In the following sections we're going to concentrate on unit tests, created using this `TestCase` base class.

**What should you test?**

You should test all aspects of your own code, but not any libraries or functionality provided as part of Python or Django.

So for example, consider the `Author` model defined below. You don't need to explicitly test that `first_name` and `last_name` have been stored properly as `CharField` in the database because that is something defined by Django (though of course in practice you will inevitably test this functionality during development). Nor do you need to test that the `date_of_birth` has been validated to be a date field, because that is again something implemented in Django.

However you should check the text used for the labels (First name, Last name, Date of birth, Died), and the size of the field allocated for the text (100 chars), because these are part of your design and something that could be broken/changed in future.

```python
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
```

Similarly, you should check that the custom methods `get_absolute_url()` and `__str__()` behave as required because they are your code/business logic. In the case of get_absolute_url() you can trust that the Django `reverse()` method has been implemented properly, so what you're testing is that the associated view has actually been defined.

> Astute readers may note that we would also want to constrain the date of birth and death to sensible values, and check that death comes after birth. In Django this constraint would be added to your form classes (although you can define validators for model fields and model validators these are only used at the form level if they are called by the model's `clean()` method. This requires a` ModelForm`, or the model's `clean()` method needs to be specifically called.)

**Test structure overview**

Django uses the unittest module's built-in test discovery, which will discover tests under the current working directory in any file named with the pattern `test*.py`. Provided you name the files appropriately, you can use any structure you like. We recommend that you create a module for your test code, and have separate files for models, views, forms, and any other types of code you need to test. For example:

        ├── blog/
            ├── tests/
                ├── __init__.py
                ├── test_forms.py
                ├── test_models.py
                └── test_views.py

Create a file structure as shown above in your project. The `__init__.py` should be an empty file (this tells Python that the directory is a package). You can create the three test files by copying and renaming the skeleton test file `/blog/tests.py`.

Open `/blog/tests/test_models.py`. The file should import django.test.TestCase, as shown:

```python
from django.test import TestCase

# Create your tests here.
```

Often you will add a test class for each model/view/form you want to test, with individual methods for testing specific functionality. In other cases you may wish to have a separate class for testing a specific use case, with individual test functions that test aspects of that use-case (for example, a class to test that a model field is properly validated, with functions to test each of the possible failure cases). Again, the structure is very much up to you, but it is best if you are consistent.

Add the test class below to the bottom of the file. The class demonstrates how to construct a test case class by deriving from `TestCase`.

```python
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
```

The new class defines two methods that you can use for pre-test configuration (for example, to create any models or other objects you will need for the test):

* `setUpTestData()` is called once at the beginning of the test run for class-level setup. You'd use this to create objects that aren't going to be modified or changed in any of the test methods.
* `setUp()` is called before every test function to set up any objects that may be modified by the test (every test function will get a "fresh" version of these objects).

> The test classes also have a `tearDown()` method which we haven't used. This method isn't particularly useful for database tests, since the TestCase base class takes care of database teardown for you.

**How to run the tests**

The easiest way to run all the tests is to use the command:

```shell
python3 manage.py test
```

This will discover all files named with the pattern `test*.py` under the current directory and run all tests defined using appropriate base classes. By default the tests will individually report only on test failures, followed by a test summary.

**Running specific tests**
If you want to run a subset of your tests you can do so by specifying the full dot path to the package(s), module, TestCase subclass or method:

```shell
# Run the specified module
python3 manage.py test blog.tests

# Run the specified module
python3 manage.py test blog.tests.test_models

# Run the specified class
python3 manage.py test blog.tests.test_models.YourTestClass

# Run the specified method
python3 manage.py test blog.tests.test_models.YourTestClass.test_one_plus_one_equals_two
```

**Models**
As discussed above, we should test anything that is part of our design or that is defined by code that we have written, but not libraries/code that is already tested by Django or the Python development team.

For example, consider the `Post` model below. Here we should test the labels for all the fields, because even though we haven't explicitly specified most of them, we have a design that says what these values should be. If we don't test the values, then we don't know that the field labels have their intended values. Similarly while we trust that Django will create a field of the specified length, it is worthwhile to specify a test for this length to ensure that it was implemented as planned.

```python
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish', null=False, verbose_name="Slug")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ('-publish',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post-detail', args=[self.slug])
```

Open our `/blog/tests/test_models.py`, and replace any existing code with the following test code for the `Post` model.

Here you'll see that we first import `TestCase` and derive our test class (`PostModelTest`) from it, using a descriptive name so we can easily identify any failing tests in the test output. We then call `setUpTestData()` to create an author object that we will use but not modify in any of the tests.

```python
from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

class TestPostModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username="test_author", 
                                     email="testing@blog.com", 
                                     password="testingpass123")
        # user = User.objects.create(username="new_user")
        Post.objects.create(title="Testing Post", slug="testing-post",
                            author=user, body="This is a testing Post.",
                            created=timezone.now, updated=timezone.now,
                            status='published')
    
    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_name = f"{post.title}"
        # self.assertTrue(isinstance(post, Post))
        self.assertEqual(str(post), expected_name)
        
    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/blog/post/testing-post/')
        
    def test_slug_label(self):
        post = Post.objects.get(id=1)
        field_name = post._meta.get_field('slug').verbose_name
        self.assertEqual(field_name, 'Slug')
        
    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        field_max_length = post._meta.get_field('title').max_length
        self.assertEqual(field_max_length, 200)
```

The interesting things to note are:

* We can't get the `verbose_name` directly using `post.slug.verbose_name`, because `post.slug` is a string (not a handle to the `slug` object that we can use to access its properties). Instead we need to use the author's `_meta` attribute to get an instance of the field and use that to query for the additional information.
* We chose to use `assertEqual(field_name,'Slug')` rather than `assertTrue(field_name == 'Slug')`. The reason for this is that if the test fails the output for the former tells you what the label actually was, which makes debugging the problem just a little easier.
* We also need to test our custom methods. These essentially just check that the object name was constructed as we expected using the post title, and that the URL we get for an `Post` item is as we would expect.

**Forms**

The philosophy for testing your forms is the same as for testing your models; you need to test anything that you've coded or your design specifies, but not the behavior of the underlying framework and other third party libraries.

Generally this means that you should test that the forms have the fields that you want, and that these are displayed with appropriate labels and help text. You don't need to verify that Django validates the field type correctly (unless you created your own custom field and validation) — i.e. you don't need to test that an email field only accepts emails. However you would need to test any additional validation that you expect to be performed on the fields and any messages that your code will generate for errors.

Consider our form for adding comments.

```python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
```

Open our `/blog/tests/test_forms.py` file and replace any existing code with the following test code for the RenewBookForm form. We start by importing our form and some Python and Django libraries to help test time-related functionality. We then declare our form test class in the same way as we did for models, using a descriptive name for our `TestCase`-derived test class.

```python
from django.test import TestCase
from blog.forms import CommentForm
from django.utils import timezone
from datetime import datetime

class CommentFormTest(TestCase):
    
    # @classmethod
    # def setUpTestData(cls):
    
    def test_form_submission_date(self):
        form = CommentForm(
            data={
                "name": "Commenter",
                "email": "commenter@blog.com",
                "body": "Testing comment submission",
            }
        )
        form1 = CommentForm(
            data={
                "email": "commenter@blog.com",
                "body": "Testing comment submission",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertFalse(form1.is_valid())
        
    def test_form_date_timezone(self):
        form = CommentForm(
            data={
                "name": "Commenter",
                "email": "commenter@blog.com",
                "body": "Testing comment submission",
                "created": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())
```

**Views**

To validate our view behavior we use the Django test Client. This class acts like a dummy web browser that we can use to simulate `GET` and `POST` requests on a URL and observe the response. We can see almost everything about the response, from low-level HTTP (result headers and status codes) through to the template we're using to render the HTML and the context data we're passing to it. We can also see the chain of redirects (if any) and check the URL and status code at each step. This allows us to verify that each view is doing what is expected.

Consider our simplest view found at `http://127.0.0.1:8000/blog/` :

```python
def home(request):
    text = "Welcome to the PythonBugs Blog"
    posts = Post.objects.all()
    
    # Getting session a session value and setting a default if its not present
    num_visits = request.session.get('num_visits', 0)
    
    # Creating a session variable
    request.session['num_visits'] = num_visits + 1
    
    return render(request, 'blog/index.html', {"welcome_text": text,
                                               "all_posts": posts,
                                               "num_visits": num_visits})
```

Open the `/blog/tests/test_views.py` file and replace any existing text with the following test code for `home()`. As before we import our model and some useful classes. In the `setUpTestData()` method we set up a number of Post objects.

```python
class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        user = User.objects.create(username="test_author",
                                   email="testing@blog.com",
                                   password="testingpass123")
         
        num_of_posts = 10
        
        for post_num in range(num_of_posts):
            Post.objects.create(
                title=f"Testing Post {post_num}", 
                slug=f"testing-post-{post_num}",
                author=user,
                body="This is a testing Post.",
                created=timezone.now,
                updated=timezone.now,
                status='published')
            
    def test_view_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
    
    def test_list_all_posts(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['all_posts']), 10)
```

All the tests use the client (belonging to our TestCase's derived class) to simulate a GET request and get a response. The first version checks a specific URL (note, just the specific path without the domain).

```python
response = self.client.get('/blog/')
```

Once we have the response we query it for its status code, the template used, the number of items returned, and the total number of items.
The most interesting variable we demonstrate above is `response.context`, which is the context variable passed to the template by the view. This is incredibly useful for testing, because it allows us to confirm that our template is getting all the data it needs. In other words we can check that we're using the intended template and what data the template is getting, which goes a long way to verifying that any rendering issues are solely due to template.

**Views that are restricted to logged in users**

In some cases you'll want to test a view that is restricted to just logged in users. For example our post_detail view is very similar to our previous view but is only available to logged in users, and only displays a specific post.

```python
@login_required
def post_detail(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)

    #  List of active comments
    comments = blog_post.comments.filter(active=True)
    
    new_comment = None
    
    if request.method == "POST":
        # A comment was passed
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create the comment but dont save
            new_comment = comment_form.save(commit=False)
            # Assign post to the form
            new_comment.post = blog_post
            # Save the comment
            new_comment.save()
    else:
        # For GET request.
        comment_form = CommentForm()
    
    return render(request, 'blog/post-detail.html',
                  {"post": blog_post, "comments": comments,
                   "new_comment": new_comment, "comment_form": comment_form})
```

Add the following test code to `/blog/tests/test_views.py`. Here we first use SetUpTestData() to create some user login accounts and post objects (along with their posts) that we'll use later in the tests.

```python
class PostDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create(username="test_author1",
                                   email="testing1@blog.com",
                                   password="testingpass123")
        
        user2 = User.objects.create(username="test_author2",
                                   email="testing2@blog.com",
                                   password="testingpass123")
        
        post = Post.objects.create(
                title=f"Testing Post", 
                slug=f"testing-post",
                author=user1,
                body="This is a testing Post.",
                created=timezone.now,
                updated=timezone.now,
                status='published')
        
        Comment.objects.create(
            post=post,
            name="Test Commenter",
            email="commneter@blog.com",
            body="Test comment",
            # created=str(timezone.now),
            # updated=timezone.now,
            # active=True,
        )
        

    def test_redirect_if_not_authenticated(self):
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/account/login/'))
    
    def test_logged_in_url(self):
        user = User.objects.get(id=2)
        logged_in = self.client.force_login(user)
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(response.status_code, 200)    
    
    def test_view_uses_correct_template(self):
        user = User.objects.get(id=2)
        logged_in = self.client.force_login(user)
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post-detail.html')
         
    def test_comments_exist(self):
        user = User.objects.get(id=2)
        post = Post.objects.get(id=1)
        logged_in = self.client.force_login(user)
        response = self.client.get('/blog/post/testing-post/')
        self.assertEqual(len(response.context['comments']), 1)
```

**Testing views with forms**

Testing views with forms is a little more complicated than in the cases above, because you need to test more code paths: initial display, display after data validation has failed, and display after validation has succeeded. The good news is that we use the client for testing in almost exactly the same way as we did for display-only views.

we will use the same post detail c=view to test views with forms.

We've already tested that the view is only available to users that are logged in.

Add the test method (shown below) to the bottom of `/blog/tests/test_views.py`. This creates logs a user in and creates a new comment under the post.

```python
    # ....
        
    def test_comment_submission(self):
        user = User.objects.get(id=2)
        post = Post.objects.get(id=1)
        logged_in = self.client.force_login(user)
        response = self.client.post('/blog/post/testing-post/', kwargs=
                                    {"post":post,
                                     "name": "Second Commenter",
                                     "email":"commenter2@blog.com",
                                     "body":"2nd Test comment."})
        self.assertEqual(response.status_code, HTTPStatus.OK)
```

Writing test code is neither fun nor glamorous, and is consequently often left to last (or not at all) when creating a website. It is however an essential part of making sure that your code is safe to release after making changes, and cost-effective to maintain.
Most importantly we've provided a brief summary of what you should test, which is often the hardest thing to work out when you're getting started. There is a lot more to know, but even with what you've learned already you should be able to create effective unit tests for your websites.

### Logging

Logging is a technique or medium which can let us track some events as the software executes. It is an important technique for developers. It helps them to track events. Logging is like an extra set of eyes for them. Developers are not only responsible for making software but also for maintaining them.

Logging helps with that part of maintenance immensely.

It tracks every event that occurs at all times. That means instead of the long tracebacks you get much more. This time when an error occurs you can see in which the system was. This method will help you resolve errors quickly. As you will be able to tell where the error occurred.

**How does it work? What’s the idea behind it?**

The logging is handled by a separate program. That logging program is simply a file-writer. The logger is said to record certain events in text format. The recorded information is then saved in files. The files for this are called logs.

The logs are simple files saved with log extension. They contain the logs of events occurred.

Well, this is just one of the most used implementations, as you can see. Since we are just storing the information, you can come up with more ways to deal with it.

Okay, it’s clear to us that logging is important. Is it difficult? No, absolutely not. Logging is not difficult at all. Anyone who knows a little bit about the setup can use this.

Being a Python programmer, you get extra features here too. We got a whole module that lets us accomplish just that. As for other languages, there are many modules, Java has Log4j and JavaScript has its own loglevel.

**Logging Module in Python**

The logging module is a built-in Python module. It comes preinstalled with Python 3. Logging module is used to keep track of the events that occur as the program runs. That can be extended to any number of programs and thus for software, it is easy to set up and use.

**Why use logging module?**
As a developer, we can ask why use the logging module. All logging does is writing to a file or printing it on the console. All that can be achieved by using print statements. Then what is the need for a logging module?. That’s a valid question. The answer to that is logging is a module that gives what print cannot.

We use print function to output something on console. So, when a function occurs, we can get a print statement that the function executed. While that approach works with smaller applications, it is inefficient.

Print function becomes part of your program and if the software stops working, you won’t get the result. Also, if anything occurs and system restarts, the console is also clear. So, what will you do then? The answer to that is logging module.

**The logging module is capable of:**

* Multithreading execution
* Categorizing Messages via different log levels
* It’s much more flexible and configurable
* Gives a more structured information

There are 4 main parts of logging module. We will look at them one by one.

1. **Loggers**

    The loggers are the objects that developers deal with. They can be understood as a function which will be invoked when they are called. We use loggers in our project files. Thus, when the function is invoked, we get a detailed report. The logger can generate multiple levels of responses.

    We can customize it to full extent.

2. **Handlers**

    Handlers are the objects which emit the information. Think of them as newspaper handlers. Their main task is to transmit the information. That can be achieved by writing the info in a log file (The default behaviour). There are various handlers provided by logging module.

    We can easily set-up multiple handlers for the same logger. There are SMTP Handlers too which will mail the log records to you. The handlers usually contain business logic for logging information.

3. **Formatters**

    The formatters are the ones which format the data. You see handlers cannot send the information as it’s a Python data type. Before it can be sent to anyone, it needs to be converted.

    The logs are by-default in Log Records format. That is the class pre-defined by logging framework. It gives various methods to developers to use. That format can not be directly sent over a network or written in a text file. To convert that or format that, we need formatters.

    There are different formatters for different handlers.

    By default, the formatters will convert the Log Record into String. This behaviour can be easily changed and you can customize this as you want. This format can be based on the business logic that we write in Handlers.

4. **Filters**

    The last piece of the logging module is filters. The filters, as the name suggests, filter the messages. Not every message we pass needs to be stored or transported. Or there can be different handlers for different messages. All that is achievable with the help of filters.

    We can use filters with both loggers and handlers.

It also provides us with message levels. The message levels are defined as:

**DEBUG:** It is verbose system information when everything is running fine. It will tell you more precise details about the state of the system. Its severity point is 10.

**INFO:** The info will produce less verbose system information but is similar to debug. It generally tells an overview of what the system is executing. Its severity point is 20.

**WARNING:** This contains information regarding low-level problems. The problems may be ignored as they don’t cause the system to halt. Although, it is recommended that these problems shall be resolved.

Its severity point is 30.

**ERROR:** This message is serious. The error will contain information about the major problem that has occurred. The problem may have stopped the operation of program and needs immediate attention.

Its severity point is 40.

**CRITICAL:** The most critical message. This message is emitted when the problem has caused the system to stop. That means the whole application has halted due to this problem.

Its severity point is 50.

The severity point determines what priority shall be given. Suppose, we set the log level to be 30. Then the logger will log or store the information when the level is greater than or equal to 30. So, you just need to confirm what level of logging you want.

![Logging Message Levels](example_imgs/logging.png)

**Logging in Django**

Django provides logging by using the logging module of Python. The logging module can be easily configured.

**Configuring Settings**

For including logging in Django, we need to configure its settings. Doing that is pretty easy. By configuring logging settings, we mean to define:

* Loggers
* Handlers
* Filters
* Formatters

Just copy this code in your `settings.py`:

```python
# Authentication settings
LOGIN_REDIRECT_URL = 'blog:home'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    
    ##Handlers
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            # Filename where logs will be kept
            "filename": "pythonbugs-debug.log",
        },
        "console": {
            "class": "logging.StreamHandler",         
        }, 
    },
    
    ## Loggers
    "loggers": {
        "django": {
            # specifying predefined handlers to use when writing logs
            "handlers": ['file', 'console'],
            # Filtering the level of messages to be written to logs
            "level": "DEBUG",
            # Specify whether to write across all logs or not
            "propagate": True,
            # Logging level for Djangos built-in/default loggers
            "level": os.getenv('DJANGO_LOG_LEVEL', 'DEBUG')  
        },
    },        
}
```

