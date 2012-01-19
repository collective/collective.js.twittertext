Introduction
============

Add twitter-text.js_ to Plone javascript registry. 

This addon doesn't provide new feature.

Version 1.4.14
Licence: twitter-text.js_ is under `Apache Licence <http://www.apache.org/licenses/LICENSE-2.0>`

About twitter-text
==================

A JavaScript utility that provides text processing routines for Tweets.
This library conforms to a common test suite shared by many other
implementations, particularly twitter-text.gem (Ruby). The library provides
autolinking and extraction for URLs, usernames, lists, and hashtags.

How to use use twitter-text
===========================

twitter text is available as twttr.txt namespace.

Example::

  $('#content').html(twttr.txt.autoLink($('#content').html()))

Credits
=======

Companies
---------

|makinacom|_

  * `Planet Makina Corpus <http://www.makina-corpus.org>`_
  * `Contact us <mailto:python@makina-corpus.org>`_

Authors

  - JeanMichel FRANCOIS aka toutpt <toutpt@gmail.com>

.. Contributors


.. |makinacom| image:: http://depot.makina-corpus.org/public/logo.gif
.. _makinacom:  http://www.makina-corpus.com
.. _twitter-text.js: https://github.com/twitter/twitter-text-js
