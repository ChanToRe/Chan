import time

y = 0
m = 0
d = 0

while True:
    if m <= 11:
        if d <= 30:
            d += 1
            #time.sleep(1)
            
        elif d == 31:
            m += 1
            d = 1
        
    elif m == 12:
        y += 1
        m = 1
        
    print(y, m, d)
        
