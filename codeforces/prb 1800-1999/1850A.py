for n in [*open(0)][1:]:
    a, b, c = map(int, n.split())
    print(['NO', 'YES'][a + b >= 10 or a + c >= 10 or b + c >= 10])
