import numpy as np
import matplotlib.pyplot as plt


def plot_discrete(dist, x_left=0, x_right=20, function='cdf'):
    x = np.linspace(x_left, x_right, x_right - x_left + 1, dtype=np.int32)
    _, ax = plt.subplots(figsize=(8, 8))
    ax.grid(linewidth=0.5)
    plt.title(dist.name)

    params = {
        'cdf': {
            'func': dist.cdf,
            'color': 'b',
            'func_symb': 'F'
        },
        'pdf': {
            'func': dist.pmf,
            'color': 'r',
            'func_symb': 'f'
        },
    }
    
    try:
        func = params[function]['func']
        color = params[function]['color']
        func_symb = params[function]['func_symb']
    except KeyError:
        print("Function to plot is one of the following: ", params.keys())
    
    plt.scatter(x, func(x), marker='D', color=color, label=r'{0}: {1}(x)'.format(dist, func_symb))      
    plt.legend()


def plot_continuous(dist, x_left=0, x_right=20, num_points=1000, function='cdf'):
    x = np.linspace(x_left, x_right, num_points)
    _, ax = plt.subplots(figsize=(8, 8))
    ax.grid(linewidth=0.5)
    plt.title(dist.name)

    params = {
        'cdf': {
            'func': dist.cdf,
            'color': 'b',
            'func_symb': 'F'
        },
        'pdf': {
            'func': dist.pdf,
            'color': 'r',
            'func_symb': 'f'
        },
    }
    
    try:
        func = params[function]['func']
        color = params[function]['color']
        func_symb = params[function]['func_symb']
    except KeyError:
        print("Function to plot is one of the following: ", params.keys())
    
    plt.plot(x, func(x), color=color, label=r'{0}: {1}(x)'.format(dist, func_symb))      
    plt.legend()
