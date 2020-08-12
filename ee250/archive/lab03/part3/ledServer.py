# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are able to successfully `import grovepi` below. You may need more for your
# assignment.
sys.path.append('../../../Software/Python/')

import grovepi

if __name__ == '__main__':
    