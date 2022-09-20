def pen_conv():
    amount = float(input("How many pennies do you have? "))
    dollars = divmod(amount, 100.00)
    print("Dollars: ", dollars[0])
    amount = round(dollars[1], 2)

    quarters = divmod(amount, 25.00)
    print("Quarters: ", quarters[0])
    amount = round(quarters[1], 2)

    dimes = divmod(amount, 10.00)
    print("Dimes: ", dimes[0])
    amount = round(dimes[1], 2)

    nickels = divmod(amount, 5.00)
    print("Nickels: ", nickels[0])
    amount = round(nickels[1], 2)
    
    penny = divmod(amount, 1.00)
    print("Pennies", penny)


pen_conv()