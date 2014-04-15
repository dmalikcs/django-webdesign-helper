=====
webhelper
=====

Webdesign-helper is collection of tags to provide flexibility for static
content in website

Installation
------------

* Install django-webhelper-helper through pip

.. code-block:: shell

    $pip install -e git://github.com/dmalikcs/django-webhelper-helper.git#egg=webhelper-helper

* Add "webhelper" to your INSTALLED_APPS setting like this

.. code-block:: python

      INSTALLED_APPS = (
          ...
          'webhelper',
      )


* Run `python manage.py migrate` to create the webhelper models.

* Start the development server and visit http://127.0.0.1:8000/admin/ to create a webhelper (you'll need the Admin app enabled).

* Visit http://127.0.0.1:8000/webhelper/ to participate in the poll.


Howtos webhelper tags
---------------------

* Load webhelper template

.. code-block:: html
    
    <html>
        ...
        {% load webhelper_tags %}
        ...
    </html>

* Sociallinks tag

.. code-block:: html
    
    <html>
        ....
        {% load webhelper_tags %}

        {% get_social_link 'facebook' %}
        {% get_social_link 'linkedin' %}
        {% get_social_link 'gplus' %}
        {% get_social_link 'twitter' %}
        ....
    </html>

* office address tag

.. code-block:: html
    
    <html>
        ....
        {% load webhelper_tags %}

        {% get_office_address as address %}
        {{ add.name }}
        {{ add.address }}
        {{ add.city }}
        {{ add.state }}
        {{ add.country }}
        ....
    </html>

* Register Address tag

.. code-block:: html
    
    <html>
        ....
        {% load webhelper_tags %}

        {% get_register_address as address %}
        {{ add.name }}
        {{ add.address }}
        {{ add.city }}
        {{ add.state }}
        {{ add.country }}
        ....
    </html>

* General Information tag

.. code-block:: html
    
    <html>
        ....
        {% load webhelper_tags %}

        {%  get_general_info 'phone_1' %}
        {%  get_general_info 'phone_2' %}
        {%  get_general_info 'phone_3' %}
        {%  get_general_info 'tollfree' %}
        {%  get_general_info 'support_email' %}
        {%  get_general_info 'sales_email' %}
        {%  get_general_info 'Billing_email' %}
        {%  get_general_info 'Website' %}
        ....
    </html>
