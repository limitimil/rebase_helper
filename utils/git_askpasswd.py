#!/usr/bin/env python3
#
# Short & sweet script for use with git clone and fetch credentials.
# Requires GIT_USERNAME and GIT_PASSWORD environment variables,
# intended to be called by Git via GIT_ASKPASS.
#

from sys import argv
from os import environ

if "username" in argv[1].lower():
    print('liminchien')
    exit()

if "password" in argv[1].lower():
    print('your password here')
    exit()

exit(1)
