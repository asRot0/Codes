a = float(input())
a = float("%.2f" % a)

if 0.00 < a <= 2000.00:
    print('Isento')
    exit()
elif 2000.00 < a <= 3000.00:
    a = a - 2000.00
    tax = (a * 8) / 100
    print('R$', "%.2f" % tax)
    exit()
elif 3000.00 < a <= 4500.00:
    a = a - 2000.00
    b = a - 1000.00
    tax = ((a - b) * 8) / 100
    tax1 = (b * 18) / 100
    print('R$', "%.2f" % (tax + tax1))
    exit()
elif a > 4500.00:
    a = a - 2000.00
    b = a - 1000.00
    c = b - 1500.00
    tax = ((a - b) * 8) / 100
    tax1 = ((b - c) * 18) / 100
    tax2 = (c * 28) / 100
    print('R$', "%.2f" % (tax + tax1 + tax2))
    exit()