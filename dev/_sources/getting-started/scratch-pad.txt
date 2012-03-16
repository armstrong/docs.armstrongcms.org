.. This is just a scratch pad of stuff that's been written.  Nothing should link to this and this shouldn't live for very long.

Project Structure
-----------------
Here's what's in our new directory.

::

    |~api/
    | |-__init__.py
    | |-api.py
    | `-resources.py
    |~demo/
    | |-demo_database.sqlite3
    | `~fixtures/
    |   `-initial_data.json
    |~fixtures/
    | |-initial_data.json
    |~requirements/
    | |-development.txt
    | `-project.txt
    |~settings/
    | |-__init__.py
    | |-defaults.py
    | |-development.py
    | `-production.py
    |~templates/
    | `-index.html
    |~urls/
    | |-__init__.py
    | |-defaults.py
    | |-development.py
    | `-production.py
    |-wsgi.py

Let's break this down, directory by directory.

``api``
    *TODO*

``demo``
    *TODO*

``fixtures``
    Armstrong has some initial data that needs to be created for everything to work.  You can use this directory to add any other fixtures you need for your project.

    Keep in mind that Django doesn't automatically add fixtures from inside this directory.  In addition to the normal ``syncdb`` and ``migrate`` commands, you need to run ``armstrong loaddata ./fixtures/<your fixture>.json`` in order to load the data.

``requirements``
    This contains the `pip`_ requirements files.  Armstrong creates two for you: ``development.txt`` and ``project.txt``.  The development file is where you add any requirements that are only necessary for running in development mode.  The ``project.txt`` file is for specifying all of the dependencies of your project.

    Armstrong adds a few dependencies for you out of the box.  The first is the Armstrong version that you used to initialize the new project.  Second is a custom version of `mptt`_ that is unfortunately, not released yet.

``settings``
    Armstrong uses a ``settings`` module instead of the normal ``settings.py`` file.  This allows for greater flexibility and makes composing different settings for different environments much easier.

    The ``settings`` module by itself

``static``
    *TODO*

``templates``
    *TODO*

``urls``
    *TODO*

``wsgi.py``
    *TODO*

.. _mptt: https://github.com/django-mptt/django-mptt
.. _pip: http://www.pip-installer.org/