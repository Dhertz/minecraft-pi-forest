#!/bin/sh

sudo apt-get -y install nmap sshpass --no-install-recommends
mesg y
nmap -p 22 192.168.1.0/24 | grep -B 3 open | grep Nmap | grep -oP '[\d|\.]+.\d'

