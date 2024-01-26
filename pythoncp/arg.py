'''
nums = [1,2,3,4]
print(nums)
print(*nums)
'''

'''
def order_pizza(size, *toppings, **details):
    print(f'Ordered a {size} pizza with the following toppings.')
    for topping in toppings:
        print(f'- {topping}')
    # print(toppings)
    # print(details)
    print('Details of the order are:')
    for key, value in details.items():
        print(f'- {key}: {value}')


order_pizza('large', 'pepperoni', 'olives', delivery=True, tip=5)
'''


def my_map(my_func, my_iter):
    result = []
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return result


nums = [1, 2, 3, 4, 5, 6]
print(my_map(lambda a: a ** 3, nums))