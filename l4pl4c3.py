import requests
from functools import lru_cache
import os
from colorama import Fore, init

start_text = ("\nWelcome to " + Fore.LIGHTGREEN_EX + "L4PL4C3!",
              Fore.WHITE + "\n► Made by "+ Fore.LIGHTGREEN_EX + "doedalus",
              Fore.WHITE + "► GitHub: " + Fore.LIGHTGREEN_EX + "https://github.com/doedalus",
              Fore.WHITE + "► Version: " + Fore.LIGHTGREEN_EX + "1.0" + Fore.WHITE)

init(autoreset=True)

logo = Fore.LIGHTGREEN_EX + "\n" +r'''`7MMF'                 `7MM"""Mq.`7MMF'                 .g8"""bgd        
  MM                     MM   `MM. MM                 .dP'     `M        
  MM             ,AM     MM   ,M9  MM             ,AM dM'       `pd""b.  
  MM            AVMM     MMmmdM9   MM            AVMM MM        (O)  `8b 
  MM      ,   ,W' MM     MM        MM      ,   ,W' MM MM.            ,89 
  MM     ,M ,W'   MM     MM        MM     ,M ,W'   MM `Mb.     ,'  ""Yb. 
.JMMmmmmMMM AmmmmmMMmm .JMML.    .JMMmmmmMMM AmmmmmMMmm `"bmmmd'      88 
                  MM                               MM           (O)  .M' 
                  MM                               MM            bmmmd'''

@lru_cache(maxsize=32)
def get_info_about_ip(ip_address):
    space = 15
    r = requests.get(f"http://ipwho.is/{ip_address}", timeout=5).json()
    if not r["success"]:
        return None
    result = (
            "┌───────────────────────────────────────────────┐",
            ("│ IP address".ljust(space) + ": " + r["ip"][:30]).ljust(48) + "│",
            ("│ Success".ljust(space) + ": " + str(r["success"])[:30]).ljust(48) + "│",
            ("│ Type".ljust(space) + ": " + str(r["type"])[:30]).ljust(48) + "│",
            "│───────────────────────────────────────────────│",
            ("│ Continent".ljust(space) + ": " + r["continent"][:30]).ljust(48) + "│",
            ("│ Country".ljust(space) + ": " + r["country"][:30]).ljust(48) + "│",
            ("│ Region".ljust(space) + ": " + r["region"][:30]).ljust(48) + "│",
            ("│ City".ljust(space) + ": " + r["city"][:30]).ljust(48) + "│",
            ("│ Latitude".ljust(space) + ": " + str(r["latitude"])[:30]).ljust(48) + "│",
            ("│ Longitude".ljust(space) + ": " + str(r["longitude"])[:30]).ljust(48) + "│",
            ("│ Postal code".ljust(space) + ": " + r["postal"][:30]).ljust(48) + "│",
            "│───────────────────────────────────────────────│",
            ("│ ASN".ljust(space) + ": " + str(r["connection"]["asn"])[:30]).ljust(48) + "│",
            ("│ ORG".ljust(space) + ": " + str(r["connection"]["org"])[:30]).ljust(48) + "│",
            ("│ ISP".ljust(space) + ": " + str(r["connection"]["isp"])[:30]).ljust(48) + "│",
            "└───────────────────────────────────────────────┘")
    return result

@lru_cache(maxsize=1)
def get_my_ip():
    r = requests.get("https://api.ipify.org/").text
    return r

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(*start_text, sep="\n")
    print("\nPress Enter to continue...")
    input()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(logo)
        print("Menu:\n " + Fore.LIGHTGREEN_EX +  " [1] " + Fore.WHITE +  "Info about IP\n  " + Fore.LIGHTGREEN_EX +  "[2] " + Fore.WHITE +  "Info about my IP\n  " + Fore.LIGHTGREEN_EX +  "[3] " + Fore.WHITE +  "Exit\n")
        choice = input("Select option: " + Fore.LIGHTGREEN_EX)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print("Result:")
        if choice == "1":
            ip = input("Enter IP: " + Fore.LIGHTGREEN_EX)
            try:
                info = get_info_about_ip(ip)
                if info is None:
                    print(Fore.LIGHTRED_EX + "\n!---IP not found---!")
                else:
                    print(Fore.WHITE, end="")
                    print(*info, sep="\n")
            except:
                print(Fore.LIGHTRED_EX + "[Error] Please check your internet connection")

        elif choice == '2':
            try:
                ip = get_my_ip()
                info = get_info_about_ip(ip)
                if info is None:
                    print(Fore.LIGHTRED_EX + "\n!---Failed---!")
                else:
                    print(*info, sep="\n")
            except:
                print(Fore.LIGHTRED_EX + "\n[Error] Please check your internet connection")

        elif choice == '3':
            print("\nExit...")
            exit()

        else:
            print(Fore.LIGHTRED_EX + "\n!--option not found--!\n")

        print("\nPress Enter to return...")
        input()
