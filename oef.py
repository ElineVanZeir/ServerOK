import sys 
import json

def main():
    if len(sys.argv) == 1:

        print("maak uw keuze:")
        print("1. server toevoegen ")
        print("2. server verwijderen ")
        print("3. lijst tonen ")

        antw = int((input("geef uw keuze: ")))

        match antw:
            case 1: 
                print("u koos voor : server toevoegen")
                adres = input("wat is het adres? ")
                Wegschrijven(adres)
            case 2: 
                print("server verwijderen")
            case 3: 
                print("lijst tonen ")
            case _:
                print("niet geldig")

    else: 
        keuze = int(sys.argv[1])

        match keuze:
            case 1: 
                print("u koos voor : server toevoegen")
                adres = input("wat is het adres? ")
                Wegschrijven(adres)
            case 2: 
                print("server verwijderen")
            case 3: 
                print("lijst tonen ")
            case _:
                print("niet geldig")

def Wegschrijven(WebAdres):
    # bestaande data uitlezen
    # WebAdres toevoegen aan bestaande lijst met servers
    # data terug wegschrijven
    data = {}
    with open("ingevoerde_data.json", "r") as data_file:
        # hier data echte beginwaarde geven
        data = json.load(data_file)
        # dan kan je aan data[servers]
        data["servers"].append(WebAdres)

    with open("ingevoerde_data.json", "w") as data_file:
        representation = json.dumps(data)
        # json.dump(data, data_file)
        data_file.write(representation)

    print("Gegevens zijn opgeslagen in 'ingevoerde_data.json'.")

if __name__ == "__main__":
    main()