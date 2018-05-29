import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)
# print(x.size)
# print(x.shape)
y = np.sin(x**2)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
plt.savefig('simple_plot')

# figure, axes = plt.subplots()
# axes.plot(x,y)

# Create the figure and two axes (two rows, one column)
fig, (ax1, ax2) = plt.subplots(2, 1)
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)
ax1.plot(x1, y1)

x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)
ax2.plot(x2, y2)

plt.savefig('sin_cos.png')

# combine the tow figures into one
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
x1 = np.linspace(0, 4 * np.pi, 100)
y1 = np.sin(x1)
function1 = ax1.plot(x1, y1, 'red', label="sin")

x2 = np.linspace(0, 4 * np.pi, 100)
y2 = np.cos(x2)
function2 = ax2.plot(x2, y2, 'blue', label='cos')

# Create the legend by first fetching the labels from the functions
functions = function1 + function2
labels = [f.get_label() for f in functions]
plt.legend(functions, labels, loc=0)

# plt.savefig('sin_cos2.png')
# plt.savefig('sin_cos3.png') ##add legend
# plt.savefig('sin_cos4_color') ##color for diff lines

# Add x-label (only one, since it is shared) and the y-labels
ax1.set_xlabel()