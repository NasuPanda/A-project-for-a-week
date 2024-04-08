"""Visualize spiral and lemniscate
"""

import matplotlib.pyplot as plt
import numpy as np
import math

fig, ax = plt.subplots(subplot_kw={"projection":"polar"})
STEP_SIZE = 1000 # This decides the smoothness of graphs

def plot_in_polar(theta, radius, label="", title=""):
    """Plot on the polar coordinate"""
    ax.plot(theta, radius, label=label) if label else ax.plot(theta, radius)
    if title:
        ax.set_title(title)

def visualize_spiral_along_magnitude(start:int, stop:int, a=2, step=2, interval=0.5):
    """
    To see how the magnitude of a in the equation `a*pi` affects the shape of the graph
    """
    for magnitude in range(start, stop, step):
        theta = np.linspace(0, magnitude*np.pi, STEP_SIZE)
        radius = a * theta
        title = f"Spiral of the equation {magnitude}π"
        plot_in_polar(theta, radius, title=title)
        plt.pause(interval)
        ax.cla()

def visualize_smoothness_of_spiral(start: int, stop: int, step: int = 1, a: int = 2, interval: float = 0.5):
    """
    To see how step size affects the smoothness of the graph
    """
    for step_size in range(start, stop, step):
        theta = np.linspace(0, 2*np.pi, step_size)
        radius = a * theta
        title = f"Spiral with a step size of {step_size}"
        plot_in_polar(theta, radius, title=title)
        plt.pause(interval) # Pause for an interval
        ax.cla()

def equation_of_lemniscate(theta, a = 2):
    cos_theta = np.cos(2 * theta)
    # If the inside of a square is negative, it's undefined
    return math.sqrt(2 * a**2 * cos_theta) if cos_theta >= 0 else np.nan

# Lemniscate: Figure-eight-like shape
# Equation r² = 2a²cos(2θ)
# NOTE: this equation is undefined when cos(2θ) is negative.
# vectorize: take a function and turn it into a NumPy vectorized function, which can operate on arrays element-wise.
vectorized_f = np.vectorize(equation_of_lemniscate)
a = 2

theta = np.linspace(0, 2*np.pi, STEP_SIZE)
radius = vectorized_f(theta)
title = "Lemniscate"
plot_in_polar(theta, radius, label="lemniscate", title=title)
plt.show()
