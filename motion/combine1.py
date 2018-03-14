import os
from subprocess import *

#run child script 1
p = Popen([r'/home/pi/Desktop/ReactionBot2.0/testserv.py', "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print (output[0])

#run child script 2
p = Popen([r'/home/pi/Desktop/ReactionBot2.0/testserv2.py', "ArcEditor"], shell=True, stdin=PIPE, stdout=PIPE)
output = p.communicate()
print (output[0])
