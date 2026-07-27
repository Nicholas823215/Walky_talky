import walky_talky
import time


f = walky_talky.bothway(10)
f.write(0)
o = 0

while int(o)<= 100:
    o = f.read()
    print(o)
    f.write(int(o) +1)
    time.sleep(0.5)

f.end()