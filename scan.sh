#!/bin/sh

nmap -p 22 10.210.193.0/24 | grep -B 3 open | grep Nmap | grep -oP '[\d|\.]+'
