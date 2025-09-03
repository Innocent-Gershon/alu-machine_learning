#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Plot y1 as a dashed red line
plt.plot(x, y1, color='red', linestyle='--', label='C-14')

# Plot y2 as a solid green line
plt.plot(x, y2, color='green', linestyle='-', label='Ra-226')

# Label the x-axis
plt.xlabel('Time (years)')

# Label the y-axis
plt.ylabel('Fraction Remaining')

# Set the title of the plot
plt.title('Exponential Decay of Radioactive Elements')

# Set x-axis range
plt.xlim(0, 20000)

# Set y-axis range
plt.ylim(0, 1)

# Add a legend in the upper right hand corner
plt.legend(loc='upper right')

# Display the plot
plt.show()
