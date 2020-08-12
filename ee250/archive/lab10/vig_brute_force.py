#!/usr/bin/env python3

import time
import sys
import vigenere

def load_file(file_path):
    try:
        with open(file_path , 'r') as f:
            return f.read()
    except Exception as e:
        print(e)
        return None

def successful_decrypt(phrase):
    """Checks the phrase for hints that it is the plaintext.
    Returns True if it is or False if it is still encrypted.
    """
    # TODO: Come up with a simple method to check that the phrase has been
    # properly decrypted. Take a look at sample.txt to see the plaintext.
    return True

def main(filename):
    encrypted_phrase = ''
    
    # key gen helper is an array that will keep track the character ascii values for us
    key_gen_helper = []

    # read the requested file
    with open(filename, 'r') as f:
        encrypted_phrase = f.read()

    decrypted_phrase = encrypted_phrase

    # start the timer
    # TODO: instrument the brute force attack using the time module to measure
    # how long it takes to determine the key
    # https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python

    key = 'a'

    # keep iterating until a successful decrypt has occurred
    while not successful_decrypt(decrypted_phrase):
        key = ''
        
        # generate the string from the key_gen_helper
        for i in reversed(range(len(key_gen_helper))):
            key += chr(key_gen_helper[i])

        # attempt to decrypt using the key generated
        if key != '':
            decrypted_phrase = vigenere.decrypt(encrypted_phrase, key)

        # increment the key_gen_helper ascii values
        index = 0
        # this while loops carries any repeated 'z's over to 'a's
        while (index < len(key_gen_helper)) and (key_gen_helper[index] == ord('z')):
            key_gen_helper[index] = ord('a')
            index += 1
        # add an 'a' to the key_gen_helper if we've reached all 'z's
        if index == len(key_gen_helper):
            key_gen_helper.append(ord('a'))
            print('Testing keys of length {} starting with letter:'.format(len(key_gen_helper)))
            print('{}'.format(chr(key_gen_helper[index - 1])))
        # otherwise increment ascii value at the current index 
        else:
            key_gen_helper[index] += 1
            # If we're incrementing the first letter, print that letter
            if index == len(key_gen_helper) - 1:
                print('{}'.format(chr(key_gen_helper[index])))
    
    # end the timer

    duration = 0

    print('Success! Key is: {}\nDecrypted phrase is:\n{}'.format(key, decrypted_phrase))
    print('Time elapsed: {}s'.format(duration))
    return 0

if __name__ == '__main__':
    main(sys.argv[1])
