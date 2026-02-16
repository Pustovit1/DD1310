import random

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
            self.namn
            + " Beteckning: " + self.beteckning
            + " Atomnummer: " + str(self.nummer)
            + " Vikt: " + str(self.vikt) + " U"
        )
    
    def __lt__(self, other):
        """
        Sorterar atomer efter atomnummer.

        Inparameter: self, other
        Returnväde: sorterad_lista
        """
        return self.nummer < other.nummer

class Atomregister():

    def __init__(self,):
        """
        Skapar en tom datastruktur för atomer
        Inparameter:ingen
        Returnväde:ingen
        """ 
        self.atomLista = []
    
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
                self.atomLista.append(atom)
                
    def slumpad_atom(self):
        """
        Returnerar en slumpmässigt vald atom.
        
        Inparameter: ingen
        Returvärde: Atom(objekt)
        """
        return self.atomLista[random.randrange(0, len(self.atomLista), 1)]
    



def visa_meny(atomregister):
    """
    Skriver ut programmets huvudmeny och läser in användarens val.
    
    Inparameter:ingen
    Returvärde: val(int)
    """

    print("""
        Menyval:
        1. Visa lista över alla atomer
        2. Träna på atomnummer
        3. Träna på atombeteckningar
        4. Träna på atomnamn
        5. Avsluta
    """)
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
    atomregister.atomLista.sort()
    for atom in atomregister.atomLista:
        print(atom)


def trana_atomnummer(atomregister):
    """
    Träningsläge för atomnummer. 
    Programmet väljer en slumpmässig atom och frågar användaren vilket atomnummer atomen har. 
    Användaren har maximalt tre försök. Vid tre felaktiga försök visas rätt svar.
    
    Inpaarmeter:atomregister(Atomregister-objekt)
    Returnväde:Ingen
    """
    atom = atomregister.slumpad_atom()
    x = 0
    while(x<3):
        print(f"Vilken atomnummer har {atom.namn}?")
        try:
            svar = int(input(" "))
        except ValueError:
            print("Skriv ditt svar med heltal.")
        if svar == atom.nummer:
            print("Du har svarat rätt!")
            break
        else:
            print("Du svarade fel")
            x += 1
    if x == 3:
        print(f"{atom.namn} har atomnummer: {atom.nummer}") 
    
    

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