import string 
import sys
morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ' ': '/'}
def ft_encode():
    cstr = ""
    for arg in argv:
        arg = arg.split(" ")
        for item in arg:
            if cstr.find(string.punctuation):
                print("ERROR")
                exit(1)
            cstr += item + " " 
    cstr = cstr[:-1]
    strr = "".join([morse_code[i.upper()]+" " for i in cstr])
    strr = strr[:-1]
    return strr

argv = sys.argv[1:]
code = ft_encode()
print(code)
