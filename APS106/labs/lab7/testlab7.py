# Test the reader out
import csv

csvfile = open("samplecsvdata.csv", "r")

colour_reader = csv.reader(csvfile)

dict1 = {}

for row in colour_reader:
    if row[0] in dict1:
        dict1[row[0]] += int(row[1])
    else:
        dict1[row[0]] = int(row[1])

print(dict1)


# Part 2
bom = {'CF14JT10K0CT-ND': 21, '469-1004-ND': 300, '1568-1123-ND': 12}
csvfile2 = open("parts_db1.csv")

table_of_costs = list(csv.reader(csvfile2))


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
    print("The price index for " + part + " is: " + str(price_index))
    cost_of_part = float(price_for_part) * bom[part]

    next_price_index = price_index + 1
    print("The next price index for " + part + " is: " + str(next_price_index))
    valid = False
    while not valid:
        if next_price_index < len(first_row):  # If price_index is not in the last column  THE PROBLEM IS WITH THE + 1
            print("TEST")
            price_for_next_part = table_of_costs[int(part_row_index)][next_price_index] # potential fix to error no.

            if price_for_next_part == "-":
                print("The next index would be " + str(next_price_index + 1))

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
            price_for_next_part = table_of_costs[int(part_row_index)][price_index]  # Just default back to the price index
            next_price_break = first_row[price_index]
            next_price_index = price_index

    print("The price for " + part + " at price break " + str(price_break) + " is: " + str(price_for_part))
    print("The next price for " + part + " at price break " + str(next_price_break) + " is: " + str(price_for_next_part))

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

    # Test the outputs

print(round(total_cost, 2))
print(bom)