#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 

import os.path

def checkSettingsFile():
	return os.path.isfile("settings.dat")