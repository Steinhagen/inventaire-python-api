.. Inventaire API documentation master file, created by
   sphinx-quickstart on Wed May 17 21:27:13 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Inventaire Python API's documentation!
=============================================

This package makes it easy to use Inventaire with Python. You can write simple scripts to manage your library and keep your database up to date automatically.

The idea of the package is to have two parts in it: a set of low-level wrappers and Inventaire objects (like entities or users).
The low-level wrappers simply perform requests to the API endpoints.
The objects should provide OOP approach and leverage the low-level wrappers. Currently the Inventaire objects are not implemented.


.. toctree::
   :maxdepth: 3
   :caption: Contents:

   installation
   examples
   troubleshooting
   inventaire

Limitations
***********

The wrappers only implement public API methods from the official Inventaire API website.

Useful links
************

`Inventaire docs <https://api.inventaire.io/>`_

