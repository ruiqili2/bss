""" Settings for application"""
import os
import random
import string
import logging
DEBUG = True
DIRNAME = os.path.dirname(__file__)
STATIC_PATH = os.path.join(DIRNAME, 'static')
TEMPLATE_PATH = os.path.join(DIRNAME, 'templates')
#WORKDIR = os.path.join(STATIC_PATH, "workdir/")
with open('config/ranC.tk', 'r') as fi:
    COOKIE_SECRET = fi.readline().strip()
    SKEY = fi.readline().strip()
