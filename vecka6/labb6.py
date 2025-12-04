
#Taras Pustovit, Ellen Thermaenius
#2025-12-02
#Det här programmet håller koll på influencers. Läser in dessa från fil, kan göra inlägg etc för att ändra sina siffror och allt sparas på fil innan programmet avslutas.

from datetime import * #datetime används för datumhantering

#Klassdefinition
class Influencer:
    """En klass som beskriver en influencer. Ett objekt av klassen har attributen användarnamn(str), antal_föjare(int), datum_senaste_inlägg(date), intäkter(float)"""
    def __init__(self, användarnamn, antal_följare, datum_senaste_inlägg, intäkter): #konstruktor
        self.användarnamn = användarnamn
        self.antal_följare = antal_följare
        self.datum_senaste_inlägg = datum_senaste_inlägg
        self.intäkter = intäkter 

    def __str__(self):#str-metod 
        return self.användarnamn + " har " + str(self.antal_följare) + " antal följare, senaste inlägget var: " + str(self.datum_senaste_inlägg) + ", Intäkter: " + str(self.intäkter) + "kr."
    
    #lt-metod
    def __lt__(self, other):
       """En funktion som sorterar influencers utifrån antal följare (Lägst till högst)
       Parameter: self, other
       Returnvärde: True eller False"""
       return self.antal_följare < other.antal_följare

    #gör_inlägg-metod
    def gör_inlägg(self):
        """Skappar inlägg för en specifik influencer. Antal följare ökar med 100 och datumet för senaste inlägg ändras till dagens datum
        Parameter: self
        Returnvärde: Ingen"""
        self.antal_följare += 100
        self.datum_senaste_inlägg = date.today()
        print(f"{self.användarnamn} har gjort ny intlägg och antal följare har ökat till: {self.antal_följare}.")
    
    
    #gör_reklam-metod
    def gör_reklam(self):
        """Gör reklam om infuencern har mer än 1000 följare, Intäkter ökar med 2000 och antal följare minskar med 100
        Parameter: self
        Returnvärde: Ingen"""
        if self.antal_följare > 1000:
            self.intäkter += 2000
            self.antal_följare -= 100
            print(f"{self.användarnamn} har gjort ett reklam, vilket ledde till att han intäkter har ökat till: {self.intäkter}, men antal följare minskade till: {self.antal_följare}")
        else:
            print("Du har inte tillräckligt med följare")
        
    def vald_influencer(self): #hjälpmetod för utskrift, låt den vara kvar i klassen
        """Skriver ut att influencern valts.
        Parameter: self
        Returvärde: inget"""
        print("Hittade " + self.användarnamn + " profil, vad ska jag göra nu?")

def läs_influencers(filnamn):
    """Funktion för att läsa in alla influencers som finns i filen och utifrån det skapa objekt av klassen ovan.
       Inparameter: filnamn - namn på filen som innehåller datat om alla influencers (str).
       Returvärde: influencerlista - alla influencerssobjket (lista)"""
    infil = open(filnamn,"r", encoding = "utf-8")
    influencerlista = []
    for rad in infil:
        rad = rad.strip()
        delar = rad.split(" ")
        influencer = Influencer(delar[0],int(delar[1]),date.fromisoformat(delar[2]), float(delar[3]))
        influencerlista.append(influencer)
    return influencerlista

def välj_aktivitet():
    """Funktion för att välja aktivitet som influencern ska utföra under menyval 2.
    Parameter: Ingen
    Returvärde: valet som användaren matar in (int)"""
    val = int(input("\n\t1. Be influencern att göra inlägg \
                     \n\t2. Be influencern göra reklam \
                     \n\t3. Återgå till huvudmenyn \
                     \n\tVad väljer du? "))
    return val


def utför_aktivitet(namn_influencer, influencerlista):
    """Funktion för att utföra aktivitet som användaren valt.
    Inparameter: namn_influencer - namn som användaren valt att leta upp (str), influencerLista - alla influencers (lista)
    Returvärde: Inget, funktionen anropar antingen metoden gör_inlägg() eller gör_reklam() samt funktionen välja_aktivitet() beroende på vad användaren matat in."""
    for i in range(len(influencerlista)):
        if influencerlista[i].användarnamn == namn_influencer:
            influencer = influencerlista[i]
            influencer.vald_influencer()
            val = välj_aktivitet()
            while val !=3:
                if val == 1: 
                    influencer.gör_inlägg()
                elif val == 2: 
                    influencer.gör_reklam()
                else: 
                    print("Du har inte angett en siffra mellan 1-3, vänligen försök igen")
                val = välj_aktivitet()

def spara(filnamn, influencerlista):
    """Funktion för att spara status på alla influencers
    Inparameter: filnamn på filen (str), influencerlista) (lista med Influencer-objekt)
    Returvärde: inget returvärde då filen sparas i funktionen"""
    with open(filnamn, "w") as infill:
        for influencer in influencerlista:
           infill.write(influencer.användarnamn + " " + str(influencer.antal_följare) + " " + str(influencer.datum_senaste_inlägg) + " " + str(influencer.intäkter) + "\n")

def huvudfunktion():
    """Funktion som hälsar välkommen samt visar huvudmenyn"""
    
    filnamn = "influencers.txt"
    lista = läs_influencers(filnamn)
    lista.sort() 
    val = 0
    print("Välkommen till Influenceramera! Vad kan jag stå till tjänst med?")
    while val != 3:
        print("\n Du har följande alternativ: \
              \n\t1. Lista alla influencers och deras status\
              \n\t2. Leta upp en influencers profil\
              \n\t3. Spara och avsluta\
              \n\tVad väljer du? ", end = "")
        try:
            val = int(input())
        except ValueError:
            print("Det där var tyvärr inte ett giltigt menyval, försök igen")
            continue
        if val == 1:
            lista.sort()
            print()
            for influencer in lista:
                print(influencer)    
        elif val == 2:
            profil = input("\nVilken profil vill du att jag letar upp?: ")
            utför_aktivitet(profil, lista)                
        elif val == 3: 
            spara(filnamn, lista)
            print("Programmet avslutas. Tack för att du använder Influenceramera!")    
        else: 
            print("Du har inte angett en siffra mellan 1-3, försök igen.")


huvudfunktion()