#Taras Pustovit, Simona Acar
#2025/11/17
#DD1310 
#Det är en luffarschacksspel, I början uppmuntrans användare att mata in namn på spelarna och därefter fuýller man i spelplan med X och O
#Spelet håller koll på Tidigare drag och avgör om någon har vunnit. För att vinna behöver man få 3 av sina märken i rad/kolumn eller på diagonalen.
import random as random
def skriv_ut_spelplan(spelplan):
  """Skriver ut spelplanen
  Använder sig av "Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character
  Inparameter: spelplan (matris)
  Returvärde: Inget
  """
  print('    A   B   C  ')
  print('  ┏━━━┳━━━┳━━━┓')
  rad_räknare = 0
  for rad in spelplan:
    rad_räknare += 1
    print(str(rad_räknare) +' ┃', end=' ')
    for ruta in rad:
      print('' + ruta, end=' ')
      print('┃', end=' ')
    print()
    if rad_räknare < 3:          #Efter sista raden vill vi inte göra detta
      print('  ┣━━━╋━━━╋━━━┫')
  print('  ┗━━━┻━━━┻━━━┛')          #Utan istället detta            if "" not in rad:
    
def kontrollera_rader(spelplan):
  """Kontrollerar om det finns tre likadana tecken på någon rad och returnerar då True, annars False
  Inparameter: spelplan (matris)
  Returvärde: True om det finns vinnare annars False (booleskt värde)
  """
  for rad in spelplan:
    if ' ' not in rad:    #Vi vill inte att tre tomma rutor ska räknas som vinst
      if rad[0] == rad[1] == rad[2]:
        return True
            
    return False

def kontrollera_kolumner(spelplan):
  """Kontrollerar om det finns tre likadana tecken på någon kolumn och returnerar då True, annars False
  Inparameter: spelplan (matris)
  Returvärde: True om det finns vinnare annars False (booleskt värde)
  """
  if ' ' not in [spelplan[0][0], spelplan[1][0], spelplan[2][0]]:
    if spelplan[0][0] == spelplan[1][0] == spelplan[2][0]:
      return True
  elif ' ' not in [spelplan[0][1],spelplan[1][1], spelplan[2][1]]:
    if spelplan[0][1] == spelplan[1][1] == spelplan[2][1]:
      return True
  elif ' ' not in [spelplan[0][2],spelplan[1][2], spelplan[2][2]]:
    if spelplan[0][2] == spelplan[1][2] == spelplan[2][2]:
      return True
  else:
    return False

def kontrollera_diagonaler(spelplan):
  """Kontrollerar om det finns tre likadana tecken på diagonalen och returnerar då True, annars False
  Inparameter: spelplan (matris)
  Returvärde: True om det finns vinnare annars False (booleskt värde)
  """
  if ' ' not in [spelplan[2][0], spelplan[1][1], spelplan[0][2]]:
    if spelplan[2][0] == spelplan[1][1] == spelplan[0][2]:
      return True
  elif ' ' not in [spelplan[0][0],spelplan[1][1], spelplan[2][0]]:
    if spelplan[0][0] == spelplan[1][1] == spelplan[2][0]:
      return True
  else:
    return False
    
def finns_vinnare(spelplan):
  """
  Kontrollerar om det finns en vinnare efter varje drag.
  Inparameter: spelplan
  Returnvärde: True om det finns en vinnare annars False.
  """
  if kontrollera_diagonaler(spelplan) == True or kontrollera_kolumner(spelplan) == True or kontrollera_rader(spelplan) == True:
    return True
  else:
    return False


def är_oavgjort(spelplan):
  """Kontrollerar om det finns plats för en element i rad, om det finns inga platser kvar returneras False, annars True
  Inparameter: spelplan (matris)
  Returvärde: True om det finns vinnare annars False (booleskt värde)
  """
  for rad in spelplan:
    for element in rad:
      if element ==' ':
        return False
  return True

def tolka_inmatning(inmatning):
  """
  Tar emot en sträng som anger en position på spelplanen och returnerar
  rad och kolumn som vi kan indexera med i vår spelplan, exempel:
  A1 -> 0,0
  B3 -> 2,1 
  Inparameter: spelplan (matris)
  Returvärde: rad, kolumn (heltal, heltal)
  """
  bokstav = inmatning[0].upper()
  rad = int(inmatning[1])-1
  if bokstav == 'A':
    kolumn = 0
  elif bokstav == 'B':
    kolumn = 1
  elif bokstav == 'C':
    kolumn = 2
  return rad, kolumn


def spela(spelarnamn_1, spelarnamn_2):
  """
  Den starta spelet och håler ordning på vems tur det är.
  Inmatning: spelarnamn_1 och spelarnamn_2
  Returnvärde: Ingen
  """
  print("Då kör vi!")
  print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
  spelplan = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  spelarlista = [spelarnamn_1, spelarnamn_2]
  vems_tur = int(round(random.random(),0))
  while True:
    vems_tur = (vems_tur+1)% 2 #vems_tur ska aldrig bli 2, utan börja om igen på 0, %-är modul dvs resten vid heltals division.
    skriv_ut_spelplan(spelplan)
    if vems_tur == 0:
      markör = 'X'
    else:
      markör = 'O'
    while True:
      inmatning = input(str(spelarlista[vems_tur]) + "s tur att spela: ")
      rad,kolumn = tolka_inmatning(inmatning)
      if ' ' in spelplan[rad][kolumn]:
        spelplan[rad][kolumn] = markör
        break      
      else:
        print("Denna position är redan upptagen! Välj en annan: ")

    if finns_vinnare(spelplan) == True:
      skriv_ut_spelplan(spelplan)
      print("Grattis " + str(spelarlista[vems_tur]) + " du vann!")
      break
    elif är_oavgjort(spelplan) == True:
      skriv_ut_spelplan(spelplan)
      print("Det blev är_oavgjort!")
      break
        
def huvudfunktion():
  """
  Frågar användaren om spelarnamn_1 och splearnamn_2, därefter startar den spelet.
  Inmatning: Ingen
  Returnvärde: Spelarnamn 1 och 2
  """
  print("Hej och väkommen till Tre-i-rad!")
  spelarnamn_1 = input("Vad heter spelare 1? ")
  spelarnamn_2 = input("Vad heter spelare 2? ")
  spela(spelarnamn_1, spelarnamn_2)

huvudfunktion()