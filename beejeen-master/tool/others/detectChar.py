#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6
#-*- coding: UTF-8 -*-


import glob
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
for filename in glob.glob('*.log'):
    print(filename.ljust(60))
    detector.reset()
    for line in open(filename, 'rb'):
        detector.feed(line)
        if detector.done: break
    detector.close()
    print(detector.result)
