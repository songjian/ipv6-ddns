#!/bin/bash
ip addr show $1 | grep inet6 | grep mngtmpaddr | awk '{ print $2; }' | sed 's/\/.*$//' | xargs ./alidns-ddns.py
