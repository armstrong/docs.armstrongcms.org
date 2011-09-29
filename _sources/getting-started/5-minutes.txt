.. _getting-start/5-minutes:

5 Minute Tutorial
=================
The first thing you need to do is install Armstrong (see :ref:`installation`).
This installs the ``armstrong`` command line tool that we're going to be using
throughout.

The first step is initializing a new Armstrong project.  Armstrong projects are a customized Django project layout.  In addition to creating a base project structure, the ``armstrong`` tool can add demo data as well.  We're going to use that feature for this tutorial so you don't have to worry about creating data.  To create a new project type the following in the command line:

.. code-block:: bash
    $ armstrong init --template=tutorial mysite
    armstrong initialized!
    $

This creates a project in the directory ``mysite`` based on the ``tutorial`` template.  Project templates are basic projects that provide a structure and generally some sort of bootstrapping depending on their environment.  For now, just know that the ``tutorial`` project template is what we're working from.

.. todo:: Add cross-ref to template docs once they are completed

The ``mysite`` part of the command tells Armstrong where to put your project.  Using that, it's in the ``./mysite`` directory.  You can use any name you like, but for the rest of this tutorial, I'm going to assume that you used ``mysite``.


Before you start the server
---------------------------
There are a few steps you need to take before you can run any Armstrong project for the first time.  Before anything else, you need to make sure all of the requirements are installed.  You do this via `pip`_ like this inside your ``mysite`` directory.

.. code-block:: bash

    $ pip install -r requirements/project.txt
    ... output from pip ...

This makes sure that everything is installed.  Armstrong has are a few dependencies that Armstrong has that are not released on PyPI.

Next, you need to configure the database connection.  You can change this by editing the ``settings/development.py`` file and adjusting the ``DATABASE`` settings.  Armstrong uses separate settings modules for different environments (see :ref:`getting-started/anatomy/settings`), but ``settings.development`` is the default one.

You can use any of the Django database drivers here.  For simplicity, I'm going to change it to use the sqlite3 backend.  Once I've made the changes, my ``DATABASE`` value looks like this:

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': project_dir('demo.db'),
        }
    }

This creates a ``demo.db`` directory in the same directory as your project.  The ``project_dir`` function is loaded from ``settings.defaults``.

Now that hte database is configured, you need to create the initial database.  Do that using Django's built-in ``syncdb`` command.

.. code-block:: bash

    $ armstrong syncdb
    Creating tables ...
    ... a lot more out from Django ...
    Installing custom SQL ...
    Installing indexes ...
    No fixtures found.
    $

.. todo:: update to reference migrations once they're in place

Our database is configured and created, now we can start the development server.


Starting the server
-------------------
Django ships with a built-in development server for testing applications.  That's the easiest way to test out everything (see :ref:`deploying` for production deployment tips).

To start a new server, simply use the ``runserver`` command like this.

.. code-block:: bash

    $ armstrong runserver
    Validating models...

    0 errors found
    Django version 1.3, using settings 'settings.development'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now you can load the Armstrong welcome page by loading ``http://127.0.0.1:8000/`` in your browser.

Getting data into Armstrong
---------------------------
.. todo:: add screenshots once the welcome screen looks a bit better.

The default Armstrong screen welcomes you to the system.  There's not much there as it's a simple direct-to-template view.  You can find it in the ``urls/defaults.py`` file.

.. code-block:: python

    # Load the Armstrong "success" page by default
    url(r'^$', TemplateView.as_view(template_name="index.html")),

Directly below that, there's a commented out URL pattern.  You can switch to that to use a ``QuerySetBackedWellView`` to display some real data.  There's a couple of new concepts here that we're going to gloss over until :ref:`getting-started/anatomy`–in particular, :ref:`getting-started/anatomy/wells`, and :ref:`getting-started/anatomy/published-content`.

For now, comment out the ``TemplateView`` above and uncomment out the other url pattern so it looks like this:

.. code-block:: python

    # Load the Armstrong "success" page by default
    #url(r'^$', TemplateView.as_view(template_name="index.html")),

    # Uncomment out this to change to the the well view
    url(r'^$',
        QuerySetBackedWellView.as_view(well_title='front_page',
                                       template_name="front_page.html",
                                       queryset=Article.published.all(), ),
        name='front_page'),

There's also a line commented out at the top that you need to uncomment.  It's the import line for ``QuerySetBackedWellView``.

.. code-block:: python

    from armstrong.core.arm_wells.views import QuerySetBackedWellView


Restart your ``runserver`` by hitting ``Control + C`` (shown as ``^C`` from here on out), then re-run ``armstrong runserver``.  Now when you load your page you should get a Django error page with ``DoesNotExist at /``.  This is becauase we're missing some data.

The ``tutorial`` template ships with some demo data that you can load to bootstrap this process.  Armstrong puts fixtures in its ``./fixtures/`` directory.  To load the demo data, stop the server with ``^C`` and run this:

.. code-block:: bash

    $ armstrong loaddata ./fixtures/demo_data.json
    Installed 202 object(s) from 1 fixture(s)

This loads a few sections (the way Armstrong categorizes content), a new well type (the model that allows you to schedule content to appear at a particular place), as well as a bunch of articles and some authors.

Restart ``runserver`` and load the front page.  You'll get a page with a bunch of articles of lorem ipsum with titles that have a distinctly Texas flavor because they came from real articles on the `Texas Tribune`_.


Editing Data in Armstrong
-------------------------
.. todo:: screenshots screenshots screenshots!!! (yes, they're worth three of everything)

You can edit the data in Armstrong using it's customized version of Django's built-in admin.  By default, it's available at ``/admin/`` of your site.  You can log in using the credentials you created during the ``syncdb`` step, or you can run ``armstrong createsuperuser`` to add a new super user if you skipped that step.

Explore around.  Wells are one of the more powerful concepts inside Armstrong.  Click on the ``Wells`` link and load the list of wells.  The demo data adds one---a well of the type ``front_page``.  That matches up with the ``well_title`` value we used in the URL routes earlier.

Click on the ``front_page`` link to load the edit form for that.  There are three boxes with article titles in them.  Reload the main page of the site (``http://localhost:8000/``), you'll see that they're the three same articles are the top articles on the site.

Click the X to remove one of the articles from the Well, click ``Save and continue editing``, then reload the front page.  The article you removed should no longer be in the top three.


Where to next?
--------------
Now you know how to create a new Armstrong project and a little bit about how they're laid out and you've seen the admin interface.  Next up, it's time to learn a bit more about how Armstrong is organized and what all of those directories in an Armstrong project are about in :ref:`getting-started/anatomy`.


.. _pip: http://www.pip-installer.org/
.. _Texas Tribune: http://www.texastribune.org/
