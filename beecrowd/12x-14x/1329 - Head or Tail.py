while True:
    ordem = int(input())
    if ordem == 0:
        break
    else:
        array = [int(i) for i in input().split(" ")]
        print(
            "Mary won %d times and John won %d times" % (array.count(0), array.count(1))
        )