def digit_sum(num_digit):
    n = 0
    for i in str(num_digit):
        n += int(i)
    return n


num_list = [13, 11, 12, 10, 17, 16]
sum_odd = [digit_sum(num) for num in num_list if num & 1]
print(sum_odd)
