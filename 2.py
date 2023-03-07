import random

tipp = int(input("Írja be hogy fej(1) vagy írás(2): "))

fej = random.randint(1,2)
írás = random.randint(1,2)



if fej>írás:
    print("maga vesztett")
elif írás<fej:
    print("maga nyert")
else:
    print("Maga nem létező számot adott meg")


