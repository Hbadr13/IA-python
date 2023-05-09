import sys

av = sys.argv
if(len(av) != 2):
    print("AssertionError: more than one argument are provided")
    exit(1)

arg = av[1]

sing = 1
if(arg[0] == '+' or arg[0] == '-'):
    if(arg[0] == '-'):
        sing = -1
    arg = arg[1:]
if(arg.isdigit() == 0):
    print("AssertionError: argument is not an integer")
    exit(1)
integer = int(arg)
integer *= sing
if(integer % 2):                                                                                                                                                                                                                                 
    print("I'm Odd.")
else:
    print("I'm Even.")
