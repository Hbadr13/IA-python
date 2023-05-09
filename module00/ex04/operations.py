import sys

if len (sys.argv) != 3:
    print("Usage: python operations.py <number1> <number2>")
    print("    Example:")
    print("python operations.py 10 3")
    exit(1)
if sys.argv[1].isdigit() == 0 or sys.argv[2].isdigit() == 0:
   print("AssertionError: only integers")
   exit(1)
digit1 = int(sys.argv[1])
digit2 = int(sys.argv[2])
print("Sum:        ",digit1 + digit2)
print("Difference: ", digit1 - digit2)
print("Product:    ", digit1 * digit2)
if(digit2 == 0):
    print("Quotient:    ERROR (division by zero)")
else:
    print("Quotient:   ", digit1 / digit2)
if(digit2 == 0):
    print("Remainder:   ERROR (modulo by zero)")
else:
    print("Remainder:  ",digit1 % digit2)

