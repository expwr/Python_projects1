def directions():
    print("Turn left out of parking lot.")
    print("drive to stoplight and turn left.")
    print("drive one mile through canfield.")
    print("starbucks is across the street from sheetz")
    print("turn left into starbucks")

number_of_people = int(input("How many people are asking for directions"))

while number_of_people > 0:
    directions()
    number_of_people = number_of_people - 1