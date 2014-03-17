#!/bin/sh

ssh-keyscan -H $1 >> ~/.ssh/known_hosts
sshpass -p 'raspberry' ssh pi@$1 StrictHostKeyChecking=no 'echo '$2' | write pi tty1'
