#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create bins every 10 units
bins = np.arange(0, 101, 10)

# Plot the histogram
plt.hist(student_grades, bins=bins, edgecolor='black')

# Label the x-axis
plt.xlabel('Grades')

# Label the y-axis
plt.ylabel('Number of Students')

# Set the title of the plot
plt.title('Project A')

# Set x-axis limits to match common grade scales, if needed,
# though the bins define the visible range mostly.
# plt.xlim(0, 100) # Optional, depends on desired exact boundary behavior.

# Display the plot
plt.show()
