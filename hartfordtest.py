import os, time, shutil, sys


work_path = r'D:\travellers\ArcFireLine\FireRing\Hartford\CO'

if os.listdir(work_path)=="":
    print "yes"
else:
    print "No"