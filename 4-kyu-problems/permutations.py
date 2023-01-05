"""In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

The order of the permutations doesn't matter."""

def permutations(string: str) -> set:
    # Base case: if the input string is of length 1, return the string as a single-item list
    if len(string) == 1:
        return [string]

    # Initialize an empty list to store the permutations
    perms = []

    # Iterate through each character in the string
    for i, char in enumerate(string):
        # Generate the permutations for the string without the current character
        sub_perms = permutations(string[:i] + string[i+1:])
        
        # Add the current character to the beginning of each permutation and append to the list
        for perm in sub_perms:
            perms.append(char + perm)
    
    # Return the list of permutations as a set to remove duplicates
    return set(perms)

# Best practice from discussion
import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

# Clever from discussion
from itertools import permutations as pm
permutations=lambda s: map(''.join, set(pm(s)))