from datetime import datetime, date, time

kata = (2019, 9, 25, 3, 30)

if len(kata) != 5:
    exit(1)
if (kata[0] > 10000 or kata[1] > 100 or kata[2] > 100 or kata[3] > 100 or kata[4] > 100):
    print("Out of range")
    exit(1)
if (kata[0] < 0 or kata[1] < 0 or kata[2] < 0 or kata[3] < 0 or kata[4] < 0):
    print("Out of range")
    exit(1)

my_string = str(kata[0]) + "*" + str(kata[1]) + "*" + str(kata[2])
my_date = datetime.strptime(my_string, "%Y*%m*%d")
print(my_date.strftime("%m-%d-%Y"), end=" ")

my_string = str(kata[3]) + "-" + str(kata[4])
my_date = datetime.strptime(my_string, "%H-%M")
print(my_date.strftime("%H:%M"))
