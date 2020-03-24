scores = "40.3,5.4,-9.8,110.4"
email = "anna.conda@mail.utoronto.ca"

scores.split(",")[0]
scores.split(",")[1]

# Calculate average
elements = scores.split(",")                                # Split the scores by comma into 4 individual elements
f_elements = []                                             # Create a new empty list
for x in elements:                                          # Use a for loop to fill new list with float scores
    f_elements.append(float(x))                             # for loop loops through the actual elements, in elements

print("Elements: " + str(elements))
average = sum(f_elements) / len(f_elements)                 # Calculate the average
print("Average: " + str(average))

# Calculate range
low = min(f_elements)
high = max(f_elements)

print("Low: " + str(low))
print("High: " + str(high))

mark_range = high - low
print("Range of marks: " + str(mark_range))

# Email address
items = email.split(".")
first = items[0]
last = items[1].split("@")[0]

first = first.upper()
last = last.upper()

email_address = last + "," + first
print("Name: " + email_address)

print("<" + str(email_address) + "," + str(average) + "," + str(mark_range) + ">")
