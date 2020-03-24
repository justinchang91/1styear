#########################################################
# APS106 Winter 2020 - Lab 7 - Bill of Materials Reader #
#########################################################

#########################################################
# PART 1 - Complete the function below to read in a file
#          containing part numbers and the amount to 
#          order
#########################################################

import csv

def parse_bom(filename):
    """
    (str) -> dict
    
    Open and read a csv file named 'filename' that contains part numbers in the
    first column and the minimum number required to order in the second column.
    
    Return a dictionary with the part numbers as keys and the minimum number
    to order as values. 
    
    >>> parse_bom("bom1.csv")
    {'MC14572UBDG-ND': 85,
     '469-1004-ND': 400,
     '480-2015-ND': 25,
     '917-1130-ND': 2,
     '1-487526-5-ND': 42}
    
    """
    
    ## TODO: YOUR CODE HERE
    csvfile = open(filename, "r")

    colour_reader = csv.reader(csvfile)

    dict1 = {}

    for row in colour_reader:
        if row[0] in dict1:
            dict1[row[0]] += int(row[1])
        else:
            dict1[row[0]] = int(row[1])

    return dict1
#########################################################
# PART 2 - Read the supplier database file and determine 
#          the correct amount of each part to order as
#          well as the total price of the order
#########################################################

def generate_order(bom, parts_cost_filename):
    """
    (dict, str) -> float, dict
    
    Open and read a csv file containing part numbers and the cost of the parts
    when ordering different quantities.
    
    For each part in the dictionary 'bom' determine the correct number of 
    units to order that minimizes the price of the order.
    
    Return the total price of the order and a dictionary with part numbers
    as keys and the total number of units to order as values
    
    >>> generate_order({'MC14572UBDG-ND': 85,'1-487526-5-ND': 42},"parts_db1.csv")
    (105.5404, {'MC14572UBDG-ND': 100, '1-487526-5-ND': 42})
    """
    
    ## TODO: YOUR CODE HERE
    csvfile2 = open(parts_cost_filename)

    table_of_costs = list(csv.reader(csvfile2))
    # print(type(table_of_costs))

    total_cost = 0
    for part in bom:  # loop through the parts

        for j in range(1, len(table_of_costs), 1):
            if table_of_costs[j][0] == part:
                part_row_index = j

        # Find the price break of the part (desired col)
        first_row = table_of_costs[0]
        for i in range(1, len(first_row), 1):
            if bom[part] >= int(first_row[i]):
                price_break = first_row[i]
                price_index = i

                # Check to see if there's a price value at that price break
                valid = False
                while not valid:
                    price_for_part = table_of_costs[int(part_row_index)][int(price_index)]
                    if price_for_part == "-":
                        price_break = first_row[price_index - 1]
                        price_index -= 1
                    else:
                        valid = True
        # print("The price index for " + part + " is: " + str(price_index))
        cost_of_part = float(price_for_part) * bom[part]

        next_price_index = price_index + 1
        # print("The next price index for " + part + " is: " + str(next_price_index))
        valid = False
        while not valid:
            if next_price_index < len(
                    first_row):  # If price_index is not in the last column  THE PROBLEM IS WITH THE + 1
                # print("TEST")
                price_for_next_part = table_of_costs[int(part_row_index)][
                    next_price_index]  # potential fix to error no.

                if price_for_next_part == "-":
                    # print("The next index would be " + str(next_price_index + 1))

                    if next_price_index + 1 == len(first_row):
                        valid = True
                        next_price_index = price_index
                        next_price_break = first_row[price_index]
                        price_for_next_part = table_of_costs[int(part_row_index)][price_index]
                    else:
                        next_price_index += 1
                        next_price_break = first_row[next_price_index]
                else:
                    valid = True
                    next_price_break = first_row[next_price_index]
            else:  # If next_price_index is outside the list that means that it was "-" for all the next price breaks
                valid = True
                price_for_next_part = table_of_costs[int(part_row_index)][
                    price_index]  # Just default back to the price index
                next_price_break = first_row[price_index]
                next_price_index = price_index

        # print("The price for " + part + " at price break " + str(price_break) + " is: " + str(price_for_part))
        # print("The next price for " + part + " at price break " + str(next_price_break) + " is: " + str(price_for_next_part))

        if bom[part] < int(next_price_break):  # checks what the quantity should be
            cost_of_next_part = float(price_for_next_part) * int(next_price_break)

        else:
            cost_of_next_part = float(price_for_next_part) * bom[part]

        # Compare the costs and add to total
        if cost_of_part < cost_of_next_part:
            total_cost += cost_of_part
        else:
            total_cost += cost_of_next_part
            if bom[part] < int(next_price_break):  # checks what the quantity should be
                bom[part] = int(next_price_break)

    return round(total_cost, 2), bom

