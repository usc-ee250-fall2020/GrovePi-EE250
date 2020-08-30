4. Reflection Questions

	1.  git clone git@github.com:my-name/my-imaginary-repo.git
		cd my-imaginary-repo
		touch my_second_file.py
		git add .
		git commit -m "Added file my_second_file.py"
		git push

	2.	I mainly edited my file on Sublime from my VM, used github to transfer my code to the RPi.
		Sometimes when I found syntactic errors or needed to make minor changes I used nano within my RPi,
		because the push pull becomes very tedious for every minor error. I'm hoping to get a monitor soon 
		so I can code using a GUI text editor directly from my RPi.

	3.	The RaspberryPi send a signal to the Ultrasonic Ranger and waits for sometime before it asks for 
		the information. There is a 2ms delay in the write_i2c_block() function in the python library which is used to signal to ultrasonic ranger. The RPi communicates with the ATmega328P through the I2C communication protocol.
