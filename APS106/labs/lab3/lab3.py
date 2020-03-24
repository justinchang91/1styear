###############################################
# APS106 Winter 2020 - Lab 3 - Grade Parser   #
###############################################


def score_average(scores):
    """
    (str) -> float
 
    Given s, a string representation of a sequence of four floating
    point numbers formatted as 'number1,number2,number3,number4',
    e.g., '1.0,12.0,13.0,2.0', calculate the average and return the average
    in s as a floating point number.
 
    >>> score_average('10.0,20.0,30.0,0.0')
    15.0
    """
    
    elements = scores.split(",")                                # Split the scores by comma into 4 individual elements
    f_elements = []                                             # Create a new empty list
    for item in elements:                                       # Use a for loop to fill new list with float scores
        f_elements.append(float(item))                          # .append() adds the floated item to the end of the list

    return sum(f_elements) / len(f_elements)                    # Calculate and return the average


def score_range(scores):
    """
    (str) -> float
 
    Given s, a string representation of a sequence of four floating
    point numbers formatted as 'number1,number2,number3,number4',
    e.g., '1.0,12.0,13.0,2.0', calculate, and return, the difference 
    between the maximum and minimum values
 
    >>> score_range('10.0,20.0,30.0,0.0')
    30.0
    """
    
    #TODO: YOUR CODE HERE
    elements = scores.split(",")
    elements = scores.split(",")  # Split the scores by comma into 4 individual elements
    f_elements = []  # Create a new empty list
    for item in elements:  # Use a for loop to fill new list with float scores
        f_elements.append(float(item))
    # Split the string into individual scores
    high = max(f_elements)                                 # Find the highest score, convert to float
    low = min(f_elements)                            # Find the lowest score, convert to float

    return high - low                                           # Return the range


def email_to_full_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@mail.utoronto.ca",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_full_name("anna.conda@mail.utoronto.ca")
    CONDA,ANNA
    """
    
    ## TODO: YOUR CODE HERE
    elements = email.split(".")                                 # Split the email by "." and put into list
    first = elements[0]                                         # Assign the first element to first name
    last = elements[1].split("@")[0]                            # Take second element, split by "@", take first element

    first = first.upper()                                       # Capitalize first name
    last = last.upper()                                         # Capitalize last name

    return last + "," + first                                   # Return formatted name


def student_quiz_results(email,marks):
    """
    (str,str) -> str
    
    Given a student's email with the format "first_name.last_name@mail.utoronto.ca"
    and marks from 4 quizzes formatted as "floating_point_number1,floating_point_number2", return
    a string "<LAST_NAME,FIRST_NAME,average_mark,range_of_marks>", where 
    FIRST_NAME and LAST_NAME are the first and last names of the student
    in all upper case characters, average_mark is the mean of the 4 quiz 
    scores and range_of_scores is the difference between the highest and 
    lowest score achieved.
 
    >>> student_quiz_results("anna.conda@mail.utoronto.ca","10.0,20.0,30.0,0.0")
    '<CONDA,ANNA,15.0,30.0>'
    """
    
    ## TODO: YOUR CODE HERE
    email_address = email_to_full_name(email)                   # Call the email to name function and assign to variable
    average = score_average(marks)                              # Call the average function and assign to variable
    mark_range = score_range(marks)                             # Call the mark range function and assign to variable

    return "<" + email_address + "," + str(average) + "," + str(mark_range) + ">"   # return formatted output


