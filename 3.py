Llista = []

szám = int(input("Írjon be számokat: "))

while(szám!=""):
    Llista.append(int(szám))
    szám = input("Írjon be számokat: ")
   
print(sum(Llista)) 