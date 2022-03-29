.. _adr-0003:

ADR 3: Use Sphinx_ as |DOC_GEN|_
================================

.. |DOC_GEN| replace:: documentation generator

:Author: Medardo Antonio Rodriguez
:Date: 2022-03-28

.. contents:: Contents
   :local:
   :depth: 2

.. _sphinx: https://www.sphinx-doc.org/
.. _doc_gen: https://en.wikipedia.org/wiki/Documentation_generator

Status
------

Accepted

Context
-------

We need a way to produce and host documentation for our projects.

Decision
--------

Documentation authoring will be done via Sphinx_, plus MyST_ extensions to
combine RST, Markdown, and Jupyter Notebooks.

Extra extensions will be configured to generate reference documentation,
including:

- autodoc_: include documentation from Python ``docstrings``.
- autodoc-typehints_: to use type annotations for documenting argument types
  and return value types of functions.

See RFC-1 section ` Documentation Tools <rfc-1:documentation-tools>`:ref: for
more information.

.. _myst: https://myst-parser.readthedocs.io/
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _autodoc-typehints: https://github.com/agronholm/sphinx-autodoc-typehints
.. _myst: https://myst-parser.readthedocs.io/

Consequences
------------

You can also use Markdown format (``.md``) for documentation, which is used by
general developers more than the ``.rst`` format.

You can read the documentation in the terminal.

Automatic generation of reference documentation makes projects more
maintainable and consistent with actual code.

You can include documentation building in custom |CI|_ workflows and fail on
errors or warnings.

You can use tools like Pandoc_ to convert a documentation project, or a
particular document, to HTML or PDF.

The documentation will be well-formatted and hyperlinked, enabling it to be
browser-ready for project hosting sites like GitHub and Bitbucket.

You can use `Read the Docs <https://readthedocs.org>`_ to host your
documentation.

.. |CI| replace:: `Continuous Integration (CI)`

.. _ci: https://en.wikipedia.org/wiki/Continuous_integration
.. _pandoc: http://pandoc.org
