def evjarat(tipus, evjarat):
    if (evjarat < 2000):
        kor = "öreg autó"
    elif (evjarat == 2024):
        kor = "friss gyártás"
    else:
        kor = "átlagos korú"
    print(f"Ez az {tipus} {kor}")
    