from datetime import datetime

for _ in range(int(input())):
    time1 = input()
    time2 = input()
    time1 = datetime.strptime(time1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(time2, '%a %d %b %Y %H:%M:%S %z')
    diff = (time1 - time2).total_seconds()
    print(abs(int(diff)))
