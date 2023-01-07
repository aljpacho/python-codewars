""""one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them"""

# Attempt 1: passes 486, fails 204
NUMBER_DICT = {'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'eleven': 11,
            'twelve': 12,
            'thirteen': 13,
            'fourteen': 14,
            'fifteen': 15,
            'sixteen': 16,
            'seventeen': 17,
            'eighteen': 18,
            'nineteen': 19,
            'twenty': 20,
            'thirty': 30,
            'forty': 40,
            'fifty': 50,
            'sixty': 60,
            'seventy': 70,
            'eighty': 80,
            'ninety': 90,
              }

def parse_int(string: str, number_dict=NUMBER_DICT) -> int:

    numbers = []
    
    print(string)
    
    tokens = string.split(' ')
    
    for token in tokens:
        if token in number_dict:
            numbers.append(number_dict[token])
        elif token == "hundred":
            numbers[-1] *= 100
        elif token == "thousand":
            numbers[-1] *= 1000
        elif token == "million":
            numbers[-1] *= 10000000
        elif "-" in token:
            token_1 = token.split("-")[0]
            token_2 = token.split("-")[1]
            numbers.append(parse_int(token_1) + parse_int(token_2))
    
    print(numbers, sum(numbers), sep="\n")
    
    return sum(numbers)