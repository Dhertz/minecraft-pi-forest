#!/bin/sh

sshpass -p 'raspberry' ssh pi@$1 StrictHostKeyChecking=no 'echo '$2' | write pi tty1'
