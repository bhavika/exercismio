def sieve(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False

    for i in range(2, int (n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n+1, i):
                p[j] = False
    
    return [i for i, x in enumerate(p) if x]

    