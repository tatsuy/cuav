#!/bin/bash

QUALITY=100

while [ true ]
do
  NAME=$(date "+%Y%m%d%H%M%S%2N")
  raspistill -w 1280 -h 960 --raw -q $QUALITY -o camera/raw/${NAME}Z.jpg
  #raspistill -r -l latest.jpg -q $QUALITY -v -dt -t 6000000 -tl 10000 -o camera/raw/${NAME}Z.jpg
  sleep 2
  #./cuav/PiCam/rpi_to_pgm camera/raw/${NAME}Z.jpg
  rm fake_chameleon.pgm > /dev/null
  ln -s camera/raw/${NAME}Z.jpg fake_chameleon.pgm
done
