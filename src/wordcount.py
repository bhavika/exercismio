__author__ = 'bhavika'


def count_words(phrase):
    results = {}
    phrase = ''.join(c for c in phrase if c not in ':!@#$%^&*()')
    words = phrase.lower().split()
    wordset = set(words)
    for word in wordset:
        ct = words.count(word)
        results.update({word: ct})
    return results




