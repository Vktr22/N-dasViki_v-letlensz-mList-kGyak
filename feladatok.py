"""
adott egy lista
lista=[12,21,56,32,-5,-23,35]

-> az alábbi metódusok paraméterként kapják a listát
-> visszatérési értékkel
1) Hány pozitív szám van benne?
2) Mennyi a negatív számok összege?
3) Mennyi az öttel osztható számok átlaga
"""


def poz_szamok_szama(lista):
    # return None    ->ezt akk haszn, ha létre akarjuk hozni a metódust, de még nem akarunk írni bele,
                    # így nem fog hibát jelezni
    i:int=0
    pozSzamokSzama:int=0
    while(i<len(lista)):
        if (lista[i]>0):
            pozSzamokSzama+=1
        i+=1
    return pozSzamokSzama


def neg_szamok_osszege(lista):
    i:int=0
    negSzamOsszeg:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            negSzamOsszeg+=lista[i]
        i+=1
    return negSzamOsszeg


def ottel_oszthat_atlag(lista):
    i:int=0
    ossz:float=0
    db:int=0
    while(i<len(lista)):
        if (lista[i]%5==0):
            ossz+=lista[i]
            db+=1
        i+=1
    atl:float=ossz/db
    return atl