import fileinput
import math
f = fileinput.input()
casenumber = int(f.readline())
for case in range(1, casenumber+1):
    value=int(f.readline())
    one = sum([int("1"+"0"*(k-i-1)) for i,j,k in [(i,j,math.floor(math.log10(abs(value))+1)) for i,j in enumerate(str(value)) if j == "4"]])
    print("Case #"+str(case)+": "+str(one)+" "+str(value-one))
