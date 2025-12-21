#Taras Pustovit, Lukas Liljestad
#Programmen skapar en inköpslista utifrån vilka recept användaren väljer.
#09/12/2025
from Recept import *
from Vara import *
from Inkopslista import *

def skapa_vara(text):
  """Delar upp en strängen på formatet namn; mängd enhet och skapar ett Vara-objekt:
  parametrar: text (formatet namn; mängd enhet)
  returnerar: Vara-objekt (Vara)"""
  delar = text.split(';')
  namn = delar[0].strip()
  mängd_enhet = delar[1].strip().split(' ')
  mängd = int(mängd_enhet[0])
  enhet = mängd_enhet[1]
  return Vara(namn, mängd, enhet)

def läs_in_recept(filnamn):
  """Läser in maträtter och deras ingredienser från fil till en lista
  parametrar: filnamn (str)
  returnerar: receptlista (list<Recept>)"""
  receptlista = []
  with open(filnamn, 'r', encoding='utf-8') as fil:
    for rad in fil:
      rad = rad.strip()
      maträtt, alla_varor = rad.split(':')
      maträtt = maträtt.strip()
      ingredienser = alla_varor.split(',')
      varor = []
      for vara in ingredienser:
        ingrediens = skapa_vara(vara.strip())
        varor.append(ingrediens)
      receptlista.append(Recept(maträtt, varor))
  return receptlista


def välj_recept(receptlista):
  """Ber användaren välja recept, lägger den valda recept-objekten i en ny lista som returneras
  parametrar: receptlista (list<Recept>)
  returnerar: valda_recept (list<Recept>)"""
  valda_recept = []
  while True:

    val = input('Välj ett recept(för att avsluta skriv "avsluta"): ')
    if val == "avsluta":
      break

    for recept in receptlista:
      if recept.maträtt == val:
        valda_recept.append(recept)
        print(f"Recept för {val} är sparad.")

  return valda_recept
      
  
def skapa_inköpslista(valda_recept):
  """Skapar en inköpslista efter de valda recepten, skriver ut inköpslistan på skärmen och returnerar den
  parametrar: valda_recept (list<Recept>)
  returnerar: inköpslista (Inköpslista<Recept>)"""
  inköpslista = Inköpslista() #Vårt Inköpslista-objekt som ska fyllas på med Vara-objekt och returneras.
  namn_varor = [] #Hjälp-lista där vi bara lägger in namnen på nya varor, så vi enklare kan kontrollera om en ingrediensen redan finns på inköpslistan.
  
  for recept in valda_recept:
    for vara in recept.ingredienser:
      if vara.namn not in namn_varor:
        namn_varor.append(vara.namn)
        inköpslista.append(vara)
      else:
        index = namn_varor.index(vara.namn)
        inköpslista[index].lägg_till_mängd(vara.mängd)
  
  print("\nInköpslista:")
  print(inköpslista)
  
  return inköpslista

      
  #Tips: Vi behöver kontrollera om ingrediensen redan finns i inköpslistan innan vi lägger till den. Använd namn_varor för att kolla detta.
  #Om den finns ska vi anropa metoden .lägg_till_mängd för det Vara-objektet. Använd namn_varor.index(x), där x är ingrediensens namn för att ta redan på vilket index den ingrediensen har i inköpslistan.
  #Annars ska vi lägga in ingrediensens namn i listan namn_varor och Vara-objektet på inköpslistan.
  
def skriv_till_fil(valda_recept, inköpslista):
  """
  Funktion skriver till ett txt dokument
  Inparametrar: valda_recept(list), inköpslista(list)
  Returnvärde: Ingen
  """
  with open("Labb7/lista.txt", "w") as fil:
    fil.write("För recepten: ")
    for recept in valda_recept:
      fil.write(recept.maträtt + ", ")
    fil.write("\n") 
    fil.write(str(inköpslista))

def main():
  filnamn = "Labb7/matratter.txt"
  list = läs_in_recept(filnamn)
  for recept in list:
    print(recept)
  valda_recept = välj_recept(list)
  for receptet in valda_recept:
    print(receptet)
  inköpslista = skapa_inköpslista(valda_recept)
  skriv_till_fil(valda_recept, inköpslista)

main()

