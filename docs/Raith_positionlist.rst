The Raith_positionlist class
============================

.. rubric:: Class overview:  :class:`Raith_positionlist`

.. table::
   :widths: 1 2
   :width: 100%

   +-------------------------------------+-----------------------------------------+
   | Properties (public)                                                           |
   +=====================================+=========================================+
   | :attr:`Raith_positionlist.library`  | |RL| object containing all structures   |
   +-------------------------------------+-----------------------------------------+
   | :attr:`Raith_positionlist.csf_path` | Path of GDSII library on Raith computer |
   +-------------------------------------+-----------------------------------------+
   | :attr:`Raith_positionlist.WF`       | Writefield dimensions                   |
   +-------------------------------------+-----------------------------------------+
   | :attr:`Raith_positionlist.chipUV`   | Size of rectangular chip (specimen)     |
   +-------------------------------------+-----------------------------------------+
   | :attr:`Raith_positionlist.poslist`  | Struture array of positionlist entries  |
   +-------------------------------------+-----------------------------------------+


.. table::
   :widths: 1 2
   :width: 100%

   +--------------------------------------+----------------------------------------------------------+
   | Methods                                                                                         |
   +======================================+==========================================================+
   | :meth:`Raith_positionlist.append`    | Append |RS| object to positionlist                       |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.plot`      | Plot entire positionlist as filled polygons              |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.plotedges` | Plot entire positionlist as unfilled polygons            |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.plotWA`    | Plot working areas of all structures in positionlist     |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.plotWF`    | Plot first writefields of all structures in positionlist |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.centre`    | Centre current positionlist entries on chip              |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.shift`     | Shift current positionlist entries on chip               |
   +--------------------------------------+----------------------------------------------------------+
   | :meth:`Raith_positionlist.writepls`  | Output Raith positionlist (.pls) file                    |
   +--------------------------------------+----------------------------------------------------------+

.. class:: Raith_positionlist

A |RP| object defines a positionlist:  a sequential list of instructions to write a structure defined in a GDSII hierarchy at a certain position on the chip.  The :meth:`Raith_positionlist.writepls` method outputs a Raith positionlist (.pls) file which can be used by the |RNS| software without any additional modification. As an aid to chip layout, the structures, working areas, and writefields of the entire positionlist can be plotted.


Properties
----------

.. attribute:: Raith_positionlist.library

   |RL| object containing all structures to be referenced in positionlist.

.. attribute:: Raith_positionlist.csf_path

   Full path of GDSII hierarchy (.csf/.gds) file, as found on the Raith tool computer.

.. attribute:: Raith_positionlist.WF

   Writefield size; 1 × 2 vector [*size*\ :sub:`u` \ *size*\ :sub:`v`]  (μm).

.. attribute:: Raith_positionlist.chipUV

   Size of rectangular chip; 1 × 2 vector [*size*\ :sub:`u` \ *size*\ :sub:`v`]  (mm).

.. attribute:: Raith_positionlist.poslist

   Structure array of positionlist entries, containing fields **name**, **uv_c**, **DF**, **WA**, and **layers**; see :meth:`Raith_positionlist.append` for a description of these fields.


Constructor
-----------

:Constructor: :matlab:`P=Raith_positionlist(library,csf_path,WF,chipUV)`
:Arguments: + **library** --  |RL| object containing all structures to be placed in positionlist
            + **csf_path** -- Full path of GDSII hierarchy file, as found on Raith tool computer (character array)
            + **WF** -- Writefield size; 1 × 2 vector [*size*\ :sub:`u` \ *size*\ :sub:`v`]  (μm)
            + **chipUV** -- Size of rectangular chip; 1 × 2 vector [*size*\ :sub:`u` \ *size*\ :sub:`v`]  (mm)

.. note::

   By default, all properties are checked for correctness (typing, allowed values, size) before being assigned, whether the |RP| object is created with a constructor or these four properties are amended individually.

