"""Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ')."""

def to_weird_case(words):
    weird_words = []
    words_list = words.split(' ')
    
    for word in words_list:
        weird_word = []
        for index, char in enumerate(word):
            if index % 2 == 0:
                weird_word.append(char.upper())
            else:
                weird_word.append(char.lower())
        weird_words.append(''.join(weird_word))
    
    weird_string = ' '.join(weird_words)
    return weird_string