##########################################################################
# APS106 Winter 2020 - Lab 2 - Cartesian to Polar Conversion Functions   #
##########################################################################

import math


def magnitude(x, y):
    """
    (float,float) -> float
    
    Function calculate the magnitude of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the magnitude of the vector as a float.
    
    The magnitude of a 2D vector can be calculated using the following
    equation:
                      ____________ 
                     /
        magnitude = v  x^2 + y^2
        
        where x and y are the x and y components of the vector
    
    
    >>> magnitude(10.0,25.5)
    27.390691849604675
    """
    
    ## TODO: YOUR CODE HERE
    r = math.sqrt(x ** 2 + y ** 2)
    return r


def phase(x, y):
    """
    (float,float) -> float
    
    Function calculates the phase angle of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the phase angle in radians as a float.
    
    The phase angle of a 2D vector can be calcuated using the following 
    equation:
        
        phase = atan( y / x )
        
        where atan represents the inverse tangent function and x and y are 
        the x and y components of the vector
    
    
    Hint: In Python's math module, there are two functions that can be used to
          calculate the inverse tangent. Find the two options in the
          documentation here: https://docs.python.org/3/library/math.html#trigonometric-functions
          
          OR

          use the help function to get information for both inverse tangent functions
          >>> import math
          >>> help(math.atan)          
          >>> help(math.atan2)
              
          During your lab session, discuss with your TA which function you
          believe should be used.
          
          Can you think of a test case where the two options would return
          different values?
        
        
    >>> phase(10.0,25.5)
    1.197069506829343
    """
    
    ## TODO: YOUR CODE HERE
    s = math.atan2(y, x)
    return s


