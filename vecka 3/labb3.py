print("Välkommen till programmet som håller koll på dina grupper!")
ANTAL_GRUPPER = 3
grupper = {}
ständig_medlem = input("Vad heter du? ")
for i in range(ANTAL_GRUPPER):
    gruppnamn = input("Vad heter grupp nr " + str(i+1) + "? ")
    grupper[gruppnamn] = [ständig_medlem]
val = 0
while val != 5:
    print("Huvudmeny\n1. Se alla grupper och dess medlemmar\
    \n2. Lägg till medlem i en grupp\
    \n3. Ta bort en medlem ur en grupp\
    \n4. Se vem som är ordförande i varje grupp\
    \n5. Avsluta")
    val = int(input("Vad vill du göra? "))
    if val == 1:
        print("\nAlla grupper och deras medlemmar:")
        for grupp in grupper.keys():
            print(grupp, "har medlemmarna:", end=" ")
            for medlem in grupper[grupp]:
                print(medlem, end=" ")
    elif val == 2:
        grupp = input("Vad heter gruppen du ska lägga till en medlem till? ")
        if grupp in grupper:
            ny = input("Vad heter den nya medlemmen? ")
            grupper[grupp].append(ny)
        else:
            print("Den gruppen finns inte.")
    elif val == 3:
        grupp = input("Vad heter gruppen som medlemmen ska gå ur? ")
        if grupp in grupper:
            medlem = input("Vad heter medlemmen som ska gå ur gruppen? ")
            if medlem == ständig_medlem:
                print("Denna medlem är ständig och kan inte tas bort.")
            elif medlem in grupper[grupp]:
                grupper[grupp].remove(medlem)
            else:
                print(f"{medlem} finns inte i gruppen {grupp}.")
        else:
            print("Den gruppen finns inte.")
    elif val == 4:
         for gruppnamn in grupper.keys():
            medlemmar = grupper[gruppnamn]
            ordf = ständig_medlem
            for i in range(len(medlemmar)):
                medlem = medlemmar[i]
                if len(medlem) > len(ordf):
                    ordf = medlem
            print(f"Ordförande i grupp {gruppnamn} är {ordf}")
    elif val == 5:
        print("Programmet avslutas")
    else:
        print("Inte rätt siffra, välj från menyn.")

