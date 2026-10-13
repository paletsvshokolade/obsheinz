import signal_generator as sg
import pwm_dac
import time

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 1000

if __name__=='__main__':
    try:
        dac = pwm_dac.PWM_DAC(12,500, 3.158, True)
        while True:
            try:
                voltage=float(amplitude*sg.get_line_wave_amplitude(signal_frequency, time.time()))
                dac.set_voltage(voltage)
                sg.wait_for_sampling_period(sampling_frequency)
            except ValueError:
                print('Вы ввели не число, попробуйте еще раз\n')
    finally:
        dac.deinit()