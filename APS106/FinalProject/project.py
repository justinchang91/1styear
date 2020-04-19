#####################################
#             Parts 1-4             #
#####################################

#Enter code for Part1 below:



def parse_covid19(filename):
    import csv
    csvfile = open(filename, "r")
    data_reader = list(csv.reader(csvfile))
    dict1 = {}

    # Looping through the rows of the CSV file
    for i in range(1, len(data_reader), 1):
        # Breaking the rows down into their respective categories
        country = data_reader[i][1]
        date = data_reader[i][2]
        confirmed = int(data_reader[i][3])

        if country in dict1: # Check to see if the country is already in the dictionary
            values = dict1[country]
            for j in values:
                if j[0] == date:
                    duplicate = j
                    replace = True
                else:
                    replace = False

            if replace:
                cases = int(duplicate[1]) + confirmed  # figure out the new amount of cases (adding the new to the old)
                new_tuple = (date, cases)  # make a new tuple
                dict1[country].remove(duplicate)  # remove the old tuple from dict
                dict1[country].append(new_tuple)  # add the new tuple to dict

            else:  # if the country is not already in the dictionary
                new_tuple = (date, int(confirmed))
                dict1[country].append(new_tuple)

        else:
            dict1[country] = [(date, int(confirmed))]

    return dict1


#Enter code for Part2 below:
def select_countries(country_names, covid19_data):
    dict2 = {}
    # Find the countries in country_names that are also in covid19_data
    for i in country_names:
        for j in covid19_data:
            if i == j:
                dict2[i] = covid19_data[j]  # Put that country and its data into the new dictionary

    return dict2

#Enter code for Part3 below:    
class Covid_Country:

    def __init__(self, country_name, covid19_data):
        self.country_name = country_name
        self.daily_count = covid19_data[country_name]

    def day_count(self, date):
        for dates in self.daily_count:
            if dates[0] == date:  # If the date has cases in this specific country
                return dates[1]  # return the number of cases this country has at this specific date

        return None  # if there's no date for that country, return None

