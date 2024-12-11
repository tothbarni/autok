from Auto import Auto

def beolvas(fajlnev:str="auto.txt", autok=[]):
    fajlom = open(fajlnev, "r", encoding="UTF-8")
    next(fajlom)
    tobbi_sor = fajlom.readlines()
    for sor in tobbi_sor:
        sor = sor.strip()
        sor_lista = sor.split("$")
        auto = Auto(sor_lista[0], int(sor_lista[1]))
        autok.append(auto)

    fajlom.close()
    return autok

def flotta(autok):
    return len(autok)

def legfiatalabb(autok):
    legfiatalabb_auto = autok[0]
    for i in range(1, len(autok)):
        if autok[i].ev > legfiatalabb_auto.ev:
            legfiatalabb_auto = autok[i]
    return legfiatalabb_auto

def atlag_kor(autok):
    aktualis_ev = 2024
    osszeg = 0
    for i in range(len(autok)):
        osszeg += aktualis_ev - autok[i].ev
    atlag = osszeg / len(autok)
    return atlag

def konzol_kiir():
    autok = beolvas()
    print("III/Flotta:")
    print(f"Autók száma: {flotta(autok)}.")
    
    legfiatalabb_auto = legfiatalabb(autok)
    print(f"III/Legfiatalabb")
    print(f"A legfiatalabb autó: {legfiatalabb_auto.nev} ({legfiatalabb_auto.ev}).")
    
    print("III/Átlag kor")
    print(f"Az autók átlagos kora: {atlag_kor(autok):.2f} év.")
