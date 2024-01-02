import numpy as np
import matplotlib.pyplot as plt

# Sequence data
sequence = [2, 3, 5, 6, 7, 9]

# Calculate mean and standard deviation
mean = np.mean(sequence)
std = np.std(sequence)

# Create the plot
plt.figure(figsize=(8, 5))  # Adjust figure size as needed

# Plot the sequence data as a blue bar chart
plt.bar(np.arange(len(sequence)), sequence, color='blue')

# Add a horizontal line for the mean in red
plt.axhline(y=mean, color='red', linestyle='--', label='Mean')

# Add shaded region for the standard deviation in blue
plt.axhspan(mean - std, mean + std, alpha=0.2, color='blue', label='Standard Deviation')

# Customize the plot
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Sequence Data with Mean and Standard Deviation')
plt.xticks(np.arange(len(sequence)))  # Add x-axis labels for each bar
plt.legend()  # Display the legend

plt.show()
