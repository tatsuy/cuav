#!/bin/bash

QUALITY=100

FILE_PREFIX=$(date "+%Y")
ln -s latest_img.jpg fake_chameleon.pgm
raspistill -r -l latest_img.jpg -q $QUALITY -v -dt -t 6000000 -tl 1000 -o camera/raw/${FILE_PREFIX}%dZ.jpg
