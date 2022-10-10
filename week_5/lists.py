shopping_list = ["Steak", "Kiwi", "Golf Tees", "Moose"]
# index =            0       1         2          3
# lists are indexed from 0 ^^^^^^^
print(shopping_list)
print(shopping_list[1])
item_2 = shopping_list[1]
print(item_2)

def my_function():
    print("Bob")

ninja = my_function()
function_list = [ninja]
function_list[0]

embedded_lists = [[["Number of Cars", 3],["Car Brands", "Chevy", "Toyota", "Honda"],["MPG", 18, 35.5, 12]],[["Protein", "Veggies", "Rice", "Cheese"],["Chicken", "Steak", "Pork"], ["Peppers", "Onions", "Tomatoes", "Corn"],["White", "Brown"], ["Colby", "Swiss"]]]


print(embedded_lists[0][1][2], embedded_lists[0][2][2], embedded_lists[1][1][0], embedded_lists[1][4][1])

# print(str(embedded_lists[0][1][2])+ " " +str(embedded_lists[0][2][2])+" " +str(embedded_lists[1][1][0])+" "+str(embedded_lists[1][4][1]))