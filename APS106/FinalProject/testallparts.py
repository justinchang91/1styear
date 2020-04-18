# PART 1 CRAP
import csv


class Covid_Country:

    def __init__(self, country, data):
        self.country_name = country
        self.daily_count = data[country]

    def day_count(self, date):
        for dates in self.daily_count:
            if dates[0] == date:
                return dates[1]

        return None


class Split_Node:

    def __init__(self, split_number = 0, countries = [], left = None, right = None):
        self.split_number = split_number
        self.countries = countries
        self.left = left
        self.right = right

    def build_tree(self, country_list, date):
        the_sum = 0

        for country in country_list:
            the_sum += country.day_count(date)

        mean = the_sum/len(country_list)
        self.split_number = mean

        list1 = []
        list2 = []
        list3 = []

        for country in country_list:
            if country.day_count(date) < 0.7 * self.split_number:
                list1.append(country)
            elif country.day_count(date) > 1.3 * self.split_number:
                list2.append(country)
            else:
                list3.append(country)

        if len(list1) > 0:
            new_split_node = Split_Node()
            self.left = new_split_node
            new_split_node.build_tree(self, list1, date)

        if len(list2) > 0:
            new_split_node = Split_Node()
            self.right = new_split_node
            new_split_node.build_tree(self, list2, date)

        self.countries = list3

        return None


filename = open("a bit of covid data.txt", "r")

data_reader = list(csv.reader(filename))
print(data_reader[1])
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

print("Part 1: ")
print(dict1)
print()
# END OF PART 1 CRAP

# Part 2
dict2 = {}
country_names = ["Afghanistan"]

for i in country_names:
    for j in dict1:
        if i == j:
            dict2[i] = dict1[j]

print("Part 2: ")
print(dict2)
print()

# Part 3
afghanistan = Covid_Country("Afghanistan", dict1)
print("Part 3: ")
print(afghanistan.country_name)
print(afghanistan.daily_count)
print(afghanistan.day_count("2020-01-22"))

# Part 4

