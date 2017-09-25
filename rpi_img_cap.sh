#!/bin/bash

QUALITY=100

FILE_PREFIX=$(date "+%Y")
ln -s latest_img.jpg fake_chameleon.pgm
## TODO: check param, ISO:400
raspistill -n -r -l latest_img.jpg -ISO 400 -q $QUALITY -v -dt -t 6000000 -tl 1000 -o /mnt/img/${FILE_PREFIX}%dZ.jpg
