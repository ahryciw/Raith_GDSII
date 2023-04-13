The Raith_library class
=======================

.. rubric:: Class overview:  :class:`Raith_library`

+----------------------------------+--------------------------------------------------+
| Properties (public)                                                                 |
+==================================+==================================================+
| :attr:`Raith_library.name`       | Character array specifying name of GDSII library |
+----------------------------------+--------------------------------------------------+
| :attr:`Raith_library.structures` | Array of |RS| objects in library                 |
+----------------------------------+--------------------------------------------------+

+----------------------------------+----------------------------------------------+
| Properties (private set access)                                                 |
+==================================+==============================================+
| :attr:`Raith_library.structlist` | Cell array of all structure names in library |
+----------------------------------+----------------------------------------------+

+---------------------------------+--------------------------------------------------+
| Methods                                                                            |
+=================================+==================================================+
| :meth:`Raith_library.append`    | Append |RS| object(s) to library                 |
+---------------------------------+--------------------------------------------------+
| :meth:`Raith_library.writegds`  | Output Raith GDSII hierarchy (.csf/.gds) file    |
+---------------------------------+--------------------------------------------------+
| :meth:`Raith_library.plot`      | Plot structure in library as filled polygons     |
+---------------------------------+--------------------------------------------------+
| :meth:`Raith_library.plotedges` | Plot structure in library as unfilled polygons   |
+---------------------------------+--------------------------------------------------+

+----------------------------------------+-------------------------------------------------------+
| Static Methods                                                                                 |
+========================================+=======================================================+
| :meth:`Raith_library.trans`            | Return augmented matrix for translation               |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.rot`              | Return augmented matrix for rotation                  |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.refl`             | Return augmented matrix for reflection about *u*-axis |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.scale`            | Return augmented matrix for uniform scaling           |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.writerec`         | Write GDSII record to file                            |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.writehead`        | Write GDSII library header records                    |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.writeelement`     | Write GDSII element record(s)                         |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.writebeginstruct` | Write GDSII records to begin a structure              |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.writeendstruct`   | Write GDSII records to end a structure                |
+----------------------------------------+-------------------------------------------------------+
| :meth:`Raith_library.writeendlib`      | Write GDSII records to end a library                  |
+----------------------------------------+-------------------------------------------------------+

.. class:: Raith_library

|RL| objects define GDSII hierarchies containing collections of structures (|RS| objects) which may be referred to in positionlist entries. By default, the :meth:`Raith_library.writegds` method outputs a "Raith-dialect" GDSII (.csf) file which can be used by the |RNS| beamwriting software without any additional modification; a standard GDSII (.gds) file readable by non-Raith GDSII viewers/editors can be output instead if the :matlab:`'plain'` dialect option is selected.  Additionally, if all referenced structures are contained in the library, the full hierarchy of structures containing :matlab:`'sref'` or :matlab:`'aref'` elements may be displayed using the :meth:`Raith_library.plot` and :meth:`Raith_library.plotedges` methods.



Properties
----------


Public properties
^^^^^^^^^^^^^^^^^

.. attribute:: Raith_library.name

   Character array specifying name of GDSII library, not including .csf/.gds extension.

.. attribute:: Raith_library.structures

   Array of |RS| objects in library. |RS| objects may be added to :attr:`structures <Raith_library.structures>` either using standard MATLAB notation, or via the :meth:`Raith_library.append` method.


Private set-access properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: Raith_library.structlist

   Ordered cell array of all names of structures (character arrays) found in library. :attr:`structlist <Raith_library.structlist>` is automatically updated whenever :attr:`structures <Raith_library.structures>` is amended.



Constructor
-----------

:Constructor: :matlab:`L=Raith_library(name,structures)`
:Arguments: + **name** --  Character array specifying name of structure.  Maximum length is 127 characters.   Allowed characters are A--Z, a--z, 0--9, underscore (_), period (.), dollar sign ($), question mark (?), and hyphen (-). Illegal characters are replaced with underscores (with a warning issued).
            + **elements** -- Array of |RE| objects in structure.  |RE| arrays are created using standard MATLAB notation (see following **Example**).

.. rubric:: Example
.. _RS_constructor_example:
.. code-block:: matlab

   % Optical racetrack resonator
   E(1)=Raith_element('arc',0,[2 0],3,[-90 90],0,0.3,200,1.3);
   E(2)=Raith_element('arc',0,[-2 0],3,[90 270],0,0.3,200,1.3);
   E(3)=Raith_element('path',0,[-2 2;3 3],0.3,1.3);
   E(4)=Raith_element('path',0,[-2 2;-3 -3],0.3,1.3);
   S=Raith_structure('racetrack',E);



Methods
-------

.. method:: Raith_library.append()

.. method:: Raith_library.writegds()

.. method:: Raith_library.plot([M[,scDF]])

.. method:: Raith_library.plotedges([M[,scDF]])

.. staticmethod:: Raith_library.trans()

.. staticmethod:: Raith_library.rot()

.. staticmethod:: Raith_library.refl()

.. staticmethod:: Raith_library.scale()

.. staticmethod:: Raith_library.writerec()

.. staticmethod:: Raith_library.writehead()

.. staticmethod:: Raith_library.writeelement()

.. staticmethod:: Raith_library.writebeginstruct()

.. staticmethod:: Raith_library.writeendstruct()

.. staticmethod:: Raith_library.writeendlib()

.. staticmethod:: Raith_library.writerec()

.. staticmethod:: Raith_library.writerec()

.. staticmethod:: Raith_library.writerec()
