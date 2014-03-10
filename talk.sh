#!/bin/sh

sshpass -p 'raspberry' ssh pi@10.210.193.168 StrictHostKeyChecking=no 'echo '$1' | write p1 tty1'
