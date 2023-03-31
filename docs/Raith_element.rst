The Raith_element class
=======================

.. rubric:: Class overview:  :class:`Raith_element`

+---------------------+
| Properties (public) |
+=====================+
|                     |
+---------------------+

+---------+
| Methods |
+=========+
|         |
+---------+

.. class:: Raith_element

|RE| objects define low-level, unnamed patterns, collections of which are bundled together to form named structures in the GDSII library.


Properties
----------

.. attribute:: Raith_element.type

   String specifying type of element; allowed values are :matlab:`'polygon'`, :matlab:`'path'`, :matlab:`'dot'`, :matlab:`'arc'`, :matlab:`'circle'`, :matlab:`'ellipse'`, :matlab:`'text'`, :matlab:`'fbmspath'`, :matlab:`'fbmscircle'`, :matlab:`'sref'`, or :matlab:`'aref'`.

.. attribute:: Raith_element.data

   Structure array containing additional record data for element; allowed field names and typing of values are determined by the element type (see :numref:`§%s <Raith_element:Constructors>`).


Constructors
------------

.. code-block:: matlab

   E=Raith_element('polygon',layer,uv,DF)
   E=Raith_element('path',layer,uv,w,DF)
   E=Raith_element('dot',layer,uv,DF)
   E=Raith_element('arc',layer,uv_c,r,theta,angle,w,N,DF)
   E=Raith_element('circle',layer,uv_c,r,w,N,DF)
   E=Raith_element('ellipse',layer,uv_c,r,w,angle,N,DF)
   E=Raith_element('text',layer,uv_0,h,angle,uv_align,textlabel,DF)
   E=Raith_element('fbmspath',layer,uv,cvtr,w,DF)
   E=Raith_element('fbmscircle',layer,uv_c,r,w,DF)
   E=Raith_element('sref',name,uv_0[,mag[,angle[,reflect]]])
   E=Raith_element('aref',name,uv_0,n_colrow,a_colrow[,mag[,angle[,reflect]]])


The above constructors may be used to create |RE| objects. The first argument sets the element :attr:`type <Raith_element.type>` property, followed by a list of arguments comprising the fields of the :attr:`data <Raith_element.data>` property (a MATLAB structure array), which vary depend on the :attr:`type <Raith_element.type>`. Agruments shown in brackets are optional.
Alternately, an empty, argumentless |RE| object may be called, with the :attr:`type <Raith_element.type>` and :attr:`data <Raith_element.data>` properties assigned afterward. For example:

.. code-block:: matlab

   E=Raith_element;
   E.type='polygon';
   E.data.layer=0;
   E.data.uv=[0 1 1 0 0;0 0 1 1 0];
   E.data.DF=1.5;

The above is equivalent to

.. code-block:: matlab

   E=Raith_element('polygon',0,[0 1 1 0 0;0 0 1 1 0],1.5);

By default, all properties are checked for correctness (typing, allowed values, size) before being assigned, whether the |RE| object is created with a constructor or its properties are amended individually; this behaviour can be disabled if necessary (see :numref:`§%s <exttech:disabling data checking>`).

Descriptions of the eleven |RE| types are given in the following subsections.


Polygon element
^^^^^^^^^^^^^^^

:Description: Closed, filled polygon
:Constructor: :matlab:`E=Raith_element('polygon',layer,uv,DF)`
:Properties: + **type** --  :matlab:`'polygon'` (string)
             + **data.layer** -- GDSII layer (integer); allowed values are 0--63
             + **data.uv** -- 2 × *n* matrix [*u*;*v*] of polygon vertices (µm)
             + **data.DF** -- Dose factor for polygon

.. note::

   If the first and last vertices in :attr:`data.uv <Raith_element.data>` are not the same (i.e., an open polygon), :attr:`data.uv <Raith_element.data>` is amended to close the polygon and a warning is issued.

.. rubric:: Example
.. code-block:: matlab

   E=Raith_element('polygon',0,[0 2 2 1 1 0 0; ...
                                0 0 1 1 2 2 0],1.3);

.. _polygon_element:
.. figure:: images/polygon_element.svg
   :align: center
   :width: 500

   Example :matlab:`'polygon'` element

Array reference element
^^^^^^^^^^^^^^^^^^^^^^^

:Description:  An array reference!
