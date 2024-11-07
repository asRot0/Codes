import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x ** 2
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 15]
labels = ['Category 1', 'Category 2', 'Category 3']
sizes = [20, 35, 45]

# Line Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='sin(x)', color='b', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='r', linestyle='--')
plt.title("Line Plot of sin(x) and cos(x)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
np.random.seed(0)
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
size = 100 * np.random.rand(50)
plt.figure(figsize=(6, 6))
plt.scatter(x_scatter, y_scatter, c=colors, s=size, alpha=0.5, cmap='viridis')
plt.title("Scatter Plot")
plt.colorbar()
plt.show()

# Bar Plot
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Horizontal Bar Plot
plt.figure(figsize=(6, 4))
plt.barh(categories, values, color='salmon')
plt.title("Horizontal Bar Plot")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

# Histogram
data = np.random.randn(1000)
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Data")
plt.ylabel("Frequency")
plt.show()

# Box Plot
data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(80, 30, 200)
data = [data1, data2, data3]
plt.figure(figsize=(6, 5))
plt.boxplot(data, vert=True, patch_artist=True, labels=['Data 1', 'Data 2', 'Data 3'])
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title("Pie Chart")
plt.show()

# Subplots
fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax[0, 0].plot(x, y1, color='blue')
ax[0, 0].set_title("Line Plot")
ax[0, 1].scatter(x_scatter, y_scatter, color='green')
ax[0, 1].set_title("Scatter Plot")
ax[1, 0].bar(categories, values, color='orange')
ax[1, 0].set_title("Bar Plot")
ax[1, 1].hist(data1, bins=15, color='purple')
ax[1, 1].set_title("Histogram")
plt.tight_layout()
plt.show()

# Heatmap
matrix = np.random.rand(10, 10)
plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()
