#!/usr/bin/env python3

import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

PORT_BUTTON = 4     # D4
PORT_ROTARY = 0     # A0

FILE = 'intercepted.txt'

def get_rotary_angle():
    ## from grove_rotary_angle_sensor.py
    adc_ref = 5
    grove_vcc = 5
    full_angle = 300

    # Read sensor value from potentiometer
    sensor_value = grovepi.analogRead(PORT_ROTARY)

    # Calculate voltage
    voltage = round((float)(sensor_value) * adc_ref / 1023, 2)

    # Calculate rotation in degrees (0 to 300)
    degrees = round((voltage * full_angle) / grove_vcc, 2)

    return min(degrees, 300)

def get_key_from_angle(degrees):
    """Converts a degree measurement from the range [0, 300] to a 
    Caesar shift key in the range [0, 26)

    Args:
        degrees: float value in the range [0, 300]
    """
    # TODO: Map degree range to key range
    key_f = 0
    return int(key_f)

def caesar_decrypt(ciphertext, key):
    """Decrypts a Caesar shift ciphertext using the specified key

    Args:
        ciphertext: the encrypted message
        key: integer value representing the key [0, 26)
    """
    # TODO: Make me work
    # Remember encryption shifts to the right, so shift left by key to decrypt
    # You may assume the ciphertext is all lowercase and all letters
    # (don't worry about spaces or punctuations)

    plaintext = ciphertext
    return plaintext

def shutdown():
    lcd.setText('')
    lcd.setRGB(0, 0, 0)

if __name__ == '__main__':
    # Setup
    grovepi.pinMode(PORT_BUTTON, "INPUT")
    grovepi.pinMode(PORT_ROTARY, "INPUT")

    lcd.setRGB(0, 128, 0)

    # Load messages
    ciphertexts = ['khoor']     # test message: 'hello' encrypted with key 3
    # TODO: Load the contents of intercepted.txt into the ciphertexts list
    # ciphertexts = []

    index = 0

    while True:
        try:
            key = get_key_from_angle(get_rotary_angle())
            plaintext = caesar_decrypt(ciphertexts[index], key)

            # Update screen
            lcd.setText_norefresh('{:16}\nKey: {:02d}'.format(plaintext, key))

            # Check for input
            if grovepi.digitalRead(PORT_BUTTON):
                index += 1
                if index >= len(ciphertexts):
                    # Finished
                    break

            time.sleep(0.2)

        except KeyboardInterrupt:
            # Gracefully shutdown on Ctrl-C
            shutdown()
            break

        except IOError as ioe:
            if str(ioe) == '121':
                # Retry after LCD error
                time.sleep(0.25)

            else:
                raise

    shutdown()
