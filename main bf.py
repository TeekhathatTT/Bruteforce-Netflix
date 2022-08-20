import pyautogui as pg 
import time

time.sleep(6) 
for j in range(0,10000):
    x, y = pg.position()
    r,g,b = pg.pixel(x, y)
    if r==229 and g==9 and b==20:
        if j<10:
            a = '000'+str(j)
            x = [int(i) for i in a]
            print(x)
            for m in x:
                m = str(m)
                pg.press(m)
        elif j<100:
            b = '00'+str(j)
            x = [int(i) for i in b]
            print(x)
            for m in x:
                m = str(m)
                pg.press(m)
        elif j<1000:
            c = '0'+str(j)
            x = [int(i) for i in c]
            print(x)
            for m in x:
                m = str(m)
                pg.press(m)
        else:
            d = j
            x = [int(i) for i in str(d)]
            print(x)
            for m in x:
                m = str(m)
                pg.press(m)

    else:
        break
