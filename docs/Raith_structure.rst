The Raith_structure class
=========================

.. rubric:: Class overview:  :class:`Raith_structure`

+----------------------------------+---------------------------------------+
| Properties (public)                                                      |
+==================================+=======================================+
| :attr:`Raith_structure.name`     | String specifying name of structure   |
+----------------------------------+---------------------------------------+
| :attr:`Raith_structure.elements` | Array of |RE| objects in structure    |
+----------------------------------+---------------------------------------+

+---------------------------------+------------------------------------------+
| Properties (private set access)                                            |
+=================================+==========================================+
| :attr:`Raith_structure.reflist` | Cell array of referenced structure names |
+---------------------------------+------------------------------------------+

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

.. attribute:: Raith_structure.elements

   Array of |RE| objects in structure. |RE| arrays are created using standard MATLAB notation.


Private set-access properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attribute:: Raith_structure.reflist

   Cell array of structure names referenced by :matlab:`'sref'` or :matlab:`'aref'` elements within the structure. :attr:`reflist <Raith_structure.reflist>` is automatically updated whenever :attr:`elements <Raith_structure.elements>` is amended.



Constructor
-----------

:Constructor: :matlab:`S=Raith_structure(name,elements)`
:Arguments: + **name** --  String specifying name of structure.  Maximum length is 127 characters.   Allowed characters are A--Z, a--z, 0--9, underscore (_), period (.), dollar sign ($), question mark (?), and hyphen (-). Illegal characters are replaced with underscores (with a warning issued).
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

.. method:: Raith_structure.plot([M[,scDF]])

   Plot |RS| object with default :ref:`Raith dose factor colouring <RaithDF>`. Elements are displayed as filled polygons, where applicable (:matlab:`'polygon'`; :matlab:`'path'` with non-zero :attr:`data.w <Raith_element.data>`; :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` with empty :attr:`data.w <Raith_element.data>`; :matlab:`'text'`). All elements in the structure are plotted, regardless of :attr:`data.layer <Raith_element.data>` value.

   :Arguments: + **M** -- Augmented transformation matrix to be applied to structure [optional]; see :meth:`Raith_library.trans`,   :meth:`Raith_library.rot`, :meth:`Raith_library.refl`, and :meth:`Raith_library.scale`.
               + **scDF** -- Overall multiplicative scaling factor applied to dose factors of all elements in structure [optional]

   :Returns: None

   .. note::

      Normally, :meth:`Raith_structure.plot` is called without arguments, to display the |RS| object as it would appear in the |RNS| software. The optional arguments :matlab:`M` and :matlab:`scDF` are used internally, when :meth:`Raith_structure.plot` is called by :meth:`Raith_library.plot` or :meth:`Raith_positionlist.plot`.

   Calling :meth:`Raith_structure.plot` does not change the current axis scaling; issue an :matlab:`axis equal` command to ensure that the structure is displayed in the figure correctly.

   .. rubric:: Example

   Given the |RS| object :matlab:`S` defined in the above :ref:`Constructor <RS_constructor_example>` section:

   .. code-block:: matlab

      S.plot;
      axis equal;

   .. _RS_plot:
   .. figure:: images/RS_plot.svg
      :align: center
      :width: 500

      Racetrack resonator structure plotted using the :meth:`Raith_structure.plot` method

.. method:: Raith_structure.plotedges([M[,scDF]])

.. [1] The |RNS| software is somewhat more relaxed as regards structure names than the GDSII specification (Release 3.0), which does not allow periods or hyphens and has a maximum length of 32.