#Enter code for Part4 below:
class Split_Node:

    def __init__(self):  # Assign default values
        self.split_number = 0
        self.countries = []
        self.left = None
        self.right = None

    def build_tree(self, country_list, date):
        the_sum = 0

        for country in country_list:  # get the sum of the cases for each country at the specific date
            the_sum += country.day_count(date)

        mean = the_sum/len(country_list)
        self.split_number = mean  # Calculate the mean then assign it to the split_number

        # Create 3 empty lists
        list1 = []
        list2 = []
        list3 = []

        for country in country_list:  # Assign each country to a list
            if country.day_count(date) < 0.7 * self.split_number:
                list1.append(country)
            elif country.day_count(date) > 1.3 * self.split_number:
                list2.append(country)
            else:
                list3.append(country)

        if len(list1) > 0:
            new_split_node = Split_Node()  # Create a new split node
            self.left = new_split_node  # Assign this split node to the current split node's left
            new_split_node.build_tree(list1, date)  # call the build_tree function again but with list1 countries

        if len(list2) > 0:
            new_split_node = Split_Node()  # Create a new split node
            self.right = new_split_node  # Assign the split node to the current split node's right
            new_split_node.build_tree(list2, date)  # Call build_tree again but with list2 countries

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

    # TEST 1
    # Input:
    # Province_State, Country_Region, Last_Update, Confirmed, Deaths
    # ,Afghanistan,2020-01-22,0,0
    # ,Afghanistan,2020-01-23,34,0

    # Expected output:
    # {'Afghanistan': [('2020-01-22', 0), ('2020-01-23', 34)]}

    # Comments:
    # This is a test that checks to see if my code can read the csv file correctly, and format the information from that
    # file the right way. Meaning, correct data types and structures. I proposed this test because I need to be pulling
    # the correct information from the file and this information must all be formatted correctly, according to what is
    # asked in the instructions.

    # TEST 2
    # Input:
    # Province_State,Country_Region,Last_Update,Confirmed,Deaths
    # ,Afghanistan,2020-01-22,0,0
    # ,Afghanistan,2020-01-22,12,0
    # ,Afghanistan,2020-01-23,34,0

    # Expected output:
    # {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)]}

    # Comments:
    # This is a test that checks to see if the number of cases on a certain date is the sum of all the cases on that
    # date. This test is needed in case in the csv file there are multiple entries on the same date.

    # Test 3:
    # Input:
    # Province_State,Country_Region,Last_Update,Confirmed,Deaths
    # ,Afghanistan,2020-01-22,0,0
    # ,Afghanistan,2020-01-22,12,0
    # ,Afghanistan,2020-01-23,34,0
    # Ontario,Canada,2020-01-23,19,0

    # Expected output:
    # {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}

    # Comments:
    # This is a test that checks to see if you can add a sub region of that country (e.g provinces) and have the code
    # still work. This is needed because there are many countries that have this such as Canada or the US.

    # {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}

    # The code for part 1:
    if test_what == "all" or test_what == "Part 1":
        stuff = parse_covid19("a bit of covid data.txt")

        print("Part 1: ")
        print(stuff)
        print()

    # Tests for Part 2

    # TEST 1
    # Input:
    # test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
    # names = ["Afghanistan"]

    # Expected output:
    # {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)]}

    # Comments:
    # This is just a general test to see if my code can search for specific countries and make a new dict with only the
    # specified countries in it. Also tests general formatting. I need this test because in order for everything to run
    # smoothly, proper formatting of data structures and types are key.

    # TEST 2
    # Input:
    # test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
    # names = []

    # Expected output:
    # {}

    # Comments
    # This is just a test to see what happens if there are no specified countries. This test is needed because I don't
    # want there to be an error just because you ran the function but there was nothing being asked for (probably will
    # never happen but someone might try it).

    # TEST 3:
    # Input:
    # test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
    # names = ["Uganda"]

    # Expected output:
    # {}

    # Comments
    # This is a test to see what happens if you're searching for a country that doesn't exist in the dictionary. This
    # is important in case someone wants to look for a country, and it's not in the dictionary, you don't want a big
    # error going everywhere.

    # The code for part 2:
    if test_what == "all" or test_what == "Part 2":
        test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
        names = ["Uganda"]

        stuff2 = select_countries(names, test_dict)

        print("Part 2: ")
        print(stuff2)
        print()

    # Tests for Part 3

    # TEST 1:
    # Input:
    # test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
    # place = "Afghanistan"
    # date = "2020-01-22"

    # Expected output:
    # Afghanistan
    # [('2020-01-22', 12), ('2020-01-23', 34)]
    # 12

    # Comment:
    # This is just a general test to see if the constructor and the day_count(date) function have the correct output
    # and formatting. Important because proper formatting ensures the rest of the program flows smoothly.

    # TEST 2:
    # Input:
    # test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
    # place = "Afghanistan"
    # date = "2020-01-13"

    # Expected output:
    # Afghanistan
    # [('2020-01-22', 12), ('2020-01-23', 34)]
    # None

    # Comments:
    # This is just a test to see what happens if the date given to day_count(date) does not exist in the dictionary.
    # If it doesn't exist, it should return None. This is important just in case someone gives a date that doesn't
    # exist. You don't want the program bugging out.

    # The code for part 3
    if test_what == "all" or test_what == "Part 3":
        test_dict = {'Afghanistan': [('2020-01-22', 12), ('2020-01-23', 34)], 'Canada': [('2020-01-23', 19)]}
        place = "Afghanistan"
        date = "2020-01-13"

        afghanistan = Covid_Country(place, test_dict)
        print("Part 3: ")
        print(afghanistan.country_name)
        print(afghanistan.daily_count)
        print(afghanistan.day_count(date))
        print()

    # Tests for Part 4

    # TEST 1
    # Input:
    # spliteth_nodeth = Split_Node()

    # Expected output when printing out the attributes:
    # 0
    # []
    # None
    # None

    # Comments:
    # This is just code to test if my constructor has the proper default values that I set it to. Important that the
    # default values are all correct and not something totally random.

    # TEST 2

    # For this test, I'm making another CSV file just to test if the logic of my code works. I have added it to the doc.
    # Input: (The CSV File)
    # Province_State,Country_Region,Last_Update,Confirmed,Deaths
    # ,Afghanistan,2020-03-21,2,0
    # Ontario,Canada,2020-03-21,19,0
    # Quebec,Canada,2020-03-21,30,0
    # New York,US,2020-03-21,50,0

    # Expected output of .split_number (the mean)
    # 33.666666 (Since Canada is in there twice, the cases get summed, 19+30 = 49)

    # Expected output of list1 (left node) since 0.7 * 33.6666 = 23.566
    # [Afghanistan]
    # Split number of list1
    # 2

    # Expected output of list2 (right node) since 1.3 * 33.666 = 43.76
    # [US, Canada] (50 and 49 respectively)
    # Split number of list2
    # 49.5

    # Expected output of list3
    # []

    # Basically this test is just to see if my nodes, and their split numbers are correct. To do this, I created
    # another CSV file with small amount of data so my binary tree would be small. Then I followed my code and
    # calculated what would be put in which list and what the split numbers would be. From there, I used the display
    # binary tree helper function to manually check if my output matched up with what I calculated. This test is needed
    # because it allows me to see if I'm getting the proper values and tree on a small data scale compared to the real
    # data file which is huge.

    # The code for part 4
    if test_what == "all" or test_what == "Part 4":
        # For test 1:
        spliteth_nodeth = Split_Node()
        print("For test 1: ")
        print(spliteth_nodeth.split_number)
        print(spliteth_nodeth.countries)
        print(spliteth_nodeth.left)
        print(spliteth_nodeth.right)

        # For test 2
        print("\nFor test 2: ")
        date = '2020-03-21'
        dict_thing = parse_covid19("a bit of covid data.txt")
        countries = []
        for country in dict_thing:
            country_object = Covid_Country(country, dict_thing)
            if country_object.day_count(date):
                countries.append(country_object)

        test_node = Split_Node()
        test_node.build_tree(countries, date)

        display_tree(test_node, date)  # this is to manually compare my output with the real output

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

