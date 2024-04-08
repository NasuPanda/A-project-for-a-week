import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection":"polar"})
STEP_SIZE = 1000 # This decides the smoothness of graphs

def plot_in_polar(theta, radius, label="", title=""):
    """Plot on the polar coordinate"""
    ax.plot(theta, radius, label=label) if label else ax.plot(theta, radius)
    if title:
        ax.set_title(title)

def equation_of_rose_curves(theta, a=2, k=1):
    cos_k_theta = np.cos(k * theta)
    # If the inside of a square is negative, it's undefined
    return a * cos_k_theta

def animate_rose_curve(start: int, stop: int, step: int = 10, a: int = 2, interval: float = 0.5):
    """
    To see how step size affects the smoothness of the graph
    """
    vectorized_f = np.vectorize(equation_of_rose_curves)
    theta = np.linspace(0, 2*np.pi, STEP_SIZE)

    for k in range(start, stop, step):
        radius = vectorized_f(theta, a=a, k=k)
        title = f"Rose curve with k = {k}"

        plot_in_polar(theta, radius, title=title)
        plt.pause(interval) # Pause for an interval
        ax.cla()

def loop_rose_curve(start: int, stop: int, step: int = 10, a: int = 2, interval: float = 0.5):
    vectorized_f = np.vectorize(equation_of_rose_curves)
    k = start
    op_should_be_incremental = True # The flag to check whether k should be increased

    while True:
        # In between start and step, the value k goes back and forth with the step size.
        if k == start:
            op_should_be_incremental = True
        if k == stop:
            op_should_be_incremental = False

        if op_should_be_incremental:
            k += step
        else:
            k -= step

        theta = np.linspace(0, 2*np.pi, STEP_SIZE)
        radius = vectorized_f(theta, a=a, k=k)
        title = f"Rose curve with k = {k}"

        plot_in_polar(theta, radius, title=title)
        plt.pause(interval) # Pause for an interval
        ax.cla()

# animate_rose_curve(1, 100, 1, 2)
loop_rose_curve(5, 10, 1, 2, 0.5)
