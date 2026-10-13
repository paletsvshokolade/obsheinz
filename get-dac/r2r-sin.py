import signal_generator as sg
import r2r_dac
import time

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000

if __name__=='__main__':
    try:
        dac = r2r_dac.R2R_DAC([16,20,21,25,26,17,27,22], 3.158, True)
        while True:
            try:
                voltage=float(amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time()))
                dac.set_voltage(voltage)
            except ValueError:
                print('Вы ввели не число, попробуйте еще раз\n')
    finally:
        dac.deinit()