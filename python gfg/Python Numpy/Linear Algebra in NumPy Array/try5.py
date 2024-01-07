import numpy as np
import matplotlib.pyplot as plt

# Vector data
v = np.array([0, 1, 2, 3, 4])

# Orders for which to calculate magnitudes
orders = [0, 1, 2, 3, 4]

# Calculate magnitudes for each order
magnitudes = [np.linalg.norm(v, ord=o) for o in orders]

# Create the plot
plt.figure(figsize=(8, 6))  # Adjust figure size as needed

# Plot the magnitudes as a line chart with markers
plt.plot(orders, magnitudes, marker='o', linestyle='--', color='blue')

# Customize the plot
plt.xlabel('Order')
plt.ylabel('Magnitude')
plt.title('Nth-Order Magnitudes of the Vector')
plt.grid(True)  # Add grid lines for visual clarity

plt.show()
