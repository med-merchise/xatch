.. _rfc-0001:

RFC 1: Project Documentation
============================

:Author: Medardo Antonio Rodriguez
:Date: 2022-03-28

.. contents:: Contents
   :local:
   :depth: 2


Introduction
------------

.. epigraph::

   Code is more often read than written.

   -- Guido van Rossum

According to `The Merriam-Webster Dictionary <mwdict_>`__, **documentation**
is *"the instructions, comments, and information for using a particular piece
or system of computer software."*

`Wikipedia <wiki-sd_>`__ states that *"the documentation either explains how
the software operates or how to use it, and may mean different things to
people in different roles."*

The documentation is a relevant part of software projects.  Software engineers
must understand users' needs in their interactions with the product and the
role of good documentation in satisfying them.  Despite this, documentation is
at the heart of many `controversies <doc-vs-agile_>`__ about managing projects
efficiently.

The use of a `Documentation System`_ could improve the process of creating
technical_ documentation.  Perhaps `The Diátaxis framework <diataxis_>`__ is
the best reference for this purpose right now.

Depending on the target audience, various `types of documentation`_ can be
defined in software projects.  Each of these types will have implications
selecting the correct `document format`_.

In addition to the methodological decisions explained above, documentation
projects will require choosing a good `set of tools`_.

This paper also defines a set of definitions, conventions, and rules useful in
any software engineering project related to this topic.

.. _mwdict: https://www.merriam-webster.com/dictionary/documentation
.. _diataxis: https://diataxis.fr


Documentation System
--------------------

