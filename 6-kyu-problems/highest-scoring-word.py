"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    letter_scores = {chr(i+96):i for i in range(1,27)}
    
    words = x.split(' ')

    scores = []
    
    for word in words:
        score = 0
        for char in word:
            score += letter_scores[char]
        scores.append(score)
    
    word_scores = list(zip(words, scores))
    
    max_word_score = max(word_scores, key=lambda x: x[1])
    
    return max_word_score[0]
    
    