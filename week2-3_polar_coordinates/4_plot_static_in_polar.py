"""https://scipy-lectures.org/intro/matplotlib/auto_examples/plot_polar.html
"""

import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)

N = 20 # Number of bars
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N) # Equally spaced angles from 0 to 2pi
radius = 10 * np.random.rand(N) # An array of random lengths
# width = np.pi / 4 * np.random.rand(N) # An array of random widths
width = 2 * np.pi / N # This creates equally spaced bars

# Creating the bars
bars = plt.bar(theta, radius, width=width, bottom=0.0)

# Styling the bars
for r,bar in zip(radius, bars):
    bar.set_facecolor(plt.cm.Blues(r/10.)) # r/10 scales the radius to a 0-1 range.
    bar.set_alpha(0.5)

ax.set_xticklabels([])
ax.set_yticklabels([])
plt.show()