This section summarizes "The Diátaxis framework".  For complete coverage,
visit `their site <diataxis_>`__.\ [#divio]_

The framework identifies four modes of documentation:

.. list-table::
   :widths: 10 30 30
   :align: right
   :header-rows: 1
   :stub-columns: 1

   * -
     - Serve our study
     - Serve our work
   * - Practical steps
     - | Tutorials_
       | `Learning-oriented`:sub:
     - | `How-To Guides`_
       | `Task-oriented`:sub:
   * - Theoretical knowledge
     - | Explanation_
       | `Understanding-oriented`:sub:
     - | Reference_
       | `Information-oriented`:sub:

Technical documentation should be explicitly structured around these four
modes and should be kept separate and distinct from one another.

The system is `widely adopted <fw-adoption_>`__ for many documentation
projects.

`Daniele Procida <twitter-dp_>`__, the author of the framework, gave a talk
about the system at `PyCon Australia 2017 <pycon-aus-2017_>`__.  `David Laing
<dlaing_>`__ `tweeted <laing-tweet_>`__ that *"This talk is like the Grand
Unified Theory of Documentation."*

.. _twitter-dp: https://twitter.com/evildmp
.. _fw-adoption: https://diataxis.fr/adoption/#adoption
.. _pycon-aus-2017: https://www.youtube.com/watch?v=t4vKPhjcMZg
.. _dlaing: https://davidklaing.com
.. _laing-tweet: https://twitter.com/davidklaing/status/1278130377228337154

Tutorials
~~~~~~~~~

`Tutorials <fw-tutorials_>`__ are **learning-oriented** lessons that take the
reader by the hand through a series of steps to complete a project of some
kind.  A tutorial turns new students into users.

.. _fw-tutorials: https://diataxis.fr/tutorials/

How-To Guides
~~~~~~~~~~~~~

`How-To Guides <fw-how-to-guides_>`__ are **goal-oriented** directions that
take the reader through the steps required to solve a real-world problem.

.. _fw-how-to-guides: https://diataxis.fr/how-to-guides/

Reference
~~~~~~~~~

`Reference Guides <fw-Reference_>`__ are **information-oriented** technical
descriptions of the machinery and how to operate it.  Reference material
should be austere and to the point.  It is common to use `documentation
generators <compare-doc-gen_>`__ to produce this kind of documentation based
on the source code.

.. _fw-Reference: https://diataxis.fr/reference/

Explanation
~~~~~~~~~~~

`Explanation <fw-explanation_>`__ is discussion that clarifies and illuminates
a particular topic.  They are **understanding-oriented**.

.. _fw-explanation: https://diataxis.fr/explanation/


Types of Documentation
----------------------

Each stage of a project development has different needs for documentation
audiences.  Therefore, it will be necessary to define different types of
documentation depending on who the recipients are.  See these types below
according to the Wikipedia page `Software documentation <wiki-sd_>`__:

- Requirements_.
- `Architecture/Design`_.
- Technical_.
- End-user_.
- Marketing_.

.. _wiki-sd: https://en.wikipedia.org/wiki/Software_documentation

Requirements
~~~~~~~~~~~~

A `requirement <wiki-req-def_>`__ is a single, documented need that a
particular product aims to satisfy.

`Requirements documentation <wiki-req-doc_>`__ is the description of what a
particular piece of software does or shall do.  Requirements are produced and
consumed by everyone involved in the project, including developers, project
managers, end-users, etc.

There are several `types of requirements <wiki-req-types_>`__: architectural,
functional, design, etc.

.. _wiki-req-def: https://en.wikipedia.org/wiki/Requirement
.. _wiki-req-doc: https://en.wikipedia.org/wiki/Software_documentation#Requirements_documentation
.. _wiki-req-types: https://en.wikipedia.org/wiki/Requirements_analysis#Types_of_Requirements

Architecture/Design
~~~~~~~~~~~~~~~~~~~

`Software architecture description <wiki-arch-desc_>`__ is the set of
practices for expressing, communicating and analysing software architectures,
and the result of applying such practices through a work product expressing a
software architecture.

`According to Wikipedia <wiki-togaf_>`__, |TOGAF|_ is the most widely used
framework for enterprise architecture.  We will use some of their approaches
to document our projects.

.. |TOGAF| replace:: `TOGAF (The Open Group Architecture Framework)`

.. _wiki-arch-desc: https://en.wikipedia.org/wiki/Software_architecture_description
.. _TOGAF: https://www.opengroup.org/togaf
.. _wiki-togaf: https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework

Technical
~~~~~~~~~

`Technical documentation <wiki-tech-doc_>`__ describes the use, functionality,
or architecture of a product, system, or service.

This kind of `documentation <wiki-stech_>`__ may be used by developers,
testers, and also `end-users <end-user_>`__.  `How-To Guides`_ and Reference_
Guides are frequent in this type of documentation.

Literate Programming
++++++++++++++++++++

Technical documentation is usually embedded along with the source code.  This
concept was first introduced in 1984 by respected computer scientist Donald
Knuth with his `Literate programming <literate_>`__ paradigm.  His main
intention was to treat computer programs as literature understandable to human
beings.

.. epigraph::

   I believe that the time is ripe for significantly better documentation of
   programs, and that we can best achieve this by considering programs to be
   works of literature.  Hence, my title: "Literate Programming."

   -- Donald Knuth

.. _wiki-tech-doc: https://en.wikipedia.org/wiki/Technical_documentation
.. _wiki-stech: https://en.wikipedia.org/wiki/Software_documentation#Technical_documentation
.. _literate: http://www.literateprogramming.com/

End-user
~~~~~~~~

`User documents <user-doc_>`__ simply describe how a program is used.  In the
case of a software library, code documents and user documents might indeed be
equivalent, but for a general application, this is often not true.

Tutorials_ and `How-To Guides`_ are common modes for this type.

.. _user-doc: https://en.wikipedia.org/wiki/Software_documentation#User_documentation

Marketing
~~~~~~~~~

`Marketing documentation <wiki-marketing_>`__ are promotional materials to
encourage the potential user about the product.  They inform about what the
product does so that the users' expectations are in line with what they will
be receiving.

.. _wiki-marketing: https://en.wikipedia.org/wiki/Software_documentation#Marketing_documentation


.. _`document format`:

Document Formats
----------------

We have previously introduced two main concepts: the use of a `Documentation
System`_ with four relevant modes; and the use of different `types of
documentation`_ depending on the target audiences.

The analysis of these concepts will impose the use of standards or rules when
selecting the document format.

In the computer age, a document_ usually is denoted for a text file, including
its structure and format.  The main formats for us are: Markdown_, and |RST|_.
Illustrations_ or images are used to complement or make the documentation
clearer (see also Infographic_).

A document usually contains metadata_ providing extra information.  Common
fields could be: title, abstract, authors, date of creation, and keywords.

Projects related to scientific and/or interactive computing, can also consider
to use `Jupyter Notebooks <jupyter_>`__ as an additional kind of file to use.

.. |RST| replace:: `reStructuredText (RST)`

.. _document: https://en.wikipedia.org/wiki/Document
.. _markdown: https://daringfireball.net/projects/markdown/
.. _rst: https://docutils.sourceforge.io/rst.html
.. _illustrations: https://en.wikipedia.org/wiki/Illustration#Technical_and_scientific_illustration
.. _infographic: https://en.wikipedia.org/wiki/Infographic
.. _metadata: https://en.wikipedia.org/wiki/Metadata
.. _python: https://www.python.org/
.. _jupyter: https://jupyter.org/

Semantic Structure
~~~~~~~~~~~~~~~~~~

Many document formats can be formalized depending on their semantic
structure.  For example, at a generic level:

- .. _decisions:

  |ADRs|: An `ADR <adr-github_>`__ captures a single software design choice;
  the collection of ADRs created and maintained on a project constitutes its
  decision log.  `Michael Nygard's post <adr-nygard_>`__ "Documenting
  Architecture Decisions" has become a sort of de-facto standard for writing
  architecture decisions for agile projects.

- .. _`reasons for decisions`:

  |RFC|: An RFC contains technical specifications and organizational notes
  focused on the process of discussing architectural design ideas.\ [#inet]_,
  see `Bruno Scheufler' post <rfc-scheufler_>`__ for more information.

- |SDD|: An `SDD <sdd-ieee_>`__ is a representation of a software design to be
  used for communicating design information to its stakeholders.

  Jelvix_ has a good video (`Software Design Document | How To write it step
  by step <jelvix-video_>`__) about this kind of documents.  You can find the
  same information on their blog post `The Anatomy of a Software Design
  Document <jelvix-blog_>`__.

  See also `the Wikipedia page <sdd-wiki_>`__.

.. |ADRs| replace:: `Architecture Decision Records (ADRs)`
.. |RFC| replace:: `Request for Comments (RFC)`
.. |SDD| replace:: `Software Design Document (SDD)`

.. _adr-nygard: http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions
.. _rfc-scheufler: https://brunoscheufler.com/blog/2020-07-04-documenting-design-decisions-using-rfcs-and-adrs#-rfcs-discuss-technical-ideas-as-a-team
.. _adr-github: https://adr.github.io/
.. _sdd-ieee: https://ieeexplore.ieee.org/document/5167255
.. _jelvix: https://jelvix.com/
.. _jelvix-video: https://www.youtube.com/watch?v=6QsSuQPxunk
.. _jelvix-blog: https://jelvix.com/blog/software-design-document
.. _sdd-wiki: https://en.wikipedia.org/wiki/Software_design_description

File name format
~~~~~~~~~~~~~~~~

For certain types, it is also convenient to formalize the names of the
files. For example, following the pattern "``type-NNNN-title.suffix``"; where:

- The ``type`` could be, ``adr``, ``rfc``, ...
- ``NNNN`` is a consecutive number (unique within each ``type``)\ [#numeric]_,
  and we assume that there will be no more than 9999 per ``type`` in a
  repository.
- The ``title`` is stored using dashes (no spaces) and lowercase.
- The ``suffix`` is the filename extension; it could be ``md`` for Markdown_,
  ``rst`` for |RST|_, ``ipynb`` for `Jupyter Notebooks <jupyter_>`__, ...


.. _`set of tools`:
.. _`rfc-1:documentation-tools`:

Documentation Tools
-------------------

There are many other documentation generators; see some `comparative tables
<compare-doc-gen_>`__.

We propose Sphinx_ to manage documentation projects.  Sphinx is a powerful
`documentation generator <wiki-doc-gen_>`__ with many great features for
writing technical_ documentation.

Sphinx was originally created for the `new Python documentation
<python-docs_>`__ but now supports several other languages.  There are
currently `many projects using Sphinx <sphinx-projects_>`__.

Sphinx_ has a great collection of `extensions <sphinx-ext_>`__ available.
Some of them are generic, applicable to any documentation project.  Others are
specific to Python projects only.

Built-in extension autodoc_ is maybe the most relevant; you can use it to
include documentation from Python docstrings_.  You can supplement this
process with Python 3 type annotations using autodoc-typehints_.

With Sphinx, you can use |RST|_ to write documentation.  Using |MyST|_
extensions, you can combine native RST, with Markdown_, and `Jupyter Notebooks
<jupyter_>`__ in the same documentation project.  To do this, configure the
myst-parser_ and myst-nb_.  Jupyter_ has support for various programming
languages, including Python_, where it all started.

There are some other tools from `"The Executable Books Project"
<exe-book_>`__: an international collaboration to build open-source tools that
facilitate the publication of computational narratives using the Jupyter_
ecosystem.  For example, `Jupyter Book <jbook_>`__ supports MyST to easily
create beautiful, publication-quality books and documents from computational
material.

The `"Documentation Tools" page <py-doc-tools_>`__ contains several references
to tools that help generate documentation for software written in Python.
Special mention to Pandoc_ (your swiss-army knife): can convert files from one
markup format to another.

A `template processor <tprocessor_>`__ is a software that "evaluate" templates
with data to produce result documents.  Sphinx_ uses the Jinja_ engine for its
HTML templates.

With `Read the Docs <https://readthedocs.org>`_ you can host your Sphinx
documentation for free, forever.

A new generation of tools uses AI techniques using large application
repositories to generate (or get suggestions) of source code and
documentation.  See, for example, `GitHub Copilot <copilot_>`__.

.. |MyST| replace:: `MyST (Markedly Structured Text)`

.. _sphinx: https://www.sphinx-doc.org/
.. _wiki-doc-gen: https://en.wikipedia.org/wiki/Documentation_generator
.. _compare-doc-gen: https://en.wikipedia.org/wiki/Comparison_of_documentation_generators
.. _python-docs: https://docs.python.org/
.. _sphinx-projects: https://www.sphinx-doc.org/en/master/examples.html
.. _myst: https://myst-parser.readthedocs.io/
.. _myst-parser: https://github.com/executablebooks/MyST-Parser
.. _myst-nb: https://github.com/executablebooks/MyST-NB
.. _exe-book: https://executablebooks.org/
.. _jbook: https://jupyterbook.org/
.. _sphinx-ext: https://www.sphinx-doc.org/en/master/usage/extensions/index.html
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _autodoc-typehints: https://github.com/agronholm/sphinx-autodoc-typehints
.. _docstrings: https://peps.python.org/pep-0257/
.. _py-doc-tools: https://wiki.python.org/moin/DocumentationTools
.. _pandoc: https://pandoc.org/
.. _tprocessor: https://en.wikipedia.org/wiki/Template_processor
.. _jinja: https://jinja.palletsprojects.com/
.. _copilot: https://copilot.github.com


.. _doc-vs-agile:

Documentation and agile development controversy
-----------------------------------------------

On `Wikipedia <wiki-controversy_>`__, they cite:

.. epigraph::

   The resistance to documentation among developers is well known and needs no
   emphasis.

   -- Herbsleb, James D. and Moitra, Dependra.

It is true that agile methodologies avoid any unnecessary activity that "does
not add" value directly.  One of the `principles <aprinciples_>`__ of
`"Manifesto for Agile Software Development" <amanifesto_>`__ expresses:
*Working software is the primary measure of progress.*

Many developers justify themselves by wrongly using the `value
<amanifesto_>`__: *Working software over comprehensive documentation*.

Which could be cynically interpreted as\ [#wiki-cite]_:

.. epigraph::

   We want to spend all our time coding.  Remember, real programmers don't
   write documentation.

   -- Rakitin, Steven.

The purpose is to try to avoid responsibilities in the work of writing
documentation.  But on the `"Manifesto for Agile Software Development"
<amanifesto_>`__ site, they also say: *That is, while there is value in
the items on the right, we value the items on the left more.*

So, in `agile software development <agile_>`__ documenting is still important.
Decisions_ and `reasons for decisions`_ must be an essential strategy to
express an architecture.

.. _wiki-controversy: https://en.wikipedia.org/wiki/Software_documentation#Documentation_and_agile_development_controversy
.. _amanifesto: https://agilemanifesto.org/
.. _aprinciples: https://agilemanifesto.org/principles.html
.. _agile: https://en.wikipedia.org/wiki/Agile_software_development


---

.. rubric:: Footnotes

.. [#divio] Other version of the framework can also be found on `Divio's site
            <divio-site_>`__.

.. [#numeric] This numeric order must be considered a `serial number`_.  Some
              projects use human authorities for assigning consecutive unique
              numbers.  Sphinx_ users could use content identifiers to check
              identity or uniqueness.

.. [#inet] We use in this article some terms that should not be confused with
           `Internet Standards <inet-stds_>`__; they have assumed some
           acronyms to identify their document types, for example, `RFC
           <rfc-inet_>`__ and FYI.

.. [#wiki-cite] This is also a `Wikipedia <wiki-controversy_>`__ cite.

.. _divio-site: https://documentation.divio.com/
.. _`serial number`: https://en.wikipedia.org/wiki/Serial_number
.. _inet-stds: https://en.wikipedia.org/wiki/Internet_Standard
.. _rfc-inet: https://en.wikipedia.org/wiki/Request_for_Comments
