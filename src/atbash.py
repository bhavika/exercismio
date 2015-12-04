from string import ascii_lowercase, punctuation

translation = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])

# print translation

BLOCK = 5


def preprocess_string(plain):
    plain = plain.replace(" ", "")
    plain = plain.lower()
    for c in plain:
        if c in punctuation:
            plain = plain.replace(c, "")
    return plain


def encode(plain):
    plain = preprocess_string(plain)
    e = str.translate(plain, translation)
    return ' '.join(e[i: i+BLOCK] for i in range(0, len(e), BLOCK))
    
  
def decode(encoded):
    d = str.translate(encoded, translation)
    d = d.replace(" ", "")
    return d
    
    
# print encode('Truth is fiction.')    
