#--- string alignment in python ----#
#https://www.scaler.com/topics/python/string-formatting-in-python/

kata = "The right format"
# if len(kata) > 42:
    # print("lenght of kata > 42")
# print("{:->{}}%".format(kata,42))
print(kata.rjust(42,'-'))
