"""
Lab 5 - Läser in resultat från en pilkastningstävling som finns lagrade på en fil och hanterar fel som kan finnas där.
Taras Pustovit, Lucas Lindberg
24/11/2025
"""

def hantera_rad(rad_sträng):
    """ Tar emot en rad i form av en sträng och returnerar en tupel bestående av ett namn (sträng) 
        och ett resultat (int) i den ordningen, alternativt returnerar den None, om raden är ogiltig.

        Alla rader som inte består av ett namn (minst ett tecken) och ett heltal med komma emellan är ogiltiga 

        Inparameter:    rad_sträng (str)
        Returvärde:     None eller en tupel med namn och poäng (tuple)
    """
    try: 
        uppdelad_rad = rad_sträng.split(",")
        if uppdelad_rad == ['\n']:
            print("Rad ignorerad pga: Tom rad")
            raise IndexError
        elif len(uppdelad_rad) != 2:
            print("Rad ignorerad pga: Fel antal delar")
            raise IndexError 
        elif int(uppdelad_rad[1]) > 50 or int(uppdelad_rad[1]<0):
            raise ValueError
        elif uppdelad_rad[0] == "":
            print("Rad ignorerad pga: Namn saknas")
            return None
        elif uppdelad_rad[1] == "":
            print("Rad ignorerad pga: Poäng saknas")
            return None
        else:
            namn = uppdelad_rad[0].strip()
            poäng_sträng = uppdelad_rad[1].strip()
            return (namn, int(poäng_sträng))
    except IndexError:
        return None
    except ValueError:
        print("Rad ignorerad pga: Ogiltig poäng")
        return None

def läs_resultat_från_fil(filnamn):
    """ Läser ifrån en fil och returnerar en lista av tupler som innehåller alla giltiga resultat från filen.
        Ska använda sig av funktionen hantera_rad()

        Inparameter:    ett filnamn (str)
        Returvärde:     en lista av tupler (list)
    """
    resultat = []
    with open(f"{filnamn}", "r") as infil:
        all_text = infil.readlines()
        for rad in all_text:
            hanterad_rad = hantera_rad(rad)
            if hanterad_rad != None:
                resultat.append(hanterad_rad)
    return resultat
    
    

def ta_ut_top_3(resultat):
    """ Tar emot en lista som sorteras. Därefter returneras de tre bästa resultaten.

        Inparameter:    lista av tupler (list)
        Returvärde:     en potentiellt kortare lista av tupler (list)
    """
    return sorted(resultat, key = lambda namn_poäng_par : namn_poäng_par[1], reverse = True)[:3]

def skriv_resultat_till_fil(top):
    """ Skriver ut top 3 till en annan textfil

        Inparameter:    lista av tupler (list)
        Returvärde:     Inga
    """
    with open("top_3.txt", "w") as fil:
        for element in top:
            fil.write(element[0] + " ")
            fil.write(str(element[1]) + "\n")

def main():
    """ Huvudfunktion"""
    filnamn = "lab5_in_fel.txt"
    resultat = läs_resultat_från_fil(filnamn)
    top_3 = ta_ut_top_3(resultat)
    skriv_resultat_till_fil(top_3)

    print()
    print("Top 3:")
    for par in top_3:
        print(par[0],":",par[1])

main()