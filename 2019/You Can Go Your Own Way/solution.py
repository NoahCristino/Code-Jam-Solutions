import fileinput
f = fileinput.input()
casenumber = int(f.readline())
for case in range(1, casenumber+1):
    dimensions=f.readline()
    x=f.readline()
    x2 = x.replace("S", "X")
    x3 = x2.replace("E", "S")
    newpath = x3.replace("X", "E")
    print("Case #"+str(case)+": "+newpath)
