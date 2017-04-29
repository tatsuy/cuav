Geotagger (geotag.py)
=====================

This program adds geotags (longitude and latitude coordinates) to
photos captured in-flight using a APM telemetry log (tlog) file to 
match the GPS location of the UAV at the time each photo was taken.

The geotags are stored in the Exif data of each photo file.

The "last modified" time of each image file is taken as it's capture time.

It has the following options and arguments:

===============================   ========================================   ===============================
Argument                          Description                                Default
===============================   ========================================   ===============================
files                             Directory containing png image files       (none)
--mavlog                          Telemetry logfile (tlog)                   (none)
--max-deltat                      Max deltat for interpolation               0.0
--max-attitude                    Max attitude geo-referencing               45 degrees
--lens                            Lens focal length                          4
--roll-stabilised                 Is camera roll stabilised?                 False
--gps-lag                         GPS lag in seconds                         0.0
--destdir                         Directory to place geotagged files         (none)
--inplace                         Modify image files in-place?               False
===============================   ========================================   ===============================

If no arguments are supplied, a GUI will appear asking for startup options.

Otherwise, it can be started directly from the commandline. For example, In Linux:

.. code:: bash

    geotag.py <arguments> <folder>
    geotag.py --mavlog=flight.tlog /home/user/images/totag
    

.. image:: geotag1.png

.. image:: geotag2.png
