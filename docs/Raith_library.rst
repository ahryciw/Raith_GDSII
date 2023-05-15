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
:Arguments: + **name** --  Character array specifying name of GDSII library, not including .csf/.gds extension.
            + **structures** -- Array of |RS| objects in library.  |RS| objects may be added to :attr:`structures <Raith_library.structures>` either using standard MATLAB notation, or via the :meth:`Raith_library.append` method.

.. note::

   By default, all properties are checked for correctness (typing, allowed values, size) before being assigned, whether the |RL| object is created with a constructor or its properties are amended individually.

.. rubric:: Example

Given the |RS| object :matlab:`S` defined in :numref:`§%s <Raith_structure:Constructor>`:

.. _RL_constructor_example:
.. code-block:: matlab

   % Racetrack resonator defined in Raith_structure object S; here we are adding a text label
   lbl=Raith_structure('radius_label',Raith_element('text',0,[0 0],2,0,[1 0],'3 µm',1.5));
   L=Raith_library('resonators',[S lbl]);



Methods
-------

.. method:: Raith_library.append(S)

   Append |RS| object(s) to library; structure names are checked for uniqueness.

   :Arguments: **S** -- |RS| object (or array thereof) to be appended to library

   :Returns: None

   .. rubric:: Example

   Given the |RS| objects :matlab:`S` and :matlab:`lbl`, defined in :numref:`§%s <Raith_structure:Constructor>` and the above :ref:`Constructor <RL_constructor_example>` section, respectively, the three following commands all yield the same library :matlab:`L`:

   .. code-block:: matlab

      % Using Raith_library.append
      L=Raith_library('resonators',S);
      L.append(lbl);

      % Using horizontal concatenation
      L=Raith_library('resonators',[S lbl]);

      % Using array indexing
      L=Raith_library('resonators',S);
      L.structures(end+1)=lbl;


.. method:: Raith_library.writegds([outdir[,dialect]])

   Write Raith GDSII hierarchy of all structures to file ⟨:attr:`name <Raith_library.name>`⟩.\ *csf* (:matlab:`'Raith'` dialect) or ⟨:attr:`name <Raith_library.name>`⟩.\ *gds* (:matlab:`'plain'` dialect).

   :Arguments: + **outdir** -- Character array specifying directory in which to write .csf file [optional]; if called without arguments, file is written to working directory.
               + **dialect** -- Character array specifying dialect of GDSII to write [optional]; may be :matlab:`'Raith'` (default) or :matlab:`'plain'` (readable by non-Raith GDSII viewers/editors).

   :Returns: None

   .. note::

      If :matlab:`'plain'` is specified for **dialect**, Raith curved and FBMS elements (:matlab:`'arc'`, :matlab:`'circle'`, :matlab:`'ellipse'`, :matlab:`'fbmspath'`, :matlab:`'fbmscircle'`) are converted to GDSII BOUNDARY (polygon) elements or PATH elements, as appropriate, matching their appearance when plotted. The exported file also has a .gds extension by default, and may be opened by non-Raith GDSII editors such as `KLayout <https://www.klayout.de>`_ .

   .. rubric:: Example

   Given the |RL| object :matlab:`L` in the above :ref:`Constructor <RL_constructor_example>` section:

   .. code-block:: matlabsession

      >> L.writegds('/Users/Public/Documents');

      Checking for missing structures...OK.
      Writing /Users/Public/Documents/resonators.csf...
           Header information
           Structure 1/2:  racetrack
           Structure 2/2:  radius_label
      GDSII library resonators.csf successfully written.


