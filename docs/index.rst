===================
Welcome to RachioPy
===================

This python package provides a interface to the Rachio public API.

Library Installation
====================

.. code-block:: bash

   $ pip install rachiopy

Getting Started
===============

.. code-block:: python
    
    from rachiopy import Rachio
    
    r = Rachio("8e600a4c-0027-4a9a-9bda-dc8d5c90350d")
    resp, content = r.person.getInfo()

    print (resp["status"])
    print (content["id"])

This prints:

.. code-block:: text

    200
    ccd8bb4d-d7ef-407c-b029-1c578c7a98d8


Source code
===========

The project is hosted on GitHub

Please feel free to file an issue on the bug tracker if you have found a bug
or have some suggestion in order to improve the library.

Dependencies
============

- Python 3.6+
- httplib2

Authors and License
===================

The rachiopy package is written mostly by Robbert Verbruggen.

It's MIT licensed and freely available.

Feel free to improve this package and send a pull request to GitHub.

Table Of Contents
=================

.. toctree::
   :maxdepth: 2

   person
   device
   zone
   schedulerule
   flexschedulerule
   notification
   rachioobject

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
