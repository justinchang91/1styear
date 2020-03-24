# Program to practice string commands

string = "Hello my name is Gary Garington. I am also so attractive"

# Using .split()
words = string.split(" ")
print(words)
print(words[0])

# Using slice
piece = string[9:31]
print(piece)
piece_two = string[9:31:2]
print(piece_two)

# Using .find()
index_name = string.find("Gary")
print(index_name)
index_name_two = string[3:6].find("Gary")  # searches for Gary in range 3 to 6 (end is always exclusive)

# .upper() and .lower()
print(string.upper())
print(string.lower())

# using .replace()
print(string.replace("Gary", "Slary"))  # you can add a third parameter for count, if you want to replace more than 1
print(string.replace("Gar", "Slar", 2))  # adds the count

# using .strip()  Used to get rid of spaces before and after the string
string_two = "     hello      "
print(string_two)
print(string_two.split())




