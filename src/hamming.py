__author__ = 'bhavika'


def distance(dna1, dna2):
    dist = 0
    if len(dna1) == len(dna2):
        l1 = list(dna1)
        l2 = list(dna2)
        for x, val in enumerate(l1):
            if l1[x] != l2[x]:
                dist += 1
    return dist


