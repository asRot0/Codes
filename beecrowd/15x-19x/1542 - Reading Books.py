while True:
    n = [int(x) for x in str(input()).split()]
    if n[0]==0:break
    q,d,p = n[0],n[1],n[2]
    x = int((d*q*p)/(p-q))
    if x==1:print('1 pagina')
    else:print('{} paginas'.format(x))