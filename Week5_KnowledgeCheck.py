#Week 5 Knowledge Check

#Print Hello World.

print("hello world!")

#Create a list and print one of the values.

List = [1, 2, 3, 4, 5, 6, 7, 8]
print(List[3])

#Create a Dictionary populated with two keys and two values.
#Print one of those values.
albums = {
    "Let It Be": 1970,
    "Abbey Road": 1969
}

for key,value in albums.items():
    if key == "Abbey Road":
        print(value)

#Create a tuple with 4 values. Print one of them.

Beatlestuple = ("John", "Paul", "George", "Ringo")
print(Beatlestuple[3])