# PART 1 CRAP
import csv

filename = open("part2data", "r")

data_reader = list(csv.reader(filename))

dict1 = {}

for i in range(1, len(data_reader), 1):
    country = data_reader[i][1]
    date = data_reader[i][2]
    confirmed = int(data_reader[i][3])

    if country in dict1:
        values = dict1[country]
        for j in values:
            if j[0] == date:
                duplicate = j
                replace = True
            else:
                replace = False

        if replace:
            cases = int(duplicate[1]) + confirmed
            new_tuple = (date, cases)
            dict1[country].remove(duplicate)
            dict1[country].append(new_tuple)

        else:
            new_tuple= (date, int(confirmed))
            dict1[country].append(new_tuple)

    else:
        dict1[country] = [(date, int(confirmed))]
# END OF PART 1 CRAP

# Part 2
dict2 = {}
country_names = ["Bulgaria", "Serbia", "Croatia", "Canada"]

for i in country_names:
    for j in dict1:
        if i == j:
            dict2[i] = dict1[j]

print(dict2)
