#!/bin/bash
# autostart for mavproxy on Ranger

(
date
export PATH=$PATH:/bin:/sbin:/usr/bin:/usr/local/bin
export HOME=/root
cd /root
screen -d -m -S MAVProxy -s /bin/bash Ranger/mav_porter.sh
) > /root/autostart.log 2>&1
exit 0
