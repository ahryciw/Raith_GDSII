Extended techniques
===================

The normal usage of the |RG| toolbox is explained in the foregoing sections of this documentation.  In this section, we describe extended techniques which may be used to save time and/or memory---two concerns which can become limiting factors when generating patterns consisting of very large numbers of elements.  The cost of these extended techniques includes the loss of |RE|, |RS|, and |RL| data checking and all plotting functionality, so they are best used in the final stages of the design process.


Disabling data checking
-----------------------

By default, the properties of |RE|, |RS|, and |RL| objects are checked for correctness (typing, allowed values, size) before being assigned or altered, ensuring that the resulting objects may be plotted and used to generate GDSII and positionlist files without subsequent errors.  By disabling data checking, |RE|, |RS|, and |RL| objects may be created more quickly, at the risk of encountering more cryptic error messages downstream.

Data checking may be disabled by declaring a global variable :matlab:`checkdata` and assigning it a value of logical zero (Boolean :matlab:`false`).

.. rubric:: Example

Creating a series of random |RE| :matlab:`'path'` objects with and without data checking:

.. _datachecking_example:
.. code-block:: matlab

   % With data checking
   tic;
   for k=1:1000
      E=Raith_element('path',0,rand(2,1000),0,1);
   end;
   t_Check=toc;

   % Without data checking
   global checkdata;
   checkdata=false;
   tic;
   for k=1:1000
      E=Raith_element('path',0,rand(2,1000),0,1);
   end;
   t_noCheck=toc;

Without data checking, there is typically a greater than 4× reduction in computation time:

.. _datacheckingout_example:
.. code-block:: matlabsession

   >> t_Check/t_noCheck

   ans =

       4.4510

.. note::

    As a global variable, :matlab:`checkdata` will remain accessible to any functions declaring it as global, even if a :matlab:`clear` command is issued in the current workspace.  To remove :matlab:`checkdata` completely (i.e., restoring the default state of enabled data checking), use :matlab:`clear global checkdata`.


Defining patterns using MATLAB structures
-----------------------------------------

The time and memory overhead associated with creating |RE| and |RS| objects can be further reduced---at the expense of losing all plotting functionality---by using MATLAB `structures <https://www.mathworks.com/help/matlab/ref/struct.html>`_  (i.e., instances of the built-in :matlab:`struct` class) with fields that match the |RE| and |RS| properties, both in name and in type.  Raith "elements" and "structures" defined in this way can be used by |RL| and |RP| objects to generate .csf and .pls files, provided data checking is disabled (see :numref:`§%s <exttech:disabling data checking>`, above).  Refer to the |RE| and |RS| documentation for descriptions of their class properties.

.. rubric:: Example

Creating an array of microrings with varying widths:

.. _struct_example:
.. code-block:: matlab

   % Cell array of ring widths (µm)
   w=num2cell(0.1:0.05:0.5)';

   % Cell array of disk centres:  15 µm spacing in u, v=0
   uv_c=num2cell(15*(0:length(w)-1)'*[1 0],2);

   % 'circle' Raith_element objects have properties 'type', and 'data', the
   % latter having fields 'layer', 'uv_c', 'r', 'w', 'N', and 'DF', so we create
   % a struct object with these fields
   data=struct('layer',0,'uv_c',uv_c,'r',5,'w',w,'N',100,'DF',1.3);
   E=struct('type','circle','data',num2cell(data));

   % Raith_structure objects have properties 'name', 'elements', and 'reflist'
   S.name='rings';
   S.elements=E;
   S.reflist=[];

   global checkdata;
   checkdata=false;
   L=Raith_library('ringarray',S);
   L.writegds;

Running the above yields the following output:

.. _structoutput_example:
.. code-block:: matlabsession

   Skipping all data checking.
   Writing /Users/Public/Documents/ringarray.csf...
        Header information
        Structure 1/1:  rings
   GDSII library ringarray.csf successfully written.

.. note::

   In the above Example, the :matlab:`data` and :matlab:`E` variables were created using MATLAB’s `struct <https://www.mathworks.com/help/matlab/ref/struct.html>`_ function, which yields a structure *array* if any of the value inputs are cell arrays; the same result could have been produced using a :matlab:`for` loop.


"On-the-fly" GDSII writing
--------------------------

In situations where the number of elements in the pattern is so large that there is insufficient memory to keep them all in the MATLAB workspace simultaneously, it is still possible to output a GDSII file by generating elements and writing them sequentially; this procedure uses the static |RL| methods :meth:`writerec <Raith_library.writerec>`, :meth:`writehead <Raith_library.writehead>`, :meth:`writebeginstruct <Raith_library.writebeginstruct>`, :meth:`writeelement <Raith_library.writeelement>`, :meth:`writeendstruct <Raith_library.writeendstruct>`, and :meth:`writeendlib <Raith_library.writeendlib>` to write GDSII records directly.\ [1]_ The following general format must be observed:

|   :meth:`Raith_library.writehead` --- Header information
|      :meth:`Raith_library.writebeginstruct` --- Begin first structure in library
|         :meth:`Raith_library.writeelement` --- First element in structure
|         ⋮
|         :meth:`Raith_library.writeelement` --- Last element in structure
|      :meth:`Raith_library.writeendstruct` --- End first structure
|      ⋮
|      :meth:`Raith_library.writebeginstruct` --- Begin last structure in library
|         :meth:`Raith_library.writeelement` --- First element in structure
|         ⋮
|         :meth:`Raith_library.writeelement` --- Last element in structure
|      :meth:`Raith_library.writeendstruct` --- End last structure
|   :meth:`Raith_library.writeendlib` --- End library

When writing GDSII files "on the fly", the user is responsible for ensuring that all structures referenced by :matlab:`'sref'` and :matlab:`'aref'` elements are in fact present in the library.

.. rubric::  Example

Creating the same array of microrings as in the above Example :numref:`§%s <exttech:defining patterns using matlab structures>` "on the fly":

.. code:: matlab

   % Vector of ring widths (µm)
   w=0.1:0.05:0.5;

   % Matrix of disk centres:  15 µm spacing in u, v=0
   uv_c=15*(0:length(w)-1)'*[1 0];

   % Open file for writing binary data
   FileID=fopen('/Users/Public/Documents/ringarray.csf','W');
   Raith_library.writehead(FileID,'ringarray');
   Raith_library.writebeginstruct(FileID,'rings');

   % Loop through all elements in structure; only one Raith_element object
   % is in memory at any given time.
   for k=1:length(w)
      E=Raith_element('circle',0,uv_c(k,:),5,w(k),100,1.3);
      Raith_library.writeelement(FileID,E);
   end

   Raith_library.writeendstruct(FileID);
   Raith_library.writeendlib(FileID);

   fclose(FileID);


.. [1] Hard-core enthusiasts should note that it is possible to write an entire arbitrary GDSII file using only the :meth:`Raith_library.writerec` method; such a feat is beyond the scope of this User Guide.
