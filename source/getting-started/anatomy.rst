.. _getting-start/anatomy:

Anatomy of Armstrong
====================
Armstrong is a large project with a lot of moving parts.  This document introduces you to all of those parts and helps you find your around the Armstrong ecosystem.


Terms in Armstrong
------------------
Access Level
    *TODO*

Article
    An article represents one of the core objects inside Armstrong.  It's a title, body, summary, and additional meta data representing the articles on the site.

Assignment
    *TODO*

Backends
    *TODO*

Layout Templates
    *TODO*

Paywall
    *TODO*

Related Content
    *TODO*

Section
    *TODO*

Well
    *TODO*



Component Structure
-------------------
``armstrong.apps``
    Anything that starts with ``armstrong.apps`` is considered a stand-alone application in the traditional Django sense.  These occassionally have dependencies on other ``apps`` and components in the ``armstrong.core`` namespace.  These are the main entry points to functionality in Armstrong.

``armstrong.core``
    Anything that starts with ``armstrong.core`` is considered part of the core Armstrong system and should generally be installed on any system that's building on top of Armstrong.  The number of models created by using ``armstrong.core`` components should be minimum.  The only ``core`` components that install models are things which can only work with data stored.

``armstrong.hatband``
    Also known as "Hatband," ``armstrong.hatband`` is Armstrong's drop-in replacement for Django's built-in ``django.contrib.admin``.  This provides some extra functionality in the admin interface and provides many custom widgets that are relied upon by various Armstrong apps.

    Though Hatband does ship with some extra features that are meant to be used with Armstrong components, you can use Hatband within any Django project to create a better version of the Django admin.

``armstrong.utils``
    ``armstrong.utils`` is the catch-all namespace.  These are for entirely stand-alone components that might be used in multiple areas throughout Armstrong.  These should have limited (if any) dependencies on other parts of Armstrong outside of other ``armstrong.utils`` components and Django itself.


Individual Components
---------------------
A fresh installation of Armstrong installs the following components:

.. TODO: update with each release
.. code-block:: bash

    $ pip freeze | grep armstrong
    armstrong==11.12.0.1
    armstrong.apps.articles==1.1.0
    armstrong.apps.content==1.0.1
    armstrong.apps.images==1.1.0
    armstrong.apps.related-content==1.2.0
    armstrong.cli==1.1.0
    armstrong.core.arm-access==1.0.5
    armstrong.core.arm-content==1.0.0
    armstrong.core.arm-layout==1.0.0
    armstrong.core.arm-sections==1.0.1
    armstrong.core.arm-wells==1.3.3
    armstrong.hatband==1.2.3
    armstrong.utils.backends==1.0.0

The first package is the main Armstrong release.  Each of the other components are explained below:

``armstrong.apps.articles``
    .. include:: ../../vendor/armstrong.apps.articles/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.apps.content``
    .. include:: ../../vendor/armstrong.apps.content/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.apps.images``
    .. include:: ../../vendor/armstrong.apps.images/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.apps.related_content``
    **TODO**

``armstrong.cli``
    .. include:: ../../vendor/armstrong.cli/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.core.arm_access``
    .. include:: ../../vendor/armstrong.core.arm_access/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.core.arm_content``
    .. include:: ../../vendor/armstrong.core.arm_access/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.core.arm_layout``
    .. include:: ../../vendor/armstrong.core.arm_layout/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.core.arm_sections``
    .. include:: ../../vendor/armstrong.core.arm_sections/README.rst
       :start-line: 2
       :end-before: Usage


``armstrong.core.arm_wells``
    .. include:: ../../vendor/armstrong.core.arm_wells/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.hatband``
    .. include:: ../../vendor/armstrong.core.arm_wells/README.rst
       :start-line: 2
       :end-before: Usage

``armstrong.utils.backends``
    .. include:: ../../vendor/armstrong.utils.backends/README.rst
       :start-line: 2
       :end-before: Usage
