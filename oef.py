import sys 
import json
from ping3 import ping

def main():
    if len(sys.argv) == 1:

        print("maak uw keuze:")
        print("1. server toevoegen ")
        print("2. server verwijderen ")
        print("3. lijst tonen ")

        antw = int((input("geef uw keuze: ")))

        match antw:
            case 1: 
                print("server toevoegen")
                adres = input("wat is het adres? ")
                TestOk = myping(adres)
                Wegschrijven(adres,TestOk)
            case 2: 
                print("server verwijderen")
                
            case 3: 
                print("lijst tonen ")
            case _:
                print("niet geldig")

    else: 
        keuze = sys.argv[1]

        match keuze:
            case "addserver": 
                print("server toevoegen")
                adres = input("wat is het adres? ")
                #adres = sys.argv[2]
                TestOk = myping(adres)
                Wegschrijven(adres,TestOk)
            case "deleteserver": 
                print("server verwijderen")
            case "listservers": 
                print("lijst tonen ")
            case _:
                print("niet geldig")

def Wegschrijven(WebAdres, Test):

    data = {}
    with open("ingevoerde_data.json", "r") as data_file:
        data = json.load(data_file)
        
    with open("testOk", "r") as data_file2:
        TestOK = json.load(data_file2)

    data["servers"].append(WebAdres)
    TestOK["servers"].append(WebAdres)
    TestOK["TestOk"].append(Test)

    with open("ingevoerde_data.json", "w") as data_file:
        representation = json.dumps(data)
        data_file.write(representation)

    print("Gegevens zijn opgeslagen in 'ingevoerde_data.json'.")


def myping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True
    
if __name__ == "__main__":
    main()