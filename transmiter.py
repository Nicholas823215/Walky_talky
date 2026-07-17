import walky_talky
import time


f = walky_talky.bothway(10)
f.write("hellow")

while True:
    o = f.read()
    print(o)
    time.sleep(1)

f.end()
