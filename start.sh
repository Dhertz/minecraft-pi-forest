#!/bin/bash

nodejs nodejs-server.js &
/home/pi/mcpi/minecraft-pi &
luakit -u http://localhost:8000/minecraftjs.html