.. method:: Raith_library.plot(structname[,M[,scDF]])

   Plot structure in library with default :ref:`Raith dose factor colouring <RaithDF>`. Elements are displayed as filled polygons, where applicable (:matlab:`'polygon'`; :matlab:`'path'` with non-zero :attr:`data.w <Raith_element.data>`; :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` with empty :attr:`data.w <Raith_element.data>`; :matlab:`'text'`).  All elements in the structure are plotted, regardless of :attr:`data.layer <Raith_element.data>` value. The full hierarchy of structures including :matlab:`'sref'` or :matlab:`'aref'` elements are displayed if all structures being referenced are present in the library.

   :Arguments: + **structname** -- Character array specifying name of structure to be plotted (must be in :attr:`structlist <Raith_library.structlist>`)
               + **M** -- Augmented transformation matrix to be applied to element [optional]; see :meth:`Raith_library.trans`,   :meth:`Raith_library.rot`, :meth:`Raith_library.refl`, and :meth:`Raith_library.scale`.
               + **scDF** -- Overall multiplicative scaling factor applied to dose factors of all elements in structure [optional]

   :Returns: None

   Calling :meth:`Raith_library.plot` does not change the current axis scaling; issue an :matlab:`axis equal` command to ensure that the element is displayed in the figure correctly.

   .. note::

      Normally, :meth:`Raith_library.plot` is called without arguments, to display the structure as it would appear in the |RNS| software. The optional arguments :matlab:`M` and :matlab:`scDF` are used internally, when :meth:`Raith_library.plot` is called by :meth:`Raith_positionlist.plot`.

   .. rubric:: Example

   Given the |RS| objects :matlab:`S` and :matlab:`lbl`, defined in :numref:`§%s <Raith_structure:Constructor>` and :numref:`§%s <Raith_library:Constructor>` section, respectively:

   .. _RL_plot_example:
   .. code-block:: matlab

      % Racetrack resonator defined in Raith_structure object S
      % Radius label defined in Raith_structure object lbl
      E(1)=Raith_element('sref','racetrack',[0 0]);
      E(2)=Raith_element('sref','radius_label',[0 -4]);
      RR=Raith_structure('labelled_racetrack',E);

      L=Raith_library('resonators',RR);
      L.plot('labelled_racetrack');  % Figure 5.1

      L.append(S);
      clf;
      L.plot('labelled_racetrack');  % Figure 5.2
      axis equal;

      L.append(lbl);
      clf;
      L.plot('labelled_racetrack');  % Figure 5.3
      axis equal;

   .. _RL_plot1:
   .. figure:: images/RL_plot1.svg
      :align: center
      :width: 500

      Display resulting from :meth:`Raith_library.plot` method when referenced structures are not in library

   .. _RL_plot2:
   .. figure:: images/RL_plot2.svg
      :align: center
      :width: 500

      Display resulting from :meth:`Raith_library.plot` method when one referenced structure is not in library

   .. _RL_plot3:
   .. figure:: images/RL_plot3.svg
      :align: center
      :width: 500

      Display resulting from :meth:`Raith_library.plot` method when  all referenced structures are present in library



.. method:: Raith_library.plotedges([M[,scDF]])

   Plot outlines of structure in library with default :ref:`Raith dose factor colouring <RaithDF>`. Elements are displayed as unfilled polygons, where applicable (:matlab:`'polygon'`; :matlab:`'path'` with non-zero :attr:`data.w <Raith_element.data>`; :matlab:`'arc'`, :matlab:`'circle'`, and :matlab:`'ellipse'` with empty :attr:`data.w <Raith_element.data>`; :matlab:`'text'`).  All elements in the structure are plotted, regardless of :attr:`data.layer <Raith_element.data>` value. The full hierarchy of structures including :matlab:`'sref'` or :matlab:`'aref'` elements are displayed if all structures being referenced are present in the library.

   :Arguments: + **structname** -- Character array specifying name of structure to be plotted (must be in :attr:`structlist <Raith_library.structlist>`)
               + **M** -- Augmented transformation matrix to be applied to element [optional]; see :meth:`Raith_library.trans`,   :meth:`Raith_library.rot`, :meth:`Raith_library.refl`, and :meth:`Raith_library.scale`.
               + **scDF** -- Overall multiplicative scaling factor applied to dose factors of all elements in structure [optional]

   :Returns: None

   Calling :meth:`Raith_library.plotedges` does not change the current axis scaling; issue an :matlab:`axis equal` command to ensure that the element is displayed in the figure correctly.

   .. note::

      Normally, :meth:`Raith_library.plotedges` is called without arguments, to display the structure as it would appear in the |RNS| software. The optional arguments :matlab:`M` and :matlab:`scDF` are used internally, when :meth:`Raith_library.plotedges` is called by :meth:`Raith_positionlist.plotedges`.

   .. rubric:: Example

   Given the |RL| object :matlab:`L` defined at the end of the :ref:`previous example <RL_plot_example>`:

   .. code-block:: matlab

      L.plotedges('labelled_racetrack');
      axis equal;

   .. _RL_plotedges:
   .. figure:: images/RL_plotedges.svg
      :align: center
      :width: 500

      Display resulting from :meth:`Raith_library.plotedges` method when all structures are present in library


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
