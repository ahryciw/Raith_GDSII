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

   .. _RP_append_example:
   .. code-block:: matlab

      % Write a racetrack resonator and label near the top-left corner of the chip (100 µm WF)
      P.append('racetrack',[1 4],1,[-50 -50 50 50]);
      P.append('radius_label',[1 3.996],1,[-50 -50 50 50]);


.. method:: Raith_positionlist.plot()

   Plot all structures in positionlist with default :ref:`Raith dose factor colouring <RaithDF>`, with chip outline. Elements are displayed as filled polygons, where applicable (:matlab:`'polygon'`; :matlab:`'path'` with non-zero :attr:`data.w <Raith_element.data>`; :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` with empty :attr:`data.w <Raith_element.data>`; :matlab:`'text'`).  All elements in the structure are plotted, regardless of :attr:`data.layer <Raith_element.data>` value.  The full hierarchy of structures including :matlab:`'sref'` or :matlab:`'aref'` elements is displayed if all structures being referenced are present in the library contained in the |RP| object.

   :Arguments: None

   :Returns: None

   .. note::

      Calling :meth:`Raith_positionlist.plot` sets the axis scaling to equal; all plotted objects therefore appear with correct, uniform scaling.  The axes are in units of µm.

   .. rubric:: Example

   Given the |RP| object :matlab:`P` defined in the above :meth:`Raith_positionlist.append` :ref:`Example <RP_append_example>`:

   .. _RP_plot_example:
   .. code-block:: matlab

      P.plot;  % Structures are too small to see at this scale
      axis([990 1010 3990 4010]);  % Zoom to structures

   .. _RP_plot:
   .. figure:: images/RP_plot.svg
      :align: center
      :width: 500

      Positionlist plotted using the :meth:`Raith_positionlist.plot` method


.. method:: Raith_positionlist.plotedges()

   Plot outlines of all structures in positionlist with default :ref:`Raith dose factor colouring <RaithDF>`, with chip outline. Elements are displayed as unfilled polygons, where applicable (:matlab:`'polygon'`; :matlab:`'path'` with non-zero :attr:`data.w <Raith_element.data>`; :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` with empty :attr:`data.w <Raith_element.data>`; :matlab:`'text'`).  All elements in the structure are plotted, regardless of :attr:`data.layer <Raith_element.data>` value.  The full hierarchy of structures including :matlab:`'sref'` or :matlab:`'aref'` elements is displayed if all structures being referenced are present in the library contained in the |RP| object.

   :Arguments: None

   :Returns: None

   .. note::

      Calling :meth:`Raith_positionlist.plotedges` sets the axis scaling to equal; all plotted objects therefore appear with correct, uniform scaling.  The axes are in units of µm.

   .. rubric:: Example

   Given the |RP| object :matlab:`P` defined in the above :meth:`Raith_positionlist.append` :ref:`Example <RP_append_example>`:

   .. _RP_plotedges_example:
   .. code-block:: matlab

      P.plotedges;  % Structures are too small to see at this scale
      axis([990 1010 3990 4010]);  % Zoom to structures

   .. _RP_plotedges:
   .. figure:: images/RP_plotedges.svg
      :align: center
      :width: 500

      Positionlist plotted using the :meth:`Raith_positionlist.plotedges` method


.. method:: Raith_positionlist.plotWA()

   Plot working area of all structures in positionlist in dotted blue lines, with chip outline.

   :Arguments: None

   :Returns: None

   .. note::

      Calling :meth:`Raith_positionlist.plotWA` sets the axis scaling to equal; all working areas therefore appear with correct, uniform scaling.

   .. rubric:: Example

   To illustrate the alignment of working areas and writefields, this example specifies working areas which are smaller than the writefield. Assume the |RL| and |RP| objects :matlab:`L` and :matlab:`P`, respectively, are defined as in :numref:`§%s <Raith_positionlist:Constructor>`; to preserve the relative alignment of the racetrack and the label, **uv_c** must be changed to accommodate the difference in WA:

   .. _RP_plotWA_example:
   .. code-block:: matlab

      P.append('racetrack',[1 4],1,[-10 -10 20 10]);
      P.append('radius_label',[0.99 4.001],1,[-20 -5 10 5]);
      P.plot; % Plot structures
      P.plotWA; % Plot working areas
      axis([935 985 3945 3975]); % Zoom to structures

   .. _RP_plotWA:
   .. figure:: images/RP_plotWA.svg
      :align: center
      :width: 500

      Working areas in positionlist plotted using the :meth:`Raith_positionlist.plotWA` method


