from random import *

class Atom():
    def __init__(self, beteckning, nummer, namn, vikt, kolumn, rad):
        """
        Skapar en ny atom.
        Inparameter: self, beteckning(str), namn(str), nummer(int), vikt(float)
        Returnväde: ingen
        """
        
        self.beteckning = beteckning
        self.nummer = nummer
        self.namn = namn
        self.vikt = vikt
        self.kolumn = kolumn
        self.rad = rad

    def __str__(self):
        """
        Returnerar en sträng som beskriver atomen
        Inparameter: self
        Returnväde: sträng
        """
        return (
            "Atomen: " + self.namn
            + " betecknas som: " + self.beteckning
            + " har atomnummer: " + str(self.nummer)
            + " och väger: " + str(self.vikt) + " U"
        )

class Atomregister():

    def __init__(self):
        """
        Skapar en tom datastruktur för atomer
        Inparameter:ingen
        Returnväde:ingen
        """ 
        self.atomer = []
    
    def __lt__(self, other, kriterie):
        """
        Sorterar atomer efter en av kriterierna.

        Inparameter: self, other, kriterie(str).
        Returnväde: sorterad_lista
        """
        if kriterie == "nummer":
            return self.nummer < other.nummer
        elif kriterie == "beteckning":
            return self.beteckning < other.beteckning
        elif kriterie == "namn":
            return self.namn < other.namn
        elif kriterie == "vikt":
            return self.vikt < other.vikt
        elif kriterie == "kolumn":
            return self.kolumn < other.kolumn
        elif kriterie == "rad":
            return self.rad < other.rad
        else:
            raise ValueError("Felaktigt kriterie, försök igen.")
    
    def läs_in(self, filnamn):
        """
        Funktion som läser in data från en fil.

        Inparameter: filnamn(str)
        Returnväde: atom (Atom-objekt)
        """
        with open(filnamn, "r", encoding="utf-8") as fil:
            for rad in fil:
                delar = rad.strip().split(" ")
                beteckning = delar[0]
                nummer = int(delar[1])
                namn = delar[2]
                vikt = float(delar[3])
                kolumn = int(delar[4])
                rad = int(delar[5])
                atom = Atom(beteckning, nummer, namn, vikt, kolumn, rad)
                self.atomer.append(atom)
            

    def hamta_slumpad_atom(self):
        """
        Returnerar en slumpmässigt vald atom.
        
        Inparameter: ingen
        Returvärde: Atom(objekt)
        """
         


def visa_meny(atomregister):
    """
    Skriver ut programmets huvudmeny och läser in användarens val.
    
    Inparameter:ingen
    Returvärde: val(int)
    """

    """
        Menyval:
        1. Visa lista över alla atomer
        2. Träna på atomnummer
        3. Träna på atombeteckningar
        4. Träna på atomnamn
        5. Sluta
    """ 
    val = int(input("Ange ditt val: "))
    while val != 5:
        if val == 1:
            visa_alla_atomer(atomregister)
        elif val == 2:
            trana_atomnummer(atomregister)
        elif val == 3:
            trana_atombeteckning(atomregister)
        elif val == 4:
            trana_atomnamn(atomregister)
        else:
            print("Felaktigt val, försök igen.")
        val = int(input("Ange ditt val: "))

def visa_alla_atomer(atomregister):
    """
    Skriver ut en lista över alla atomer i atomregistret.

    Inparameter: atomregister(Atomregister-objekt)
    Returvärde: ingen
    """
    for atom in atomregister.atomer:
        print(atom)

def trana_atomnummer(atomregister):
    """
    Träningsläge för atomnummer. 
    Programmet väljer en slumpmässig atom och frågar användaren vilket atomnummer atomen har. 
    Användaren har maximalt tre försök. Vid tre felaktiga försök visas rätt svar.
    
    Inpaarmeter:atomregister(Atomregister-objekt)
    Returnväde:Ingen
    """
    

def trana_atombeteckning(atomregister):
    """
    Träningsläge för atombeteckningar. 
    Användaren ska ange korrekt atombeteckning för en slumpad atom. Max tre försök tillåts.
    
    Inpaarmeter:atomregister(Atomregister-objekt)
    Returnväde:Ingen
    """
    pass


def trana_atomnamn(atomregister):
    """
    Träningsläge för atomnamn.
    Användaren ska ange korrekt atomnamn baserat på atombeteckning eller atomnummer.
    
    Inpaarmeter:atomregister(Atomregister-objekt)
    Returnväde:Ingen
    """
    pass

def huvudprogram():
    atomregister = Atomregister()
    atomregister.läs_in("avikt_med_position.txt")
    visa_meny(atomregister)
huvudprogram()