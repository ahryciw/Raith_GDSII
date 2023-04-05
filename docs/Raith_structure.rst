The Raith_structure class
=========================

.. rubric:: Class overview:  :class:`Raith_structure`

+---------------------+
| Properties (public) |
+=====================+
|                     |
+---------------------+

+---------------------------------+
| Properties (private set access) |
+=================================+
|                                 |
+---------------------------------+

+-----------------------------------+-------------------------------------+
| Methods                                                                 |
+===================================+=====================================+
| :meth:`Raith_structure.plot`      | Plot structure as filled polygons   |
+-----------------------------------+-------------------------------------+
| :meth:`Raith_structure.plotedges` | Plot structure as unfilled polygons |
+-----------------------------------+-------------------------------------+

.. class:: Raith_structure

|RS| objects define named structures composed of low-level elements (|RE| objects). Structures are packaged together in a GDSII hierarchy (library), and are the objects referred to in positionlist entries.


Properties
----------

Public properties
^^^^^^^^^^^^^^^^^

.. attribute:: Raith_structure.name

   String specifying name of structure.  Maximum length is 127 characters.  Allowed characters are A--Z, a--z, 0--9, underscore (_), period (.), dollar sign ($), question mark (?), and hyphen (-).\ [1]_






Methods
-------

.. method:: Raith_structure.plot([M[,scDF]]))

.. method:: Raith_structure.plotedges([M[,scDF]]))

.. [1] The |RNS| software is somewhat more relaxed as regards structure names than the GDSII specification, which does not allow periods or hyphens and has a maximum length of 32.
