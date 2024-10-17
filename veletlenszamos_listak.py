"""
Készíts függvényt mely az érmedobást szimulálja és legenerál 10 db fej,
v írástt és az eredményt eltárolja egy listában. A függvény térjen vissza a listával

A továbbiakban ezzel a listával dolgozz az alábbi függvényekben:
számold meg hány db fej van a listában
"""
import random


def ermedobasok(lista):
    i:int=0
    #veletlen:int=0
    while(i<10):
        veletlen:int = int(random.random()*2+1)   # random.random()*(b-a)+a
        """veletlen: int = random.random()  # random.random()*(b-a)+a
                    if (veletlen < 0,5):"""
        if(veletlen==1):
            lista.append("fej")
        else:
            lista.append("írás")
        i+=1
    return lista

def hany_fej_van(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]=="fej"):
            db+=1
        i+=1
    return db


"""
Készíts függvényt, mely a kockadobást szimulálja és legenerál 200db véletlen kockadobást
és az eredményt eltárolja egy listában. A fgv térjen vissza a listával

A továbbiakban ezzel a listával dolg., az alábbi fgv-ekben:
számold meg hányszor dobtunk egyest, kettest, ... hatost!

Készíts cinkelt kockát! A hatost nagyobb valószínűséggel dobja!
A cinkelt kockával is futtasd le a fenti fgv-eket! Kiderül a csalás?
"""


def kockadobasok(lista):
    i:int = 0
    dob:int=0
    while(i<200):
        dob=int(random.random()*6+1)
        lista.append(dob)
        i+=1
    return lista


def hanyszorDobVmelySzambol(szam, lista):
    i:int=0
    hanyszor:int=0
    while(i<len(lista)):
        if(lista[i]==szam):
            hanyszor+=1
        i+=1
    return hanyszor

def cinkeltkocka(dobSzam,lista):
    