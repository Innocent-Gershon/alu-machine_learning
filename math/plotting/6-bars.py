#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# your code here
person = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
fruits = ['apples', 'bananas', 'oranges', 'peaches']

bottom = np.zeros(len(person))

for i in range(len(fruits)):
    plt.bar(person, fruit[i], width=0.5, label=fruits[i], color=colors[i],
            bottom=bottom)
    bottom += fruit[i]

plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
