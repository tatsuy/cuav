===============
Getting Started
===============

This section gives details on running the various tools that make up
the cuav package.

PGM Converter (pgm_convert.py)
==============================

This program converts images from pgm format to
either jpeg or png format.

The pgm file type is used by some camera models (such
as the `Ptgrey Chameleon <https://www.ptgrey.com/chameleon-usb2-cameras/>`_, 
used by CanberraUAV) to represent
a raw bayer grid image.

It has the follow options and arguments:

===============================   ========================================   ===============================
Setting                           Description                                Default
===============================   ========================================   ===============================
directory                         Directory containing PGM image files       (none)
output-directory                  Directory to place converted files         (same directory as input files)
format                            type of file to convert to (png or jpg)    jpg
===============================   ========================================   ===============================

.. image:: pgm_conv1.png

.. image:: pgm_conv2.png

Geotagger (geotag.py)
=====================

This program adds geotags (longitude and latitude coordinates) to
photos captured in-flight using a APM telemetry log (tlog) file to 
match the GPS location of the UAV at the time each photo was taken.

The geotags are stored in the Exif data of each photo file.

The "last modified" time of each image file is taken as it's capture time.

It has the follow options and arguments:

===============================   ========================================   ===============================
Setting                           Description                                Default
===============================   ========================================   ===============================
files                             Directory containing png image files       (none)
mavlog                            Telemetry logfile (tlog)                   (none)
max-deltat                        Max deltat for interpolation               0.0
max-attitude                      Max attitude geo-referencing               45 degrees
lens                              Lens focal length                          4
roll-stabilised                   Is camera roll stabilised?                 False
gps-lag                           GPS lag in seconds                         0.0
destdir                           Directory to place geotagged files         (none)
inplace                           Modify image files in-place?               False
===============================   ========================================   ===============================

.. image:: geotag1.png

.. image:: geotag2.png

Geosearch (geosearch.py)
========================

This program searches a set of photos taken by a UAV and looks for any interesting
or unusual objects (such as stranded people). Any candidate objects are georeferenced on a 
map and shown to the user.

The overall objective is to quickly and easily find the location of a missing person, based on
a set of photos taken overhead by a UAS.

The algorithm used in geosearch is very conservative and will err on the side of cuation when deciding
if an object is "interesting" enough to flag to the user. Thus it is expected that many false positives will 
be detected, at which point it will be up to the user to figure out if an image contains the desired person or 
object.

The algorithm is tuned for finding person-sized and shaped objects that contrast well against the background. So a 
person laying down and wearing high-visibility clothing will be easily found. It has been (somewhat humourously) noted
that sheep to fit in this category too. 

There are two ways of running geosearch:

#. With timestamped images and a flight log

#. With geotagged images

It has the follow options and arguments:

===============================   =================================================   ===============================
Setting                           Description                                         Default
===============================   =================================================   ===============================
files                             Directory containing png image files                (none)
mavlog                            Telemetry logfile (tlog)                            (none)
mission                           Waypoints text file for displaying mission          (none)
kmzlog                            Kmz file for image positions                        (none)
triggerlog                        Robota trigger file for image positions             (none)
time-offset                       Offset between camera and mavlink log times         0 seconds
view                              Show images                                         False
saveview                          Save image view                                     False
lens                              Lens focal length                                   28
sensorwidth                       Sensor (camera) width                               35 mm
service                           Map tile service                                    MicrosoftSat
camera-params                     Camera calibration json file from OpenCV            (none)
debug                             Enable debug info                                   False
roll-stabilised                   Is camera roll stabilised?                          False
rotate-180                        Rotate images 180 degrees                           False
altitude                          Altitude when images captured (0 for automatic)     0
thumbsize                         Thumbnail size                                      60
mosaic-thumbsize                  Mosiac thumbnail size                               35
minscore                          Minimum score for an image to be flagged            100
gammalog                          Gamma.log from flight                               (none)
target                            Lat,lon,radius of area to search                    (none)
categories                        Xml file containing categories for classification   (none)
flag                              Flag positions                                      (none)
blue-emphasis                     Enable blue emphasis in scanner                     False
===============================   =================================================   ===============================

.. toctree::
    :maxdepth: 1
