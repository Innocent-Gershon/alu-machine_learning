#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Plot x vs y as a line graph
plt.plot(x, y)

# Label the x-axis
plt.xlabel('Time (years)')

# Label the y-axis
plt.ylabel('Fraction Remaining')

# Set the title of the plot
plt.title('Exponential Decay of C-14')

# Set y-axis to logarithmic scale
plt.yscale('log')

# Set x-axis range
plt.xlim(0, 28650)

# Display the plot
plt.show()
