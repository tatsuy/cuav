PGM Converter (pgm_convert.py)
==============================

This program converts images from pgm format to
either jpeg or png format.

The pgm file type is used by some camera models (such
as the `Ptgrey Chameleon <https://www.ptgrey.com/chameleon-usb2-cameras/>`_, 
used by CanberraUAV) to represent
a raw bayer grid image.

It has the following options and arguments:

===============================   ========================================   ===============================
Argument                          Description                                Default
===============================   ========================================   ===============================
--directory                       Directory containing PGM image files       (none)
--output-directory                Directory to place converted files         (same directory as input files)
--format                          type of file to convert to (png or jpg)    jpg
===============================   ========================================   ===============================

If no arguments are supplied, a GUI will appear asking for startup options.

Otherwise, it can be started directly from the commandline. For example, In Linux:

.. code:: bash

    geotag.py <arguments> <folder>
    geotag.py --format=png /home/user/images/toconvert
    
.. image:: pgm_conv1.png

.. image:: pgm_conv2.png
