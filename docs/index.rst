Raith_GDSII MATLAB Toolbox documentation
========================================

This toolbox enables the creation of patterns for `Raith <http://www.raith.com>`_ electron-beam lithography and focused ion beam tools using `MATLAB <http://www.mathworks.com/products/matlab/>`_.  It can also be used to create standard GDSII files for arbitrary lithography appplications.

The Raith_GDSII MATLAB Toolbox is currently maintained by the `University of Alberta <https://www.ualberta.ca>`_ `nanoFAB Centre <https://www.nanofab.ualberta.ca>`_ [1]_.  Please refer to the `GitHub <https://github.com/ahryciw/Raith_GDSII>`_ repository for the source code and installation details.

Features
--------

+ Generate Raith-dialect GDSII hierarchy (.csf) and positionlist (.pls) files directly within MATLAB
+ Plot patterns in MATLAB using Raith dose factor colouration, from individual GDSII elements to entire positionlists
+ Full support for Raith curved elements (circles, ellipses, arcs)
+ Full support for Raith "fixed beam moving stage" exposure elements (paths and circles)
+ Simply connected font defined to use for text elements
+ Export pattern in plain GDSII (.gds), where Raith-specific elements are converted to polygons and paths, to use with non-Raith GDSII editors

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Table of Contents

   introduction
   quickstart
   Raith_element
   Raith_structure
   Raith_library
   Raith_positionlist
   exttech



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`


.. [1]  Versions 1.1 and earlier were developed at the (former) National Institute for Nanotechnology, a joint initiative between the University of Alberta, the Government of Canada, the Government of Alberta, and the National Research Council Canada.
