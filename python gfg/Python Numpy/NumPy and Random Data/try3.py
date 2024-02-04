import numpy as np

num_list = [10, 20, 30, 40, 50]

print(np.random.choice(num_list))
print(np.random.choice(num_list, 3,
                       p=[0, 0, 0, 1, 0]))
print(np.random.choice(num_list, 3,
                       p=[0, 0, 0.5, 0.5, 0]))
print('__ '*10)

num = np.arange(10)
np.random.shuffle(num)
print(num)

num = np.arange(16).reshape((4, 4))
np.random.shuffle(num)
print(num)