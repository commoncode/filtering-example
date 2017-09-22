Generic Filtering Example Project
=================================


A quick and dirty Django project to illustrate an approach to generic filtering that can be used throughout a Django project to ensure that views and other business logic are easily restricted by the currently logged in user.

This is a complement to the presentation: `Reusable filtering for Django and DRF`_


It is mostly for illustrative purposes, but if you do wish to run it yourself you will need to follow this process:

#. Clone this repo locally with ``git clone git@github.com:commoncode/filtering-example.git``
#. Change into the locally checked out folder ``cd filtering-example``
#. Create and activate a python virtualenv  (e.g.  ``python3 -v venv filtering_venv  && source filtering_venv/bin/activate``)
#. Install the requirements with ``pip install -r requirements.txt``
#. Run migrations ``pracman/manage.py migrate``
#. Create a super user with ``pracman/manage.py createsuperuser``
#. Start dev server ``pracman/manage.py runserver``


Once the above has been completed you should be able to login into admin using: `http://127.0.0.1:8000/admin <http://127.0.0.1:8000/admin/>`_


The following REST endpoints are also available:


* `http://127.0.0.1:8000/api/appointments <http://127.0.0.1:8000/api/appointments>`_
* `http://127.0.0.1:8000/api/appointments/future <http://127.0.0.1:8000/api/appointments/future>`_



.. _`Reusable filtering for Django and DRF`: https://docs.google.com/presentation/d/1rPPx_eciyb_gmuJDnXWlZqTJABNMFvBqTYJumDDeGP0/edit
