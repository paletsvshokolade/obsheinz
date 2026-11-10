import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage,verbose=False,name='experimental_plot'):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel('time')
    plt.ylabel('voltage')
    plt.ylim(0,max_voltage)
    if verbose: plt.savefig(f'{name}.png')
    plt.show()

def plot_sampling_period_hist(time,verbose=False,name='time_plot'):
    sampling_periods = [time[i]-time[i-1] for i in range(1,len(time))]
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods)
    plt.ylabel('number of measures')
    plt.xlabel('time of measure')
    plt.grid()
    if verbose: plt.savefig(f'obsheinz/plots/{name}.png')
    plt.show()