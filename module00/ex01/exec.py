import sys

av = sys.argv
if(len(av) < 3):
    exit(1)
av = av[::-1]
for i in range(0, len(av) - 1):
    av[i] = av[i][::-1]
    print(av[i].swapcase(), end = "")
    if(i != len(av) - 2):
        print(end=" ")
print("")
