import matplotlib.pyplot as plt
import json
import math

def plot_set_vs_list():
    with open('set_vs_list.json', 'r') as f:
        data = json.load(f)
    # plt.plot(data['sizes'],[(y) for y in data['set']], marker='o', label='set')
    # plt.plot(data['sizes'], [(y) for y in data['list']], marker='x', label='list')
    plt.plot(data['sizes'],[math.log10(y) for y in data['set']], marker='o', label='set')
    plt.plot(data['sizes'], [math.log10(y) for y in data['list']], marker='x', label='list')
    plt.legend()
    plt.xlabel('Number of elements')
    plt.ylabel('log10(Time) ')
    plt.xscale('log')
    plt.show()

plot_set_vs_list()
