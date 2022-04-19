.. _adr-0004:

ADR 4: Use Jupyter Notebooks for |INTC|
=======================================

.. |INTC| replace:: Interactive Computing

:Author: Medardo Antonio Rodriguez
:Date: 2022-03-28

.. contents:: Contents
   :local:
   :depth: 2

Status
------

Accepted

Context
-------

`Jupyter notebooks <jupyter_>`__ provide a medium for users to define
executable documents in a recognized environment.  Markup text (Markdown_)
cells, and rich inline outputs, make `Jupyter notebooks <jupyter_>`__ suitable
candidates for testing libraries and aplications, and to produce interactive
reports.

Using MyST_ based extensions will complete a full base tool-kit.

Papermill_ can be used to parameterize notebooks at runtime to get different
results for different scenarios.  Additionally, scrapbook_ can be used to
persist data in a notebook so that it can be re-used in a later notebook.

A collection of tools aimed at scientific computing integrate nicely with
Jupyter notebooks.  See the Jupyter notebook "Help" menu to see a base list.

.. _jupyter: https://jupyter.org/
.. _markdown: https://daringfireball.net/projects/markdown/
.. _myst: https://myst-parser.readthedocs.io/
.. _papermill: https://papermill.readthedocs.io/
.. _scrapbook: https://nteract-scrapbook.readthedocs.io/


Decision
--------

This project will use Jupyter_ notebooks to enrich documentation projects with
dynamic and interactive content.


Consequences
------------

This decision will allow a lot of flexibility in testing each functionality in
this project.

Analysts and users will already be familiar with Jupyter notebooks, so the
process of prototyping tests and reports, even before automating it with
stable modules, should be relatively easy to use.
