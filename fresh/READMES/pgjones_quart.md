Quart
=====

.. image:: https://assets.gitlab-static.net/pgjones/quart/raw/main/artwork/logo.png
   :alt: Quart logo

|Build Status| |docs| |pypi| |python| |license| |chat|

Quart is an async Python web microframework. Using Quart you can,

* render and serve HTML templates,
* write (RESTful) JSON APIs,
* serve WebSockets,
* stream request and response data,
* do pretty much anything over the HTTP or WebSocket protocols.

Quickstart
----------

Quart can be installed via `pip
<https://docs.python.org/3/installing/index.html>`_,

.. code-block:: console

    $ pip install quart

and requires Python 3.7.0 or higher (see `python version support
<https://pgjones.gitlab.io/quart/discussion/python_versions.html>`_ for
reasoning).

A minimal Quart example is,

.. code-block:: python

    from quart import Quart, render_template, websocket

    app = Quart(__name__)

    @app.route("/")
    async def hello():
        return await render_template("index.html")

    @app.route("/api")
    async def json():
        return {"hello": "world"}

    @app.websocket("/ws")
    async def ws():
        while True:
            await websocket.send("hello")
            await websocket.send_json({"hello": "world"})

    if __name__ == "__main__":
        app.run()

if the above is in a file called ``app.py`` it can be run as,

.. code-block:: console

    $ python app.py

To deploy this app in a production setting see the `deployment
<https://pgjones.gitlab.io/quart/tutorials/deployment.html>`_
documentation.

Contributing
------------

Quart is developed on `GitLab <https://gitlab.com/pgjones/quart>`_. If
you come across an issue, or have a feature request please open an
`issue <https://gitlab.com/pgjones/quart/issues>`_. If you want to
contribute a fix or the feature-implementation please do (typo fixes
welcome), by proposing a `merge request
<https://gitlab.com/pgjones/quart/merge_requests>`_.

Testing
~~~~~~~

The best way to test Quart is with `Tox
<https://tox.readthedocs.io>`_,

.. code-block:: console

    $ pip install tox
    $ tox

this will check the code style and run the tests.

Help
----

The Quart `documentation <https://pgjones.gitlab.io/quart/>`_ or
`cheatsheet
<https://pgjones.gitlab.io/quart/reference/cheatsheet.html>`_ are the
best places to start, after that try searching `stack overflow
<https://stackoverflow.com/questions/tagged/quart>`_ or ask for help
`on gitter <https://gitter.im/python-quart/lobby>`_. If you still
can't find an answer please `open an issue
<https://gitlab.com/pgjones/quart/issues>`_.

Relationship with Flask
-----------------------

Quart is an asyncio reimplementation of the popular `Flask
<http://flask.pocoo.org/>`_ microframework API. This means that if you
understand Flask you understand Quart.

Like Flask Quart has an ecosystem of extensions for more specific
needs. In addition a number of the Flask extensions work with Quart.

Migrating from Flask
~~~~~~~~~~~~~~~~~~~~

It should be possible to migrate to Quart from Flask by a find and
replace of ``flask`` to ``quart`` and then adding ``async`` and
``await`` keywords. See the `docs
<https://pgjones.gitlab.io/quart/how_to_guides/flask_migration.html>`_
for more help.


.. |Build Status| image:: https://gitlab.com/pgjones/quart/badges/main/pipeline.svg
   :target: https://gitlab.com/pgjones/quart/commits/main

.. |docs| image:: https://img.shields.io/badge/docs-passing-brightgreen.svg
   :target: https://pgjones.gitlab.io/quart/

.. |pypi| image:: https://img.shields.io/pypi/v/quart.svg
   :target: https://pypi.python.org/pypi/Quart/

.. |python| image:: https://img.shields.io/pypi/pyversions/quart.svg
   :target: https://pypi.python.org/pypi/Quart/

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://gitlab.com/pgjones/quart/blob/main/LICENSE

.. |chat| image:: https://img.shields.io/badge/chat-join_now-brightgreen.svg
   :target: https://gitter.im/python-quart/lobby
