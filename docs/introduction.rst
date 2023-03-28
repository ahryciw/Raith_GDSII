Introduction
============

The Raith_GDSII toolbox provides a simple, versatile, and scriptable means of generating patterns for `Raith <http://www.raith.com>`_  electron-beam lithography (EBL) and focused ion beam (FIB) tools using `MATLAB <http://www.mathworks.com/products/matlab/>`_.  It can also be used to generate standard GDSII files for photomask fabrication or direct-write laser lithography applications.

Although relatively simple structures may be generated directly within the Raith Nanosuite software via the GDSII editing tools in the *Design* panel, this interface becomes cumbersome for complicated structures comprising many elements, or for arrays of structures with subtle variations in geometry.  GDSII files can be scripted using third-party libraries [1]_, but beam dose information and Raith curved elements (arcs, circles, and ellipses) are generally not supported [2]_.  Scripted generation of patterns using the ASCII-based .asc or .elm formats is possible [3]_, but these files must be manually loaded into a GDSII hierarchy file in the Raith software; the GDSII file is backed up after *each* .asc/.elm file is added to the library, which can yield unacceptably long load-times if there are many structures to add.

To circumvent these issues, the Raith_GDSII toolbox may be used to generate both the GDSII hierarchy and positionlist files directly within MATLAB, with full support for Raith curved elements.  The relevant objects may be manipulated using standard MATLAB functionality, making scripting easy.  Furthermore, structures may be plotted using the standard Raith dose factor colourmap---from individual low-level elements to entire positionlists---to aid in visualisation and error-checking during the pattern design process.

The Raith_GDSII classes
-----------------------

There are four MATLAB classes in the Raith_GDSII toolbox:  :class:`Raith_element`, :class:`Raith_structure`, :class:`Raith_library`, and :class:`Raith_positionlist`. The first three classes reflect the structure of the GDSII stream format and are used to generate the GDSII library containing the structures referenced in the positionlist:


.. [1] E.g., `Gdspy <https://github.com/heitzmann/gdspy>`_, `libgds <https://github.com/scholi/libgds>`_, and `python-gdsii <https://pypi.org/project/python-gdsii>`_.

.. [2] The `libgds <https://github.com/scholi/libgds>`_ Python library does in fact encode the dose factor, but does not truly support Raith curved elements, instead implementing them as polygons or paths.

.. [3] See §5.1.3 (Edit Menu) of the *Raith Software Reference Manual*, Version 5.0.
