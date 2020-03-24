#####################################################
# APS106 Winter 2020 - Lab 6 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>>mol_form("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}

    >>>mol_form("C1H4")
    {'C': 1, 'H': 4}

    >>>mol_form("Al2O3")
    {'Al': 2, 'O': 3}
    """
     
    ## TODO: YOUR CODE HERE
    stepper = 0
    list1 = []

    while stepper < len(compound_formula):
        word = ""  # Erases word's value

        if 65 <= ord(compound_formula[stepper]) <= 90 and 97 <= ord(compound_formula[stepper + 1]) <= 122:  # if it's a letter
            word += compound_formula[stepper]  # Add the first letter to the word because you know it's a capital
            word += compound_formula[stepper + 1]

            list1.append(word)
            stepper += 2

        elif 65 <= ord(compound_formula[stepper]) <= 90:
            word += compound_formula[stepper]
            list1.append(word)
            stepper += 1

        else:  # if it's a number ONLY WORKS FOR SINGLE DIGITS
            if stepper + 1 < len(compound_formula) and 48 <= ord(compound_formula[stepper + 1]) <= 57:  # if the number is within
                word += compound_formula[stepper]
                word += compound_formula[stepper + 1]
                list1.append(int(word))
                stepper += 2
            else:
                word += compound_formula[stepper]
                list1.append(int(word))
                stepper += 1

    # convert the list to a dictionary

    dict1 = {}
    for i in range(0, len(list1), 2):
        dict1[list1[i]] = list1[i + 1]

    return dict1
######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {"Na" : 7, "Cl" : 2, "H" : 2, "F" : 5}
    
    """
    ## TODO: YOUR CODE HERE
    dict2 = {}
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

    return dict2

########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>>  >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    
    ## TODO: YOUR CODE HERE
    list1 = []
    for atom in reactant_atoms:
        if reactant_atoms[atom] != product_atoms[atom]:
            list1.append(atom)

    return set(list1)

########################################################
# PART 4 - Test your code! You should write test cases
#          for each individual function above. You may
#          also use the function below to test all three
#          functions when you are finished.
########################################################

def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    
        C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
        reactants: ((1,5), ("C3H8","O2"))
        products: ((4,3), ("H2O1","C1O2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()
    
    Similarly for the unbalanced equation
    
            C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
        reactants: ((1,2), ("C3H8","O2"))
        products: ((4,3), ("H2O1","C1O2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    
    NOTE - YOU DO NOT NEED TO CHANGE THIS FUNCTION, IT IS ONLY FOR YOUR TESTING
    PURPOSES!
    """
    
    reactant_molecs = ()
    product_molecs = ()
    
    for molec in reactants[1]:
        reactant_molecs += (mol_form(molec),)
        
    
    for molec in products[1]:
        product_molecs += (mol_form(molec),)
    
    reactant_atoms = expr_form(reactants[0], reactant_molecs)
    product_atoms = expr_form(products[0], product_molecs)
    
    # check if the two sides contain different elements
    unbalanced_elems = find_unbalanced_atoms(reactant_atoms,product_atoms)
    
    return unbalanced_elems
    

