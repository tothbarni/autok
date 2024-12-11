import random
def lotto_szamok(): 
    lotto_szamok = []
    for i in range(5):
        lotto_szamok.append(random.randint(1, 100))
    print(*lotto_szamok, sep="; ")
    return lotto_szamok
    
def egyjegyuek_szama (szamok):
    db:int = 0
    for i in range(0, len(szamok)-1):
        if (szamok[i] > 0 and szamok[i] < 10):
            db += 1
    return db

def konzol_kiir(szoveg:str, db:int):
    print(f"{szoveg} {db}")

def file_kiir(db):
    f = open("szamok.txt", "a")
    f.write("II/F:\n")
    f.write(f"Az egyjegyűek száma: {db}")
    f.close()
