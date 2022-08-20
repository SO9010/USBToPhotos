#!/usr/bin/env python
from os import walk
from os import listdir
#settings

move = False
copy = True

goDir = "~/Pictures/"		#change this if you want the photos to go somewhere else :)
fromDir = "/run/media/samio"

imageEnds = ["avif", "gif", "jpg", "jpeg", "jfif", "pjpeg", "pjp", "png", "svg", "webp"]

blackList = ["HardDrive"]

for i in listdir(fromDir): 
    if i not in blackList:
        for files in walk(fromDir + "/" + i):
            if len(files[2]) != 0:
                print(files[2])
                for p in files[2]:
                    if p.endswith(tuple("xml")):
                        print(p)
