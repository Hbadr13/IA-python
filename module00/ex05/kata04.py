kata = (0, 4, 132.42222, 10000, 12345.67)
if len(kata) != 5:
    print("Invalid kata length")
    exit(1)
print("module_%s, ex_%s : %.2f, %.2e, %.2e"%(str(kata[0]).rjust(2,"0"),(str(kata[1]).rjust(2,"0")),kata[2],kata[3],kata[4]))
