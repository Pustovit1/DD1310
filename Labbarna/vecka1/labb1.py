# Laboration 1
# DD1310
# Taras Pustovit CENMI1
# 2025-10-28 16:26
# Detta är en program som frågar användare om dens namn och ålder, efter att ha fått ålder i form av antalet år omvanldar den antalet år till antalet dagar, timmar, minuter. 

print("Hej! Vad heter du?")
name = input()
print(f"Trevligt att träffas {name}! Mitt namn är Taras. Hur gammal är du?")
while True:
    try:
        age = int(input())
        break   
    except:
        print("Ålder måste anges som ett tal utan bokstäver.")

days = age*365.25
hours = days*24
minutes = hours*60

if age < 18:
    print(f"Du är inte vuxen än men {age} år är också en långt tid! {age} år motsvarar {days} dagar, {hours} timmar, {minutes} minuter!")
else:
    print(f"Du är vuxen människa, {age} år är en lång tid! {age} år motsvarar {days} dagar, {hours} timmar, {minutes} minuter!")
print(f"Tyvärr har jag inte mer tid för att prata med dig. Hejdå {name}, tack för det trevliga samtalet!")
