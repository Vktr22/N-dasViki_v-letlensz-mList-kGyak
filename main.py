import feladatok
import veletlenszamos_listak

lista = [12, 21, 56, 32, -5, -23, 35]

print("1.) feladat:")
db: int = feladatok.poz_szamok_szama(lista)
print(f"A pozitív számok száma {db}")
print("")

print("2.) feladat:")
osszeg: int = feladatok.neg_szamok_osszege(lista)
print(f"A negatív számok összege: {osszeg}")
print("")

print("3.) feladat:")
atlag: float = feladatok.ottel_oszthat_atlag(lista)
print(f"Az öttel osztható számok átlaga: {atlag}")
print("")


#print("Véletlenszámos listák:")
tizermedobasLista = []
veletlenszamos_listak.ermedobasok(tizermedobasLista)
print(tizermedobasLista)
fejdb:int=(veletlenszamos_listak.hany_fej_van(tizermedobasLista))
print(f"{fejdb} esetben lett fej 10 dobásból.")
print("")

ketszaszKockadobasLista = []
dobszam:int=200
print(veletlenszamos_listak.kockadobasok(ketszaszKockadobasLista, dobszam))
print("")

print(f"{veletlenszamos_listak.hanyszorDobVmelySzambol(1,ketszaszKockadobasLista)} alkalommal dobtunk 1-est.")
print(f"{veletlenszamos_listak.hanyszorDobVmelySzambol(2,ketszaszKockadobasLista)} alkalommal dobtunk 2-est.")
print(f"{veletlenszamos_listak.hanyszorDobVmelySzambol(3,ketszaszKockadobasLista)} alkalommal dobtunk 3-ast.")
print(f"{veletlenszamos_listak.hanyszorDobVmelySzambol(4,ketszaszKockadobasLista)} alkalommal dobtunk 4-est.")
print(f"{veletlenszamos_listak.hanyszorDobVmelySzambol(5,ketszaszKockadobasLista)} alkalommal dobtunk 5-öst.")
print(f"{veletlenszamos_listak.hanyszorDobVmelySzambol(6,ketszaszKockadobasLista)} alkalommal dobtunk 6-ost.")
db1:int=veletlenszamos_listak.hanyszorDobVmelySzambol(1,ketszaszKockadobasLista)
db2:int=veletlenszamos_listak.hanyszorDobVmelySzambol(2,ketszaszKockadobasLista)
db3:int=veletlenszamos_listak.hanyszorDobVmelySzambol(3,ketszaszKockadobasLista)
db4:int=veletlenszamos_listak.hanyszorDobVmelySzambol(4,ketszaszKockadobasLista)
db5:int=veletlenszamos_listak.hanyszorDobVmelySzambol(5,ketszaszKockadobasLista)
db6:int=veletlenszamos_listak.hanyszorDobVmelySzambol(6,ketszaszKockadobasLista)
print(db1+db2+db3+db4+db5+db6)

dobasokSzama:int=200
cinkeltDobasokLista=[]
veletlenszamos_listak.cinkeltkocka(dobasokSzama, cinkeltDobasokLista)



