"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If, for example, we change the first number to something else, comp is not returning true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.
"""

# First attempt 
def comp(array1, array2):
    multiplicity_dict = {num: num*num for num in array1}
    
    print(array1, array2, sep="\n")
    
    if type(array1) != type(array2): 
        return False
    
    for num in array2: 
        if num not in multiplicity_dict.values():
            return False
    
    return True

# Second attempt 
from collections import Counter

def comp(array1: list, array2: list) -> bool:
    # Return False if either array is None or empty
    if array1 is None or array2 is None:
        return False
    # Return False if one array is empty and the other is not
    elif not array1 and array2 or array1 and not array2:
        return False
    # Return True if both arrays are empty
    elif not array1 and not array2:
        return True
    
    # Create frequency dict for both arrays
    freq1 = Counter(array1)
    freq2 = Counter(array2)

    # Check if all elements in array1 are present in array2
    for key, value in freq1.items():
        if key**2 not in freq2 or freq2[key**2] != value:
            return False
    
    return True
