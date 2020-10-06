import time

y = 0
m = 0

while True:
    if m <= 11:
        m += 1
        time.sleep(1)
        
    elif m == 12:
        y += 1
        m = 1
    print(y, m)
