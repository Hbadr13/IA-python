
import sys

def text_analyzer(*argv):
    lower = 0
    upper = 0
    spaces = 0
    punctuation = 0
    if len(argv) == 0:
        av = input("What is the text to analyze?\n>> ")
    elif len(argv) > 1:
        return
    elif 1:
        print ('AssertionError: argument is not a string')
        return
    else:
        av = argv[0]
    for i in av:
        if(i.islower()):
            lower += 1
        elif(i.isupper()):
            upper += 1
        elif(i.isspace()):
            spaces += 1
        else:
            punctuation += 1
    print(upper, " upper letter(s)")
    print(lower, " lower letter(s)")
    print(punctuation, " punctuation mark(s)")
    print(spaces, " space(s)")
