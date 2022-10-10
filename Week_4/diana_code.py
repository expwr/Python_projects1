import os
from time import sleep

def CLEAR_CONSOLE():
    # Windows
    if os.name == "nt":
        return os.system("cls")

    # For Mac & Linux
    else: 
        return os.system("clear")    


print("hello there.")
sleep(2)
CLEAR_CONSOLE()
print("It worked????")        
