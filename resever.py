import walky_talky

f = walky_talky.bothway(10)
f.write("Hi")

while True:
    o = f.read()
    if o != None:
        print(f.read(),end="")



