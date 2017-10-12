import os, datetime, commands

from time import sleep
from picamera import PiCamera

image_tail = "jpg"
image_format = "jpeg" # for picamera capture func
save_dir = "images"
#save_dir = "camera/raw"
fake_org_tail = "jpg"
fake_name = "fake_chameleon.pgm"
fake_dir = "/home/apsync/GitHub/cuav"
pgm_command = "./cuav/PiCam/rpi_to_pgm"

def camera_setup(camera):
    camera.iso = 400

def capture():
    camera = PiCamera(resolution=(1280, 960), framerate=15)
    camera_setup(camera)
    # start and wait warming up
    camera.start_preview()
    sleep(2)
    # continuous capture
    fname = "rpi_tmp.%s" % (image_tail)
    for filename in camera.capture_continuous(fname, format=image_format, bayer=True):
        now = datetime.datetime.now()
        stamp = now.strftime("%Y%m%d%H%M%S%f")[0:-4]
        new_name = "%sZ.%s" % (stamp, image_tail)
        os.rename(filename, new_name)
        new_path = move_to_save_dir(new_name)
        link_to_fake(new_path)

def move_to_save_dir(filename):
    filepath = os.path.realpath(filename)
    print filepath
    targetpath = os.path.realpath(save_dir)
    targetpath = "%s/%s" % (targetpath, filename)
    print targetpath
    os.rename(filepath, targetpath)
    convert_to_pgm(targetpath)
    return targetpath

def convert_to_pgm(filename):
    print "convert %s" % (filename)
    ret = commands.getoutput("%s %s" % (pgm_command, filename))

def link_to_fake(new_path):
    pgm_path = new_path.replace(image_tail, fake_org_tail)
    fake_target = "%s/%s" % (fake_dir, fake_name)
    if (os.path.islink(fake_target)):
        os.unlink(fake_target)
    os.symlink(pgm_path, fake_target) 

capture()
