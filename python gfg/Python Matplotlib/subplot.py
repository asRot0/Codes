import matplotlib.pyplot as plt

t = range(0, 20)
s = range(30, 10, -1)
grid_size = '22'
figure = plt.figure()

position = grid_size + '1'
print('Adding first subplot to position', position)
axis1 = figure.add_subplot(int(position))
axis1.set(title='subplot(2,2,1)')
axis1.plot(t, s)

position = grid_size + '2'
print('Adding second subplot to position', position)
axis2 = figure.add_subplot(int(position))
axis2.set(title='subplot(2,2,2)')
axis2.plot(t, s, 'r-')

position = grid_size + '3'
print('Adding third subplot to position', position)
axis3 = figure.add_subplot(int(position))
axis3.set(title='subplot(2,2,3)')
axis3.plot(t, s, 'g-')

position = grid_size + '4'
print('Adding fourth subplot to position', position)
axis4 = figure.add_subplot(int(position))
axis4.set(title='subplot(2,2,4)')
axis4.plot(t, s, 'y-')
plt.show()