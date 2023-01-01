"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

def find_it(seq):

    if len(seq) == 1:
        return seq[0]
    else:
        sequence_dict = {}
        
        for num in seq:
            if num not in sequence_dict:
                sequence_dict[num] = 1
            else:
                sequence_dict[num] += 1
        
        for num, count in sequence_dict.items():
            if count % 2 != 0:
                return num

# Second iteration
def find_it(seq):
    # Create a dictionary to store the frequency of each element in the sequence
    frequency = {}
    
    # Iterate through the sequence and count the frequency of each element
    for num in seq:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1
    
    # Iterate through the dictionary and return the first element with odd frequency
    for num, count in frequency.items():
        if count % 2 != 0:
            return num

