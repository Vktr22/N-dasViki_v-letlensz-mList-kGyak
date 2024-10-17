import feladatok
lista=[12,21,56,32,-5,-23,35]

print("1.) feladat:")
db:int=feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma {db}")
print("")

print("2.) feladat:")
osszeg:int=feladatok.neg_szamok_osszege(lista)
print(f"A negatív számok összege: {osszeg}")
print("")