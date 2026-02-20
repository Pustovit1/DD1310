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
        self.atribut = ""

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
    
def valet(atomregister):
    """
    Programmet frågar användaren om ett tal och kotrollerar att svaret är angivet som heltal
    
    Inparameter: Atomregister(obejkt)
    Returnvärde: resultat(int)
    """
    tal = input(" ")
    try:
        resultat = int(tal) 
        return resultat
    except ValueError:
        print("Svara med heltal!")
        visa_meny(atomregister)

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
    val = valet(atomregister)
    match val:
        case 1:
            visa_alla_atomer(atomregister)
            visa_meny(atomregister)
        case 2:
            träna(atomregister, 0)
            visa_meny(atomregister)
        case 3:
            träna(atomregister, 1)
            visa_meny(atomregister)
        case 4:
            träna(atomregister, 2)
            visa_meny(atomregister)
        case 5:
            print("Programet avslutas. Forstätt ha en fin dag!")
        case 6:
            print("Felaktigt val, försök igen. Välj mellan 1-5")

def visa_alla_atomer(atomregister):
    """
    Skriver ut en lista över alla atomer i atomregistret.

    Inparameter: atomregister(Atomregister-objekt)
    Returvärde: ingen
    """
    atomregister.atomLista.sort()
    for atom in atomregister.atomLista:
        print(atom)

def svar_kontroll(atom, läge, atomregister):
     """
     Kontrollerar användarens svar och håller räkning på 3 försök
     
     Inparameter: Atom(objekt), läge(int), Atomregister(objekt)
     Returnvärde: Ingen
     """
     x = 0
     while(x<3):
        if läge == 0:
            svar = valet(atomregister)
        else:
            svar =input(" ")        
        
        if svar == atom.atribut:
            print("Du har svarat rätt!")
            break
        else:
            print("Du svarade fel")
            x += 1
            if x == 3:                        
                print(f"Rätt svar är: {atom.atribut}") 

def träna(atomregister, träningsläge):
    """ 
    Programmet väljer en slumpmässig atom och frågar användaren vilket atomnummer/atombeteckning/namn atomen har beroende på vilket läge använderen väljer. 
    Användaren har maximalt tre försök. Vid tre felaktiga försök visas rätt svar.
    
    Inpaarmeter:atomregister(Atomregister-objekt), träningsläge
    Returnväde:Ingen
    """
    atom = atomregister.slumpad_atom()
    match träningsläge:
        case 0:
            atom.atribut = atom.nummer
            print(f"Vilken atomnummer har {atom.namn}?")
            svar_kontroll(atom,0, atomregister)
        case 1:
            atom.atribut = atom.beteckning
            print(f"Vilken atombeteckning har {atom.namn}?")
            svar_kontroll(atom, 1, atomregister)
        case 2:
            atom.atribut = atom.namn
            print(f"Vilken namn har {atom.beteckning}?")
            svar_kontroll(atom, 1, atomregister)

def huvudprogram():
    atomregister = Atomregister()
    atomregister.läs_in("avikt_med_position.txt")
    visa_meny(atomregister)
huvudprogram()