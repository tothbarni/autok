import bevezetes
import sorozat
import autom

print("I/A:")
tipus = input("Autó neve: ")
evjarat = int(input("Gyártási dátum: "))

print("\nI/B:")
bevezetes.evjarat(tipus, evjarat)

print("\nII/A, B, C:")
szamok = sorozat.lotto_szamok()

print("\nII/D, E:")
db = sorozat.egyjegyuek_szama(szamok)
sorozat.konzol_kiir("Az egyjegyűek száma:", db)

sorozat.file_kiir(db)

autom.konzol_kiir()