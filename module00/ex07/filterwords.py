import string
import sys

argv = sys.argv[1:]
if len(argv) != 2:
    print("ERROR")
    exit(1)
if argv[1].isdigit() == False:
    print("ERROR")
    exit(1)
lenn = int(argv[1])
lst = argv[0].split(" ")
lst2 =[ls.strip(string.punctuation) for ls in lst if len(ls.strip(string.punctuation)) > lenn]
print(lst2)