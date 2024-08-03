for _ in range(int(input())):
    output = ''
    for _ in range(8):
        inp_str = input()
        output += inp_str.replace('.', '')
    print(output)