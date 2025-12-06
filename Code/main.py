""" LIBRARIES """

from sys import exit
from art import tprint
from colorama import Fore
from json import dump, load
from ast import literal_eval
from os.path import isfile, exists
from colorama.ansi import AnsiFore
from os import getlogin, listdir, system

""" VARIABLES """

# const data
VERSION_MAJOR: str = 1
VERSION_MINOR: str = 4
VERSION_PATCH: str = 0
PATH: str = f"C:/Users/{getlogin()}/AppData/LocalLow/Landfall Games/Content Warning/Saves"

# default data
MONEY: int = 1000000
MC_MONEY: int = 1000000
ISLAND_UPGRADES: list = list(range(0, 5))
UNLOCKED_HATS: list = list(range(0, 31))

""" FUNCTIONS """

# main 
def main() -> None:
    if not exists("data.json"):
        create_file()

    banner(Fore.MAGENTA, "The  Cracker Program", f"by Wormyy\nV. {VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}\n")
    asker()
    
# asks for a number, then calls a function
def asker() -> None:
    action: str = input("1. Start injection\n2. Overwrite values\n3. Go to default values\n4. Leave\n\n>>> ")
    match(action):
        case "1":
            inject()
        case "2":
            overwrite()
        case "3":
            go_to_default()
        case "4":
            leave(True)
        case _:
            print(Fore.RED + "\nUnknown option\n\n" + Fore.WHITE)
            asker()

# cre8s cul banner
def banner(color : AnsiFore = Fore.WHITE, title: str = "", subtitle: str = "") -> None:
    system("cls")
    print(color)
    tprint(title)
    print(subtitle + Fore.WHITE)

# overwrites injecting values
def overwrite() -> None:
    new_data: dict = {"World_money":None,"Mc_money":None,"Island_buildings":None,"Hats":None}
    for i in range(4):
        key_var: str = list(new_data.keys())[i]
        banner(Fore.LIGHTYELLOW_EX, "Rewrite  the value", f"Set a value for a \"{key_var}\" variable\nif you don't want to change the value of this variable press \"enter\"")
        
        new_value: str = input(">>> ")
        
        while True:
            if new_value.isdigit() and int(new_value) >= 0 or new_value == "":
                break
            else:
                print(Fore.RED + "Error! Cause: wrong value type" + Fore.WHITE)
                new_value: str = input(">>> ")
        
        if new_value == "":
            new_data[key_var] = gain_data()[key_var]
            continue
        else:
            new_data[key_var] = int(new_value) if i in [0, 1] else list(range(0, int(new_value) if int(new_value) <= 100 else 200))
    else:
        create_file(new_data)
        banner(Fore.GREEN, "Done!", "The values have been overwritten!\n")
        leave()

# brings default values back
def go_to_default():
    create_file()
    banner(Fore.GREEN, "Done!", "The values have been overwritten to default ones!\n")
    leave()

# cre8s/edits a file
def create_file(dictionary_to_write : dict = {"World_money": MONEY,"Mc_money":MC_MONEY,"Island_buildings":ISLAND_UPGRADES,"Hats":UNLOCKED_HATS}) -> None:
    with open("data.json", "w") as file:
        dump(dictionary_to_write, file)

# user action check
def leave(quit: bool = False) -> None:
    if quit:
        exit()
    else:    
        input("press \"enter\"\n>>> ")
        main()

# reads the file with data
def gain_data() -> dict:
    with open("data.json") as file:
        return load(file)

# injects
def inject() -> None:
    try: 
        gained_data: dict = gain_data()

    except FileNotFoundError:
        create_file()
        gained_data: dict = gain_data()

    finally:
        formatted_local_data : dict = {"MetaCoins":gained_data["Mc_money"],"UnlockedHats":gained_data["Hats"],"UnlockedIslandUpgrades":gained_data["Island_buildings"]}

        try:
            with open(PATH + "/metaData.m", "w") as file:
                file.write(f"SerializedMetaProgression, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null|{str(formatted_local_data).replace("'", "\"").replace(" ", "")}")
                file.close()

            for i in listdir(PATH):
                current_path = f"{PATH}/{i}"
                if isfile(current_path) and "Save" in i:

                    with open(current_path, 'r') as file:
                        file_data = file.read()
                        file.close()

                    file_dict: dict = literal_eval(str(file_data[97:]))
                    file_data: str = file_data[:97]

                    file_dict["Money"] = gained_data["World_money"]

                    with open(current_path, "w") as file:
                        file.write(f"{file_data}{str(file_dict).replace("'", "\"")}")
                        file.close()
            
            else:
                banner(Fore.GREEN, "Success!", "The game data has been overwritten successfully!")

        except Exception as e:
            banner(Fore.RED, "Failure!", f"something went wrong, here's an error:\n{e}")

        finally:
            print("\n\n")
            leave()

# Launches the program
if __name__ == '__main__':
    main()