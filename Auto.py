class Auto:
    def __init__(self, nev, ev):
        self.nev = nev
        self.ev = ev

    def __str__(self):
        return f"{self.nev} ({self.ev})"
