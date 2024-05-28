from datetime import datetime, timedelta, date
import time

print(date.today())
print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
print(datetime.now().strftime("%H:%M:%S"))

t1 = datetime.now()
t2 = datetime.strptime("2000/01/01", "%Y/%m/%d")

print((t1-t2).total_seconds())

print(datetime.now().strftime("%Y-%b-%d %H:%M:%S"))

date = input("Ivesti data formatu MMMM/MM/DD: ")

date = datetime.strptime(date, "%Y/%m/%d")

print(date - date.today())

sekundes = int(input("Ivesti sekundes: "))

for sekunde in range(sekundes, -1, -1):
    print("\t{0}".format(sekunde), end="\r")
    time.sleep(1)

print("\rLaikas")