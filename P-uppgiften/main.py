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
        return f"{self.nummer:>3} | {self.beteckning:<3} | {self.namn:<15} | {self.vikt:>8.4f} u"
    
    def __lt__(self, other):
        """
        Sorterar atomer efter atomnummer.

        Inparameter: self, other
        Returnväde: sorterad_lista
        """
        return self.nummer < other.nummer

class Atomregister():

    def __init__(self):
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
    
def valet(prompt_text="Ange ett heltal"):
    """
    Programmet frågar användaren om ett tal och kotrollerar att svaret är angivet som heltal
    
    Inparameter: Atomregister(obejkt)
    Returnvärde: resultat(int)
    """
    while True:
        tal = input(f"{prompt_text}> ")
        try:
            resultat = int(tal)
            return resultat
        except ValueError:
            print("Ogiltig inmatning. Skriv ett heltal.")

def visa_meny(atomregister):
    """
    Skriver ut programmets huvudmeny och läser in användarens val.
    
    Inparameter: Atomregister(objekt)
    Returvärde:ingen
    """

    print(
        """
        ------------ MENY ------------
        1. Visa lista över alla atomer
        2. Träna på atomnummer
        3. Träna på atombeteckningar
        4. Träna på atomnamn
        5. Träna på atomvikt
        6. Avsluta
        ------------------------------
        """
    )
    val = valet("Välj ett alternativ (1-6)")
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
            träna(atomregister, 3)
            visa_meny(atomregister)
        case 6:
            print("Programmet avslutas. Fortsätt ha en fin dag!")
        case _:
            print("Felaktigt val. Välj ett tal mellan 1 och 6.")
            visa_meny(atomregister)

def visa_alla_atomer(atomregister):
    """
    Skriver ut en lista över alla atomer i atomregistret.

    Inparameter: atomregister(Atomregister-objekt)
    Returvärde: ingen
    """
    atomregister.atomLista.sort()
    print("------------- ALLA ATOMER ------------")
    print("Nr  | Sym | Namn            | Vikt (u)")
    print("----+-----+-----------------+---------")
    for atom in atomregister.atomLista:
        print(atom)
    print("---------------------------------- ---")

def svar_kontroll(atom, läge, alternativ = []):
     """
     Kontrollerar användarens svar och håller räkning på 3 försök
     
     Inparameter: Atom(objekt), läge(int), Atomregister(objekt)
     Returnvärde: Ingen
     """
     x = 0
     while(x < 3):
        if läge == 0:
            svar = valet(f"Försök {x + 1}/3 - Ditt svar: ")
            korrekt = svar == atom.atribut
        elif läge == 1:
            svar = input(f"Försök {x + 1}/3 - Ditt svar: ")
            korrekt = svar == str(atom.atribut)
        elif läge == 2:
            svar = valet(f"Försök {x + 1}/3 - Ditt svar: ")
            korrekt = alternativ[svar-1] == atom.vikt
        
        if korrekt:
            print("Rätt svar!")
            break
        else:
            print("Fel svar.")
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
            print(f"Vilket atomnummer har {atom.namn}?")
            svar_kontroll(atom, 0)
        case 1:
            atom.atribut = atom.beteckning
            print(f"Vilken atombeteckning har {atom.namn}?")
            svar_kontroll(atom, 1)
        case 2:
            atom.atribut = atom.namn
            print(f"Vilket namn har atomen {atom.beteckning}?")
            svar_kontroll(atom, 1)
        case 3:
            atom.atribut = atom.vikt
            print(f"Vilken vikt har {atom.namn}?")
            alternativ = [atom.vikt, atomregister.slumpad_atom().vikt, atomregister.slumpad_atom().vikt]
            random.shuffle(alternativ)
            n = 0
            for svaralternativ in alternativ:
                n += 1
                print(str(n) + ". " + str(svaralternativ))
            svar_kontroll(atom, 2, alternativ)

def huvudprogram():
    atomregister = Atomregister()
    atomregister.läs_in("avikt_med_position.txt")
    visa_meny(atomregister)
huvudprogram()