import walky_talky


f = walky_talky.bothway(10)
f.write("hellow")

while True:
    print("hi")
    o = f.read()
    if o == None:
        pass
    print(f.read(),end="")

f.end()
