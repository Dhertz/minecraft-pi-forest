#!/bin/bash

git pull
cd /home/pi/RPi-WaterbearNodeJS
git pull
git submodule update
nodejs nodejs-server.js &
/home/pi/mcpi/minecraft-pi &
IP=`ip addr show eth0 | grep -oP '(inet [\d|\.]+)' | grep -oP '[\d|\.]+'`
echo "Go to http://$IP:8000/minecraftjs.html on the RM computer in chrome!"

