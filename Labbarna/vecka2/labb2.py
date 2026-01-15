#Laboration 2
#Taras Pustovit, Julia Lundquist
#04/11/2025
#Vårt program kommer att koventera Celsius till Farenheit, pounds till kilogram och meter till amerikanska mil.
print("""Hej, välkommen till vårt program!
Vilken konvertering vill du göra?""")

while True:
    answer = int(input("""
    1. Celsius till Farenheit
    2. Pounds till kilogram
    3. Meter till amerikanska mil
    4. Avsluta program
    Välj 1-4: """))
    if answer == 1:
        celsius = float(input("Ange grader i Celsius: "))
        farenheit = 1.8 * celsius + 32
        print(f"{celsius} grader Celsius motsvarar {farenheit} grader Farenheit.")
    elif answer == 2:
        pounds = float(input("Ange vikt i pounds: "))
        kilogram = 2.2046 * pounds
        print(f"{pounds} pounds motsvarar {kilogram} kilogram.")
    elif answer == 3:
        meter = float(input("Ange sträckan i meter: "))
        miles = meter / 1609.3
        print(f"{meter} meter motsvarar {miles} amerikanska mil.")
    elif answer == 4:
        print("Tack för att du använde vårt program! Ha en fin dag!")
        break
    else:
        print("Välj ett tal mellan 1-4! skriv tal i siffror!")