""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grovepi import *
from grove_rgb_lcd import *
from time import sleep

# Connect the Rotary Angle Sensor to analog port A2


# Connect the Ultrasonic ranger to digital port D4


setRGB(0,255,0)

i = 0


"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    
	ultrasonic_ranger = 4
	potentiometer = 2

while True:
	try:
		# Read resistance from Potentiometer
		i = grovepi.analogRead(potentiometer)
		threshold = int(i / 2)
		print(threshold)

		time.sleep(0.2)
		distant = ultrasonicRead(ultrasonic_ranger)
		print(distant,'cm')

		t = str(threshold)
		d = str(distant)

		if distant <= threshold:
			print("Threshold reached")
			setRGB(255,0,0)
			obj = "OBJ PRES"
		else:
			setRGB(0,255,0)
			obj = ""

		setText_norefresh(t + "cm " + obj + "\n" + d + "cm")



	

	except TypeError:
		print("Error")
	except IOError:
		print("Error")