.. rubric:: Example

Given the |RS| object :matlab:`S` defined in :numref:`§%s <Raith_structure:Constructor>`:

.. _RP_constructor_example:
.. code-block:: matlab

   % Racetrack resonator defined in Raith_structure object S
   lbl=Raith_structure('radius_label',Raith_element('text',0,[0 0],2,0,[1 0],'3 um',1.5));
   L=Raith_library('resonators',[S lbl]);
   % Postionlist for a 5 mm x 5 mm chip, 100 µm writefield
   P=Raith_positionlist(L,'F:\Raith\resonators.csf',[100 100],[5 5]);


Methods
-------

.. method:: Raith_positionlist.append(name,uv_c,DF,WA[,layers])

   Append |RS| object to positionlist.

   :Arguments: + **name** -- Character array specifying |RS| object name (as found in GDSII library)
               + **uv_c** -- Centre of first writefield of structure; 1 × 2 vector [*u*\ :sub:`c` \ *v*\ :sub:`c`] (mm)
               + **DF** -- Overall dose factor scaling applied to entire structure
               + **WA** -- Working area of structure; 1 × 4 vector [*u*\ :sub:`min` \ *v*\ :sub:`min` \ *u*\ :sub:`max` \ *v*\ :sub:`max`] (µm)
               + **layers** -- Vector of layers to expose [optional]; defaults to all layers present in structure elements

   :Returns: None

   .. note::

      The units of the arguments reflect how they are stored in the positionlist: **uv_c** is in mm and **WA** is in μm. The working area coordinates are defined with respect to the origin of the |RS| object.  As in the |RNS| software, the bottom-left corners of the working area and the writefield are aligned; as such, **uv_c** specifies a point half a writefield width above and to the right of the bottom-left corner of the working area.  One design paradigm which simplifies the positioning of structures contained in a single writefield is to define them centred on the origin, then specify a working area---also centred on the origin---which is the same size as the writefield (see following **Example**). In this case, **uv_c** will correspond to the origin of the structure.

   .. rubric:: Example

   Given the |RL| and |RP| objects :matlab:`L` and :matlab:`P`, respectively, defined in the above :ref:`Constructor <RP_constructor_example>` section:

   .. code-block:: matlab

      % Write a racetrack resonator and label near the top−left corner of the chip (100 µm WF)
      P.append('racetrack',[1 4],1,[−50 −50 50 50]);
      P.append('radius_label',[1 3.996],1,[−50 −50 50 50]);


.. method:: Raith_positionlist.plot()

   Plot all structures in positionlist with default :ref:`Raith dose factor colouring <RaithDF>`, with chip outline. Elements are displayed as filled polygons, where applicable (:matlab:`'polygon'`; :matlab:`'path'` with non-zero :attr:`data.w <Raith_element.data>`; :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` with empty :attr:`data.w <Raith_element.data>`; :matlab:`'text'`).  All elements in the structure are plotted, regardless of :attr:`data.layer <Raith_element.data>` value.  The full hierarchy of structures including :matlab:`'sref'` or :matlab:`'aref'` elements are displayed if all structures being referenced are present in the library contained in the |RP| object.

   :Arguments: None

   :Returns: None

   .. note::

      Calling :meth:`Raith_positionlist.plot` sets the axis scaling to equal; all plotted objects therefore appear with correct, uniform scaling.  The axes are in units of µm.

   .. rubric:: Example

   Given the |RP| object :matlab:`P` defined in :numref:`§%s <Raith_positionlist:Constructor>`, above:

   .. code-block:: matlab

      P.plot;  % Structures are too small to see at this scale
      axis([990 1010 3990 4010]);  % Zoom to structures

   .. _RP_plot:
   .. figure:: images/RP_plot.svg
      :align: center
      :width: 500

      Positionlist plotted using the :meth:`Raith_positionlist.plot` method

.. method:: Raith_positionlist.plotedges([M[,scDF]]))
