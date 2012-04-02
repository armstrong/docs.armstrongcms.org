.. _getting-start/anatomy:

Anatomy of Armstrong
====================
Armstrong is a large project with a lot of moving parts.  This document introduces you to all of those parts and helps you find your around the Armstrong ecosystem.


Terms in Armstrong
------------------
Access Level
    An Access Level corresponds to a class of users. In the most common case, a site will have one Access Level that is free for every user and a single Access Level for paid subscribers.

Article
    An article represents one of the core objects inside Armstrong.  It's a title, body, summary, and additional meta data representing the articles on the site.

Assignment
	An Assignment defines a time period during which users posessing an Access Level are allowed to view a piece of content. They consist of a start date/time, an end date/time, a link to a particular piece of content's access object and an Access Level

Backends
    Backends are a callable that can be changed at run-time via configuration.  These are generally used to provide flex-points where there are multiple ways to provide the same information.

Content
    A ``Content`` model provides a base class

Layout Templates
    Layout templates are templates used by the ``{% render_model %}`` template tag.  They're found inside the ``<template_path>/layout/`` directory and follow the pattern of ``<template_path>/<app_label>/<model>/<layout_name>.html``.

Paywall
	A paywall is a function that wraps your content detail views and ensures that all users who view a piece of content have the required Access Level. They are configurable to provide a number of different responses to an unauthorized user including redirects, rendering different templates or raising an exception.

Related Content
    Related content is a generic way to relate two completely separate models without either model having to know about the other.  This is useful for generic code and is used throughout Armstrong.  The flexibility comes with a slight performance hit, but most sites can cache their way out of the performance hit.

Section
    Sections provide a the foundation for a taxonomy for Django sites.  Models opt-in to be included in sections.  Each section has a series of items that it retrieves from the configured backend.  This is generally combined with a *well* to allow "pinning" an item to the top of a section.

Well
    Wells allow you to schedule content to appear at a given place on your site for a given time.  Wells are a particular Well Type and have zero or more Well Nodes.

Well Type
    Well Types allow you to specify all of the wells you want to use.  A Well Type can have any number of Wells created for it, but current Well for a given Well Type has a start date in the past and either no expiration date or an expiration date in the future.

Well Node
    Well Nodes are the connection between a Well and any model within Django.  They use a generic foreign key, but have some optimization to help remove some of the inherent inefficiency inside Django.


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
    armstrong==12.03.1
    armstrong.apps.articles==1.1.1
    armstrong.apps.content==1.0.2
    armstrong.apps.images==1.1.1
    armstrong.apps.related-content==2.0.1
    armstrong.cli==1.1.1
    armstrong.core.arm-access==1.0.6
    armstrong.core.arm-content==1.3.2
    armstrong.core.arm-layout==1.1.1
    armstrong.core.arm-sections==1.5.3
    armstrong.core.arm-wells==1.6.0
    armstrong.hatband==1.2.4
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
    .. include:: ../../vendor/armstrong.apps.related_content/README.rst
       :start-line: 2
       :end-before: Usage

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
