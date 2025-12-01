import os
import tkinter

# root init
root = tkinter.Tk()

# custom data
root.geometry("250x250")
root.resizable(False, False)
root.title("CW Cracker")

#functions
def inject() -> None:
    with open(f"C:/Users/{os.getlogin()}/AppData/LocalLow/Landfall Games/Content Warning/Saves/metaData.m", "w") as file:
        file.write("""SerializedMetaProgression, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null|{"MetaCoins":1000000,"UnlockedHats":[0,1,2,3,4,5,6,7,9,10,11,12,13,15,16,17,18,19,20,14,30,8,21,22,23,24,25,26,27,28,29],"UnlockedIslandUpgrades":[0,4,2,3,1]}""")
        file.close()
    button.config(text="DONE!", bg="#008800", activebackground="#008800", fg="#ffffff", activeforeground="#ffffff", command=None)

# button
button = tkinter.Button(root, text="CRACK", command=inject, width=40, height=25, bg="#880015", activebackground="#880015", fg="#ffffff", activeforeground="#ffffff")
button.pack()

# launch the program
if __name__ == '__main__':
    root.mainloop()