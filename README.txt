=================
``gs.skin.green``
=================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A green skin for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-07-25
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

A green skin for GroupServer. The This skin takes the typeset page,
provided by ``gs.content.css``, and adds colours_.

Colours
=======

The most prominent colour is **hibiscus dream**, which is the background of
the page heading, and the text colour of all the headers. The most *common*
colour is **white,** which is the background of the page, followed by the
body text, which is **lead** grey:

+-------------+-----+--------------------+-------------------------------------+
| Colour      | Eg. | Colour description | Use                                 |
+=============+=====+====================+=====================================+
| ``#ffffff`` | |0| | White              |   ``<heading>`` title               |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<body>`` background             |
+-------------+-----+--------------------+-------------------------------------+
| ``#fffff6`` | |1| | Fog white          |   Disabled ``<button>`` text        |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<button>`` borders              |
+-------------+-----+--------------------+-------------------------------------+
| ``#d9e8bd`` | |2| | Dusty green        |   ``<heading> <a>`` text            |
|             |     |                    +-------------------------------------+
|             |     |                    |   Borders between items             |
+-------------+-----+--------------------+-------------------------------------+
| ``#b4d07b`` | |3| | Lime mist          |   Borders,                          |
|             |     |                    +-------------------------------------+
|             |     |                    |   Disabled ``<button>`` background  |
|             |     |                    +-------------------------------------+
|             |     |                    |   Muted ``<heading>`` text          |
+-------------+-----+--------------------+-------------------------------------+
| ``#669900`` | |5| | **Hibiscus dream** |   ``<heading>`` background          |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<button>`` background           |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<h1>``, ``<h2>``, ``<h3>`` text |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<a>``                           |
+-------------+-----+--------------------+-------------------------------------+
| ``#3b6600`` | |8| | Midnight forest    |   ``<heading> <button>`` background |
+-------------+-----+--------------------+-------------------------------------+
| ``#8c968a`` | |4| | Tropical whisper   |   Muted body text                   |
+-------------+-----+--------------------+-------------------------------------+
| ``#667366`` | |6| | Lead               |   ``<body>`` text                   |
+-------------+-----+--------------------+-------------------------------------+
| ``#404d40`` | |7| | Liquefaction grey  |   ``<h4>`` text                     |
|             |     |                    +-------------------------------------+
|             |     |                    |   ``<strong>``                      |
+-------------+-----+--------------------+-------------------------------------+

.. |0| raw:: html

  <span style="background:#ffffff;">&#160;Sample&#160;</style>

.. |1| raw:: html

  <span style="background:#fffff6;">&#160;Sample&#160;</style>

.. |2| raw:: html

  <span style="background:#d9e8bd;">&#160;Sample&#160;</style>

.. |3| raw:: html

  <span style="background:#b4d07b;">&#160;Sample&#160;</style>

.. |4| raw:: html

  <span style="background:#8c968a;">&#160;Sample&#160;</style>

.. |5| raw:: html

  <span style="background:#669900;">&#160;Sample&#160;</style>

.. |6| raw:: html

  <span style="background:#667366;">&#160;Sample&#160;</style>

.. |7| raw:: html

  <span style="background:#404d40;color:white;">&#160;Sample&#160;</style>

.. |8| raw:: html

  <span style="background:#3b6600;color:white;">&#160;Sample&#160;</style>

Authors
=======

Mike Harding from `Cactus Lab`_ performed the design work, based on colours
from a tissue box that Dan_ likes. The CSS coding and egg creation, was by
`Michael JasonSmith`_.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.skin.green/
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/
.. _Dan: http://groupserver.org/p/danr/
.. _Cactus Lab: http://cactuslab.com/
