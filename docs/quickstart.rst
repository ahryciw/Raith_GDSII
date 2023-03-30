Quick-start guide
=================

As a simple example, let us construct a pattern of a cantilever for use with a positive-tone resist (e.g,. ZEP, PMMA). First, define a polygon element for a 10-μm-long, 1-μm-wide cantilever with 3 μm spacing between the cantilever and the edge of the window:

.. code-block:: matlab

   % obj=Raith_element('polygon',layer,uv,DF)
   % uv is a 2 x n matrix of polygon vertices [u_values;v_values]
   % DF is dose factor
   E=Raith_element('polygon',0,[0 13 13 0 0 10 10 0 0; ...
                                0  0  7 7 4  4  3 3 0],1.3);
   axis equal;
   E.plot;

