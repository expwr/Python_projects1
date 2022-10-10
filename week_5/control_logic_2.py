char_name = input("What is your name:  ").title()
char_class = input("What type of adventurer are you? ").title()

def welcome_screen():
        if(char_name == "Ninja" and char_class == "Mage"):
            print("Hello Mage. Watch them fireballs.")
        elif(char_name == "Bob" or char_class == "Builder"):
            print("I bet you like to build things.")
        elif(char_name != "Bob" and char_name != "Ninja"):
            print("Hmmm... I don't think we've met.")
        elif(char_name == "Bob" or char_name == "Ninja"):
            print("I've figured one of you two would show up.")
        else:
            print("We've reached the final else.")

welcome_screen()          
print(char_name)      
 