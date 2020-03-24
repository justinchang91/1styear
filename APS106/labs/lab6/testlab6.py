formula = "Na1Cl12"
stepper = 0
list1 = []

while stepper < len(formula):
    word = ""  # Erases word's value

    if 65 <= ord(formula[stepper]) <= 90 and 97 <= ord(formula[stepper+1]) <= 122:   # if it's a letter
        word += formula[stepper]  # Add the first letter to the word because you know it's a capital
        word += formula[stepper+1]

        list1.append(word)
        stepper += 2

    elif 65 <= ord(formula[stepper]) <= 90:
        word += formula[stepper]
        list1.append(word)
        stepper += 1

    else:  # if it's a number ONLY WORKS FOR SINGLE DIGITS
        if stepper + 1 < len(formula) and 48 <= ord(formula[stepper + 1]) <= 57:  # if the number is within
            word += formula[stepper]
            word += formula[stepper+1]
            list1.append(word)
            stepper += 2
        else:
            word += formula[stepper]
            list1.append(word)
            stepper += 1


# convert the list to a dictionary

dict1 = {}
for i in range(0, len(list1), 2):
    dict1[list1[i]] = list1[i+1]

print(dict1)


# Part 2

dict2 = {}
expr_coeffs = (2,1,5)
expr_molecs = ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1})

# Loop and multiply the coefficients to the molecules
j = 0
for molecule in expr_molecs:
    for atom in molecule:
        molecule[atom] *= expr_coeffs[j]

    j += 1

# Add the atoms to dict1
for molecule in expr_molecs:
    for atom in molecule:
        if atom in dict2:
            dict2[atom] += molecule[atom]
        else:
            dict2[atom] = molecule[atom]

print(dict2)


# Part 3

list1 = []
left_dict = {"C": 3, "H": 8, "O": 4}
right_dict = {"H": 8, "O": 10, "C": 3}

for atom in left_dict:
    if left_dict[atom] != right_dict[atom]:
        list1.append(atom)

print(set(list1))




