简体中文_
 
.. _简体中文: README-zh.rst

YABGP
=====

|Docker| |Version| |License| |Build Status| |Code Health| |Documentation Status| |Test Coverage| |Downloads|


What is yabgp?
~~~~~~~~~~~~~~

YABGP is a yet another Python implementation for BGP Protocol. It can be used to establish BGP connections with all kinds
of routers (include real Cisco/HuaWei/Juniper routers and some router
simulators like GNS3) and receive/parse BGP messages for
future analysis.

Support sending BGP messages(route refresh/update) to the peer through RESTful API. YABGP can't send any BGP update messages
by itself, it's just a agent, so there can be many agents and they can be controlled by a contoller.

We write it in strict accordance with the specifications of RFCs.

This software can be used on Linux/Unix, Mac OS and Windows systems.

Features
~~~~~~~~

-  It can establish BGP session based on IPv4 address (TCP Layer) in
   active mode(as TCP client);

-  Support TCP MD5 authentication(IPv4 and does not support Windows
   now);

-  BGP capabilities support: 4 Bytes ASN, Route Refresh(Cisco Route Refresh), Add Path send/receive;

-  Address family support:

   - IPv4/IPv6 unicast

   - IPv4/IPv6 Labeled Unicast

   - IPv4 Flowspec(limited)

   - IPv4 SR Policy(draft-previdi-idr-segment-routing-te-policy-07)

   - IPv4/IPv6 MPLSVPN

   - EVPN (partially supported)

-  Decode all BGP messages to json format and write them into files in local disk(configurable);

-  Support basic RESTFUL API for getting running information and sending BGP messages.

Quick Start
~~~~~~~~~~~

We recommend run ``yabgp`` through python virtual-env from source
code or pip install

Use yabgp from source code:

.. code:: bash

    $ virtualenv yabgp-virl
    $ source yabgp-virl/bin/activate
    $ git clone https://github.com/smartbgp/yabgp
    $ cd yabgp
    $ pip install -r requirements.txt
    $ cd bin
    $ python yabgpd -h

Use pip install

.. code:: bash

    $ virtualenv yabgp-virl
    $ source yabgp-virl/bin/activate
    $ pip install yabgp
    $ which yabgpd
    /home/yabgp/yabgp-virl/bin/yabgpd
    $ yabgpd -h

For example:

.. code:: bash

    $ yabgpd --bgp-local_addr=1.1.1.1 --bgp-local_as=65001 --bgp-remote_addr=1.1.1.2 --bgp-remote_as=65001 --bgp-afi_safi=ipv4

Use Docker container

.. code:: bash

    $ docker run -it smartbgp/yabgp:latest --bgp-afi_safi=ipv4 --bgp-local_as=65022 --bgp-remote_addr=10.75.44.219 --bgp-remote_as=65022

More docker image tags, please reference https://hub.docker.com/r/smartbgp/yabgp/tags/

Documentation
~~~~~~~~~~~~~

More information please see the documentation http://yabgp.readthedocs.org

Related Projects
~~~~~~~~~~~~~~~~

Routewatch brings automated alerting to YABGP. https://github.com/nerdalize/routewatch

A BGP update generator based on YaBGP https://github.com/trungdtbk/bgp-update-gen

Support
~~~~~~~

Please join our Slack_ for questions, discussion, suggestions, etc

Send email to xiaoquwl@gmail.com, or use GitHub issue system.


Contribute
~~~~~~~~~~

Please create Github Pull Request https://github.com/smartbgp/yabgp/pulls

More details please read HACKING.rst.

Thanks
~~~~~~

For core files like fsm, protocol, we copy some of the code from
https://github.com/wikimedia/PyBal/blob/master/pybal/bgp.py,

and message parsing, we reference from
https://github.com/Exa-Networks/exabgp

.. |License| image:: https://img.shields.io/hexpm/l/plug.svg
   :target: https://github.com/smartbgp/yabgp/blob/master/LICENSE
.. |Build Status| image:: https://travis-ci.org/smartbgp/yabgp.svg?branch=master
   :target: https://travis-ci.org/smartbgp/yabgp

.. |Code Health| image:: https://landscape.io/github/smartbgp/yabgp/master/landscape.svg?style=flat
   :target: https://landscape.io/github/smartbgp/yabgp/master

.. |Documentation Status| image:: https://readthedocs.org/projects/yabgp/badge/?version=latest
   :target: https://readthedocs.org/projects/yabgp/?badge=latest

.. |Test Coverage| image:: https://coveralls.io/repos/smartbgp/yabgp/badge.svg?branch=master
   :target: https://coveralls.io/r/smartbgp/yabgp

.. |Version| image:: https://img.shields.io/pypi/v/yabgp.svg?
   :target: http://badge.fury.io/py/yabgp

.. |Downloads| image:: https://img.shields.io/pypi/dm/yabgp.svg?
   :target: https://pypi.python.org/pypi/yabgp

.. |Docker| image:: https://img.shields.io/docker/automated/jrottenberg/ffmpeg.svg?style=plastic   
   :target: https://hub.docker.com/r/smartbgp/yabgp/
   
.. _Slack: https://join.slack.com/t/smartbgp/shared_invite/enQtNzQwNjgzNTA5NjA3LTY3YzFkODMzYWFjODI1ZmE3NDRkMTQwYTY0MWZiMmE3M2NiMzM0ZTI3NjNjY2RkNDAzMmFkZWJkOTE2M2VjOWU
