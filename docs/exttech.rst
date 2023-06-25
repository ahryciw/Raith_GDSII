Extended techniques
===================

The normal usage of the |RG| toolbox is explained in the foregoing sections of this documentation.  In this section, we describe extended techniques which may be used to save time and/or memory---two concerns which can become limiting factors when generating patterns consisting of very large numbers of elements.  The cost of these extended techniques includes the loss of |RE|, |RS|, and |RL| data checking and all plotting functionality, so they are best used in the final stages of the design process.


Disabling data checking
-----------------------

By default, the properties of |RE|, |RS|, and |RL| objects are checked for correctness (typing, allowed values, size) before being assigned or altered, ensuring that the resulting objects may be plotted and used to generate GDSII and positionlist files without subsequent errors.  By disabling data checking, |RE|, |RS|, and |RL| objects may be created more quickly, at the risk of encountering more cryptic error messages downstream.

Data checking may be disabled by declaring a global variable :matlab:`checkdata` and assigning it a value of logical zero (Boolean :matlab:`false`).

.. rubric:: Example

Creating a series of random |RE| :matlab:`'path'` objects with and without data checking, resulting in a greater than 4× reduction in computation time:

.. _datachecking_example:
.. code-block:: matlab

   >> % With data checking
   >> tic;for k=1:1000
   E=Raith_element('path',0,rand(2,1000),0,1);
   end;t_Check=toc;
   >> % Without data checking
   >> global checkdata
   >> checkdata=false;
   >> tic;for k=1:1000
   E=Raith_element('path',0,rand(2,1000),0,1);
   end;t_noCheck=toc;
   >> t_Check/t_noCheck

   ans =

       4.4510

.. note::

    As a global variable, :matlab:`checkdata` will remain accessible to any functions declaring it as global, even if a :matlab:`clear` command is issued in the current workspace.  To remove :matlab:`checkdata` completely (i.e., restoring the default state of enabled data checking), use :matlab:`clear global checkdata`.


Defining patterns using MATLAB structures
-----------------------------------------




"On-the-fly" GDSII writing
--------------------------

