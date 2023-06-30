Introduction
============

The |RG| toolbox provides a simple, versatile, and scriptable means of generating patterns for `Raith <http://www.raith.com>`_  electron-beam lithography (EBL) and focused ion beam (FIB) tools using `MATLAB <http://www.mathworks.com/products/matlab/>`_.  It can also be used to generate standard GDSII files for photomask fabrication or direct-write laser lithography applications.

Although relatively simple structures may be generated directly within the |RNS| software via the GDSII editing tools in the *Design* panel, this interface becomes cumbersome for complicated structures comprising many elements, or for arrays of structures with subtle variations in geometry.  GDSII files can be scripted using third-party libraries,\ [1]_ but beam dose information and Raith-specific elements (e.g., curved elements such as arcs, circles, ellipses; |FBMS| paths and circles) are generally not supported.\ [2]_  Scripted generation of patterns using the ASCII-based .asc or .elm formats is possible,\ [3]_ but these files must be manually loaded into a GDSII hierarchy file in the Raith software; the GDSII file is backed up after *each* .asc/.elm file is added to the library, which can yield unacceptably long load-times if there are many structures to add.

To circumvent these issues, the |RG| toolbox may be used to generate both the GDSII hierarchy and positionlist files directly within MATLAB, with full support for Raith curved and |FBMS| elements.  The relevant objects may be manipulated using standard MATLAB functionality, making scripting easy.  Furthermore, patterns may be plotted using the standard Raith dose factor colourmap---from individual low-level elements to entire positionlists---to aid in visualisation and error-checking during the design process.

The Raith_GDSII classes
-----------------------

There are four MATLAB classes in the |RG| toolbox:  |RE|, |RS|, |RL|, and |RP|. The first three classes reflect the structure of the GDSII stream format and are used to generate the GDSII library containing the structures referenced in the positionlist:

|RE|
   Used to define unnamed, low-level GDSII pattern elements.  The following element types are supported:

   :polygon:  A closed, filled polygon.  :matlab:`'polygon'` elements are fractured into trapezoids by the |RNS| software before writing.
   :path:  A path of connected line segments. :matlab:`'path'` elements may be either single-pixel lines or have a non-zero width.
   :dot:  A single-pixel dot, or series thereof.
   :arc:  A segment of a circular or elliptical path (Raith curved element). :matlab:`'arc'` elements may be single-pixel lines, have a non-zero width, or be filled (i.e., a circular or elliptical segment).
   :circle: A circle or disc (Raith curved element). :matlab:`'circle'` elements may be single-pixel lines, have a non-zero width, or be filled (i.e., a disc).
   :ellipse: An ellipse or elliptical disc (Raith curved element). :matlab:`'ellipse'` elements may be single-pixel lines, have a non-zero width, or be filled (i.e., an elliptical disc).
   :text: A line of text rendered as simple polygons.\ [4]_
   :fbmspath: A path of connected line segments and/or circular arcs, exposed using the Raith "fixed beam moving stage" (FBMS) mode, also known as *traxx*. :matlab:`'fbmspath'` elements may be either single-pixel lines or have a non-zero width.
   :fbmscircle: A circle exposed using |FBMS| mode. :matlab:`'fbmscircle'` elements may be either single-pixel lines or have a non-zero width.
   :sref: A structure reference. :matlab:`'sref'` elements refer to named |RS| objects, and may optionally apply transformations (magnification, rotation, reflection across the *u* axis).\ [5]_
   :aref: An array reference. :matlab:`'aref'` elements generate a rectangular array of named |RS| objects, and may optionally apply transformations (magnification, rotation, reflection across the *u* axis).\ [5]_ [6]_

   Elements of type :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` are implemented as Raith curved elements:  exposure is via a curved beam path which in general consists of concentric ellipses, rather than being fractured into trapezoids.

|RS|
   Used to define named structures, comprising collections of |RE| objects.

|RL|
   Used to define a GDSII library, comprising a collection of uniquely named |RS| objects, and to write a Raith-readable GDSII hierarchy (.csf) file. Exporting to standard GDSII format (.gds), readable by non-Raith GDSII viewers/editors, is also supported.

|RP|
   Used to define a positionlist, comprising chip-level references to |RS| objects in a |RL|, and to write a Raith-readable positionlist (.pls) file.


Software use and bug reporting
------------------------------

Use of the |RG| toolbox is subject to the terms of the `Mozilla Public License, v. 2.0 <https://www.mozilla.org/en-US/MPL/2.0/>`_.

The latest version of the |RG| toolbox may be downloaded from its `GitHub repository <https://github.com/ahryciw/Raith_GDSII>`_.

Please send comments, bug reports, and future update suggestions to Aaron Hryciw at `ahryciw@ualberta.ca <mailto:ahryciw@ualberta.ca>`_.


Citing Raith_GDSII
------------------

Please cite the |RG| MATLAB toolbox in any publication for which you found it useful by including the text "The Raith_GDSII MATLAB toolbox is maintained at the University of Alberta nanoFAB Centre; it is available at github.com/ahryciw/Raith_GDSII." in a footnote or endnote, as appropriate.


Installation
------------

To install the |RG| toolbox, simply place the four |RG| class definitions in the ``src`` directory (:file:`Raith_element.m`, :file:`Raith_structure.m`, :file:`Raith_library.m`, and :file:`Raith_positionlist.m`) in a folder on your MATLAB path.  A full description of the these classes is contained in §§ :doc:`3<Raith_element>`--:doc:`6<Raith_positionlist>`. To get started, however, the following section outlines a typical (albeit brief) workflow.


.. [1] E.g., `Gdspy <https://github.com/heitzmann/gdspy>`_, `libgds <https://github.com/scholi/libgds>`_, and `python-gdsii <https://pypi.org/project/python-gdsii>`_.

.. [2] The `libgds <https://github.com/scholi/libgds>`_ Python library does in fact encode the dose factor, but does not truly support Raith curved elements, instead implementing them as polygons or paths.

.. [3] See §4.1 (Importing files in ASCII format) of the *NanoSuite Software Reference Manual*, Release 6.0.

.. [4] Using `simple polygons <https://en.wikipedia.org/wiki/Simple_polygon>`_ for text shapes prevents the interiors of letters (e.g., A, B, D) from being released if there is a subsequent undercut etch step.

.. [5] The little-used *absolute magnification* and *absolute rotation* transformations in the GDSII specification are not supported by the |RG| toolbox.

.. [6]  The Raith software’s interpretation of :matlab:`'aref'` objects differs somewhat from the GDSII specification. See :numref:`§%s <Raith_element:Array reference element>`.
