import matplotlib.pyplot as plt

riding = ((17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
          (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4))
swimming = ((17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
            (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9))
sailing = ((31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
           (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4))

plt.scatter(x=riding[0], y=riding[1], c='red', marker='o', label='riding')
plt.scatter(x=swimming[0], y=swimming[1], c='green', marker='^', label='swimming')
plt.scatter(x=sailing[0], y=sailing[1], c='blue', marker='*', label='sailing')

plt.xlabel('age')
plt.ylabel('hours')
plt.title('Activities scatter graph')
plt.legend()
plt.show()