from time import sleep

import diana_code as sc



def the_answer():
    password = input("what is the answer to life, the universe and everything? ")


    if(password == "42"):
        print("Welcome wise one. I see you've traveled the Galaxy. Let's begin.")
        level_1()
    elif(password != "bob"):
        print("This is no time for jokes.")  
    elif(password == "tom"):
        print("Ah yes. The funny cat that chases that mouse.")
    else:
        print("I see you are new. Go get more experince and come back.")          

def level_1():
    print("THe man opens the door")
    sleep(2)
    sc.CLEAR_CONSOLE()
    print("An old wizard approaches you.")
    sleep(2)
    sc.CLEAR_CONSOLE()
    begin_quest = input("Are you ready to begin your adventures y/n ")
    if(begin_quest == "y"):
        sc.CLEAR_CONSOLE()
        print("The adventure begins...")
    else:
        print("You're correct. Best if you go get some sleep")



the_answer()