#!/bin/bash

git pull
cd /home/pi/RPi-WaterbearNodeJS
git pull
git submodule update
nodejs nodejs-server.js &
/home/pi/mcpi/minecraft-pi &
luakit -u http://localhost:8000/minecraftjs.html
