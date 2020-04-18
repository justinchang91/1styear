#####################################
#             Parts 1-4             #
#####################################

#Enter code for Part1 below:



def parse_covid19(filename):
    import csv
    csvfile = open(filename, "r")
    data_reader = list(csv.reader(csvfile))
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
                new_tuple = (date, int(confirmed))
                dict1[country].append(new_tuple)

        else:
            dict1[country] = [(date, int(confirmed))]

    return dict1


#Enter code for Part2 below:
def select_countries(country_names, covid19_data):
    dict2 = {}
    for i in country_names:
        for j in covid19_data:
            if i == j:
                dict2[i] = covid19_data[j]

    return dict2

#Enter code for Part3 below:    
class Covid_Country:

    def __init__(self, country_name, covid19_data):
        self.country_name = country_name
        self.daily_count = covid19_data[country]

    def day_count(self, date):
        for dates in self.daily_count:
            if dates[0] == date:
                return dates[1]

        return None

#Enter code for Part4 below:
class Split_Node:

    def __init__(self):
        self.split_number = 0
        self.countries = []
        self.left = None
        self.right = None

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
            new_split_node.build_tree(list1, date)

        if len(list2) > 0:
            new_split_node = Split_Node()
            self.right = new_split_node
            new_split_node.build_tree(list2, date)

        self.countries = list3

        return None

#####################################
#             Tests                 #
#####################################
def run_my_tests():
    '''
    (NoneType) -> NoneType
    Run the tests defined by the student
    '''
    
    # Change this variable to test different parts of the project.
    # Possible values: "Part 1", "Part 2", "Part 3", "Part 4", "all"
    test_what = "all" 

    # Tests for Part 1
    if test_what == "all" or test_what == "Part 1":
        pass

    # Tests for Part 2
    if test_what == "all" or test_what == "Part 2":
        pass

    # Tests for Part 3
    if test_what == "all" or test_what == "Part 3":
        pass

    # Tests for Part 4
    if test_what == "all" or test_what == "Part 4":
        pass   

# You can change the booleans below to decide if you want to run
# your tests or the visualization or both 

run_tests = True
run_visualization = True


#####################################
# Do not change anything below here #
#####################################
import matplotlib.pyplot as plt
from datetime import datetime
from project_helper import display_growth, display_tree


if __name__ == "__main__":

    if run_tests: 
        run_my_tests() 

    if run_visualization: 

        # load data via parse_covid19
        covid_dict = parse_covid19("Covid-19_data.csv")
        
        # select countries via select_countries 
        country_names = ["US","Italy","Spain","Germany"]
        sd = select_countries(country_names, covid_dict)
        
        # visualize graph via display_growth()
        display_growth(sd)
        
        # create Covid_country list 
        covid_countries = []
        date = '2020-03-21'
        for country in covid_dict:
            country = Covid_Country(country, covid_dict)
            if country.day_count(date):
                covid_countries.append(country)
        #for country in covid_dict:
        #    covid_countries.append(Covid_Country(country, covid_dict))
        
        #Create split_node and build tree
        date = '2020-03-21'
        sp_node = Split_Node()
        sp_node.build_tree(covid_countries,date)
        
        #Visualize the tree
        display_tree(sp_node, date)

