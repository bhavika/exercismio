


def detect_anagrams(word, sentence):
    is_anagram = []
    for w in sentence:
        word = word.lower()
        x = w.lower()
        if sorted(str(word)) == sorted(str(x)) and word != x:
            is_anagram.append(w)
    return is_anagram
    
