led = {'1':2,
       '2':5,
       '3':5,
       '4':4,
       '5':5,
       '6':6,
       '7':3,
       '8':7,
       '9':6,
       '0':6}
for n in range(int(input())):
       a = input()
       s =0
       for i in a: s+=led[i]
       print(s, 'leds')