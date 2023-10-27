print("maak uw keuze:")
print("1. server toevoegen ")
print("2. server verwijderen ")
print("3. lijst tonen ")

antw = int((input("geef uw keuze: ")))

match antw:
    case 1: 
        print("server toevoegen")
    case 2: 
        print("server verwijderen")
    case 3: 
        print("lijst tonen ")
    case _:
        print("niet geldig")