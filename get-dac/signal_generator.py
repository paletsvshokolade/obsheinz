import numpy as np
import time

def get_sin_wave_amplitude(freq,t):
    return (np.sin(2*np.pi*freq*t)+1)/2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)

def get_line_wave_amplitude(freq,t):
    phase=t*freq % 1.0
    return 1 - abs(2.0*phase-1.0)