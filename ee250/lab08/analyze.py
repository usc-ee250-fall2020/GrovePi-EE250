import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import sys
import os
#required: sudo apt-get install ffmpeg python3-tk

MAX_FRQ = 2000
SLICE_SIZE = 0.15

def main(start_time, file):
    print("Importing {}".format(file))
    audio = AudioSegment.from_mp3(file)

    sample_count = audio.frame_count()
    sample_rate = audio.frame_rate

    print("Number of channels: " + str(audio.channels))
    print("Sample count: " + str(sample_count))
    print("Sample rate: " + str(sample_rate))
    print("Sample width: " + str(audio.sample_width))

    """***********************FULL SAMPLE PLOT**************************"""
    samples = audio.get_array_of_samples()
    period = 1/sample_rate                  #the period of each sample
    duration = sample_count/sample_rate     #length of full audio in seconds
    time = np.arange(0, duration, period)   #generate a array of time values from 0 to [duration] with step of [period]

    #TODO: Plot the full sample as a subplot (make sure to include labels)
    plt.figure(figsize=(20,10))
    plt.subplot(221)

    """***********************SAMPLE SLICE PLOT*************************"""
    print("Analyzing slice at {}s".format(start_time))
    slice_frame_size = int(SLICE_SIZE*sample_rate)   #get the number of elements expected for [SLICE_SIZE] seconds
    start_index = int(start_time*sample_rate)        #get the starting index for the given [start_time]
    end_index = start_index + slice_frame_size      #find the ending index for the slice

    time_slice = time[start_index: end_index]       #take a slice from the time array for the given start and end index 
    sample_slice = samples[start_index: end_index]  #take a slice from the samples array for the given start and end index

    #TODO: Plot the sample slice as a subplot (make sure to include labels)
    plt.subplot(222)

    """**********************SAMPLE SLICE FFT PLOT**********************"""
    n = slice_frame_size                            #n is the number of elements in the slice

    #generating the frequency spectrum
    k = np.arange(n)                                #k is an array from 0 to [n] with a step of 1
    slice_duration = n/sample_rate                   #slice_duration is the length of time the sample slice is (seconds)
    frq = k/slice_duration                          #generate the frequencies by dividing every element of k by slice_duration

    sample_slice_fft = np.fft.fft(sample_slice)/n   #perform the fourier transform on the sample_slice and normalize by dividing by n

    max_frq_idx = int(MAX_FRQ*slice_duration)       #get the index of the maximum frequency (2000)
    frq = frq[range(max_frq_idx)]                   #truncate the frequency array so it goes from 0 to 2000 Hz
    sample_slice_fft = sample_slice_fft[range(max_frq_idx)]     #truncate the sample slice fft array so it goes from 0 to 2000 Hz

    #TODO: Plot the frequency spectrum as a subplot (make sure to include labels)
    plt.subplot(212)

    plt.suptitle(file)
    plt.show()

def usage():
    print("Usage: analyze.py [file] [start_time]")

if __name__ == '__main__':
    if len(sys.argv) != 3 or not os.path.isfile(sys.argv[1]):
        usage()
        exit(1)
    try:
        float(sys.argv[2])
    except ValueError:
        usage()
        exit(1)

    main(float(sys.argv[2]), sys.argv[1])
