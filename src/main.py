#!/usr/bin/env python
import os

#settings

move = False
copy = True

goDir = "~/Pictures/"		#change this if you want the photos to go somewhere else :)
fromDir = "/run/media" + os.getlogin()

for files in os.walk("fromDir"):
	print(files)