def fun(var):
    if var in ['a', 'e', 'i']:
        return True
    else:
        return False


li = list('eijdffeso')

print(list(filter(fun, li)))


