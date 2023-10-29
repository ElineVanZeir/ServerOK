import sys 
import json
from ping3 import ping

def main():
    if len(sys.argv) == 1:

        while True:

            print("maak uw keuze:")
            print("1. server toevoegen ")
            print("2. server verwijderen ")
            print("3. lijst tonen ")
            print("0. stoppen ")

            antw = int((input("geef uw keuze: ")))

            match antw:
                case 1: 
                    print("server toevoegen")
                    adres = input("wat is het adres? ")
                    TestOk = myping(adres)
                    Toevoegen(adres)
                    Check(adres, TestOk)
                case 2: 
                    print("server verwijderen")
                    adresVerwijderen = input("welk adres moet verwijderd worden?")
                    if Verwijderen(adresVerwijderen):
                        print("webadres verwijderd")
                    else:
                        print("webadres bestaat niet")
                case 3: 
                    print("lijst tonen ")
                    LijstTonen()
                case 0:
                    break
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
                Toevoegen(adres)
            case "deleteserver": 
                print("server verwijderen")
            case "listservers": 
                print("lijst tonen ")
            case _:
                print("niet geldig")

def Toevoegen(WebAdres):

    data = {}

    # data uit de file halen 
    with open("ingevoerde_data.json", "r") as data_file:
        data = json.load(data_file)
        
    # data toevoegen 

    data["servers"].append(WebAdres)

    # data terug wegschrijven 

    with open("ingevoerde_data.json", "w") as data_file:
        representation = json.dumps(data)
        data_file.write(representation)

    print("Gegevens zijn opgeslagen in 'ingevoerde_data.json'.")

def Check(WebAdres, Test):

    TestOK = {}

    # data uit de file halen 
        
    with open("testOK.json", "r") as data_file2:
        TestOK = json.load(data_file2)

    # data toevoegen 

    TestOK["servers"].append(WebAdres)
    TestOK["TestOK"].append(Test)

    # data terug wegschrijven 
   
    with open("testOK.json", "w") as data_file2:
        representation = json.dumps(TestOK)
        data_file2.write(representation)

    print("checks  zijn opgeslagen in 'testOK.json'.")

def Verwijderen(Webadres):
    data = {}
    with open("ingevoerde_data.json", "r") as data_file:
        data = json.load(data_file)
    if Webadres in data["servers"]:
        data["servers"].remove(Webadres)
        with open("ingevoerde_data.json", "w") as data_file:
            representation = json.dumps(data)
            data_file.write(representation)

        with open("testOK.json", "r") as bestand:
            server_data = json.load(bestand)

        if "server" in server_data:
            if Webadres in server_data["server"]:
                positie = server_data["server"].index(Webadres)
                server_data["server"].remove(Webadres)
                if positie < len(server_data["serverok"]):
                    del server_data["serverok"][positie]

        with open("serverok.json", "w") as data_file:
            representation = json.dumps(server_data)
            data_file.write(representation)
        return True
    else:
        return False
    
def LijstTonen():
    data = {}

    # data uit de file halen 
    with open("ingevoerde_data.json", "r") as data_file:
        data = json.load(data_file)
    for index, server in enumerate(data["servers"]):
        print(f"{index} : {server}")
    
def myping(host):
    resp = ping(host)

    if resp == False:
        return False
    else:
        return True
    
if __name__ == "__main__":
    main()