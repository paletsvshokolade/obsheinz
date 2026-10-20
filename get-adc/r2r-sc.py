import r2r_adc
import time
import adc_plot

adc=r2r_adc.R2R_ADC(3.16,0.0001)

voltages=[]
times=[]
duration=3.0

if __name__=='__main__':
    try:
        t1=time.time()
        while time.time()-t1<duration:
            voltages.append(adc.get_sc_voltage())
            times.append(time.time()-t1)
        adc_plot.plot_voltage_vs_time(times, voltages, 3.16)
    finally:
        adc.deinit()