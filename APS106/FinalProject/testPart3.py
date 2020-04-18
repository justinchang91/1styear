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


filename = open("a bit of covid data.txt", "r")

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

afghanistan = Covid_Country("Afghanistan", filename)

print(afghanistan.country_name)