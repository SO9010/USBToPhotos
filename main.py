#!/usr/bin/env python
import os
import shutil
#settings

move = False
copy = True

goDir = "/home/samio/Pictures"		#change this if you want the photos to go somewhere else :)
fromDir = "/run/media/samio"

imageEnds = "avif, gif, jpg, jpeg, jfif, pjpeg, pjp, png, svg, webp"

blackList = "HardDrive"


def isDoubleName(checkFile):
    for files in os.listdir(goDir):
        if files == checkFile:
            return True
    return False

duploNo = 0

for folder in os.listdir(fromDir):
    if folder not in blackList:
        for root, dirs, files in os.walk(fromDir + "/" + folder):
            if blackList not in root:    
                for name in files:
                    if name[len(name) - 3 : len(name)] in imageEnds: 
                        if isDoubleName(name) != True:
                            print(os.path.join(root, name))
                            if move:
                                shutil.move(os.path.join(root,name), goDir + "/" + name)
                            if copy:
                                shutil.copyfile(os.path.join(root, name), goDir + "/" + name)