.. method:: Raith_positionlist.plotWF()

   Plot writefields of all structures in positionlist in dotted green lines, with chip outline; writefield centres are marked with a :green:`+` sign.

   :Arguments: None

   :Returns: None

   .. note::

      Calling :meth:`Raith_positionlist.plotWF` sets the axis scaling to equal; all writefields therefore appear with correct, uniform scaling.

   .. rubric:: Example

   Given all objects defined in the above :meth:`Raith_positionlist.plotWA` :ref:`Example <RP_plotWA_example>`:

   .. _RP_plotWF_example:
   .. code-block:: matlab

      P.plot;  % Plot structures
      P.plotWA;  % Plot working areas
      P.plotWF;  % Plot writefields
      axis([940 1050 3950 4055]);  % Zoom to structures

   .. _RP_plotWF:
   .. figure:: images/RP_plotWF.svg
      :align: center
      :width: 500

      Working areas in positionlist plotted using the :meth:`Raith_positionlist.plotWA` method


.. method:: Raith_positionlist.centre([mbyn])

   Centre current positionlist entries on the chip, preserving relative spacing, with the option of matrix-copying them.

   :Arguments: **mbyn** -- Number of rows and columns of the matrix of sub-chips [optional]; 1 × 2 vector [*m* *n*]

   :Returns: None

   .. note::

      If called with no argument, the current positionlist entries are shifted such that the overall pattern (as defined by the working areas) are centred both vertically and horizontally on the chip. If called with the optional **mbyn** argument, the chip is divided into an *m*-by-*n* matrix of equal-sized rectangular sub-chips, and the positionlist entries are centred as described above in each sub-chip. In either case, the :attr:`poslist <Raith_positionlist.poslist>` property is overwritten; there is no built-in way of undoing this operation.

   .. rubric:: Example

   Given the |RP| object defined in the above :meth:`Raith_positionlist.plotWA` :ref:`Example <RP_plotWA_example>`:

   .. _RP_centre_example:
   .. code-block:: matlab

      P.plotWF;  % Before centring
      P.centre;
      P.plotWF;  % After centring
      P.centre([4 5]);
      P.plotWF;  % After matrix-copying

   .. _RP_centre:
   .. figure:: images/RP_centre.svg
      :align: center
      :width: 500

      Position of writefields (a) before centring, (b) after issuing :matlab:`P.centre`, and (c) after issuing :matlab:`P.centre([4 5])`


.. method:: Raith_positionlist.shift(uv_sh)

   Shift current positionlist entries on the chip, preserving relative spacing.

   :Arguments: **uv_sh** -- Relative shift of the new positionlist entries with respect to their current positions (mm); 1 × 2 vector [*u*\ :sub:`sh` \ *v*\ :sub:`sh`]  (mm)

   :Returns: None

   .. note::

      The :attr:`poslist <Raith_positionlist.poslist>` property is overwritten when :meth:`Raith_positionlist.shift` is invoked; there is no built-in way of undoing this operation.

   .. rubric:: Example

   Given the |RP| object defined in the above :meth:`Raith_positionlist.plotWA` :ref:`Example <RP_plotWA_example>`:

   .. _RP_shift_example:
   .. code-block:: matlab

      P.plotWF; % Before shifting
      P.shift([1 -2]);
      P.plotWF; % After shifting

   .. _RP_shift:
   .. figure:: images/RP_shift.svg
      :align: center
      :width: 500

      Position of writefields (a) before shifting, (b) after issuing :matlab:`P.shift([1 -2])`


.. method:: Raith_positionlist.writepls([filepath])

   Write positionlist to file.

   :Arguments: **filepath** -- Full path of positionlist file to be written, including .pls extension [optional]

   :Returns: None

   .. note::

      If called without argument, a :attr:`Raith_library.name`.\ *pls* file is written to the current directory.

   .. rubric:: Example

   Given the |RP| object defined in the above :meth:`Raith_positionlist.plotWA` :ref:`Example <RP_plotWA_example>`:

   .. _RP_writepls_example:
   .. code-block:: matlabsession

      >> P.writepls;

      Writing /Users/Public/Documents/resonators.pls...
      Positionlist resonators.pls successfully written.
