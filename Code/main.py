import os
from sys import exit
from art import tprint
from time import sleep
from colorama import Fore
from ast import literal_eval
from colorama.ansi import AnsiFore

VERSION = 1.1
PATH = f"C:/Users/{os.getlogin()}/AppData/LocalLow/Landfall Games/Content Warning/Saves"

#functions
def main() -> None:
    banner(Fore.BLUE, "Cracker", f"Content Warning Cracker\nby Wormyy\nv. {VERSION}\n")
    input("Press \"enter\" to start the injection\n>>>")
    inject()

def banner(color : AnsiFore = Fore.WHITE, title: str = "", subtitle: str = "") -> None:
    os.system("cls")
    print(color)
    tprint(title)
    print(subtitle + Fore.WHITE)

def timer(seconds : int = 5) -> None:
    for i in range(seconds):
        print(f"leaving in {seconds - i - 1} seconds.", end="\r" if i + 1 != seconds else "\n")
        sleep(1)
    else:
        print("Closing the app...")
        exit() # and i know that i can use the 'quit' key phrase but it gives an error at the last second

def inject() -> None:
    try:
        # Editing the data file
        with open(PATH + "/metaData.m", "w") as file:
            file.write(
                """SerializedMetaProgression, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null|{"MetaCoins":1000000,"UnlockedHats":[0,1,2,3,4,5,6,7,9,10,11,12,13,15,16,17,18,19,20,14,30,8,21,22,23,24,25,26,27,28,29],"UnlockedIslandUpgrades":[0,4,2,3,1]}"""
                )
            file.close()

        for i in os.listdir(PATH):
            current_path = f"{PATH}/{i}"
            if os.path.isfile(current_path) and "Save" in i:
                
                with open(current_path, 'r') as file:
                    file_data = file.read()
                    file.close()

                file_dict = literal_eval(str(file_data[97:]))
                file_data = file_data[:97]

                file_dict["Money"] = 1000000

                with open(current_path, "w") as file:
                    file.write(f"{file_data}{str(file_dict).replace("'", "\"")}")
                    file.close()

        # Success!
        banner(Fore.GREEN, "Success!", "The game data has been overwritten successfully!")

    except Exception as e:
        # Error!
        banner(Fore.RED, "Failure!", f"something went wrong, here's an error:\n{e}")

    finally:
        print("\n\n")
        timer()

# launch the program
if __name__ == '__main__':
    main()