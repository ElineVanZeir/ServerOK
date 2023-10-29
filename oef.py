import sys 
import json
from ping3 import ping
from jinja2 import Environment, FileSystemLoader

def main():
    if len(sys.argv) == 1:

        while True:

            print("maak uw keuze:")
            print("1. server toevoegen ")
            print("2. server checken ")
            print("3. server verwijderen ")
            print("4. lijst tonen ")
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
                    print("server checken")
                    adres = input("wat is het adres? ")
                    TestOk = myping(adres)
                    Check(adres, TestOk)
                case 3: 
                    print("server verwijderen")
                    adresVerwijderen = input("welk adres moet verwijderd worden? ")
                    Verwijderen(adresVerwijderen)
                case 4: 
                    print("lijst tonen ")
                    LijstTonen()
                case 0:
                    break
                case _:
                    print("niet geldig")

    else: 
        keuze = sys.argv[1]
        match keuze:
            case "management": 
                optie = sys.argv[2]
                print("management")
                match optie:
                    case "add":
                        adres = sys.argv[3]
                        print("server toevoegen")
                        Toevoegen(adres)
                    case "delete":
                        adres = sys.argv[3]
                        print("server verwijderen")
                        Verwijderen(adres)
                    case "list":
                        print("lijst tonen")
                        LijstTonen()
                    case _:
                        print("niet geldig")
            case "check": 
                print("CHECK UITVOEREN :")
                adres = sys.argv[2]
                TestOk = myping(adres)
                # Toevoegen(optie)
                Check(adres, TestOk)
                print(f"check uitgevoerd voor {adres}")
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
    Wegschrijven()

def Verwijderen(Webadres):
    data = {}
    server_data = {}
    with open("ingevoerde_data.json", "r") as data_file:
        data = json.load(data_file)
    if Webadres in data["servers"]:
        data["servers"].remove(Webadres)
        with open("ingevoerde_data.json", "w") as data_file:
            representation = json.dumps(data)
            data_file.write(representation)

    with open("testOK.json", "r") as bestand:
        server_data = json.load(bestand)

    if Webadres in server_data["servers"]:
        positie = server_data["servers"].index(Webadres)
        server_data["servers"].remove(Webadres)
        if positie < len(server_data["TestOK"]):
            del server_data["TestOK"][positie]

    with open("testOK.json", "w") as data_file:
        representation = json.dumps(server_data)
        data_file.write(representation) 

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

def Wegschrijven():

    with open('testOK.json', 'r') as json_file:
        data = json.load(json_file)


    servers = []
    for server_name, test_ok in zip(data['servers'], data['TestOK']):
        servers.append({'name': server_name, 'status': 'OK' if test_ok else 'Failed'})

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    output = template.render(servers=servers)

    with open('server_report.html', 'w') as html_file:
        html_file.write(output)

    print("HTML-pagina gegenereerd: server_report.html")

if __name__ == "__main__":
    main()