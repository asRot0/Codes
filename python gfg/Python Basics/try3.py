# Python code to truncate float
# values to 2 decimal digits.

# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

# Using format
Output = [float('{:.2f}'.format(elem)) for elem in Input]
output = ['{:.2f}'.format(elem) for elem in Input]

# Print output
print(Output)
print(output)
