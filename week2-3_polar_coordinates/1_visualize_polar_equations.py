"""Visualize basic polar equations: Circle, Line, and Cardioid(butt-like shape)
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection":"polar"})
step_size = 200 # This decides the smoothness of graphs

# Equation1: Circle
theta = np.linspace(0, 2*np.pi, step_size) # Array of angles
radius = 2 # constant radius
ax.plot(theta, radius * np.ones_like(theta), label="Circle")

# Equation 2: Line
theta = np.pi * 99   # Fixed angle
radius = np.linspace(0, 3, step_size)  # Range of radii
ax.plot(theta * np.ones_like(radius), radius, label="Line")

# Equation 3: Cardioid
a = 2 # Size of the shape
theta = np.linspace(0, 2*np.pi, step_size)
radius = a + a*np.cos(theta)
ax.plot(theta, radius, label="Cardioid")

# Showing the graph
ax.set_title("Polar Equations")
ax.legend()
plt.show()
