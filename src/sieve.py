strike = []
def sieve(n):
    strike = list(range(2, n+1))
    for x in strike:
        for i in range(2, len(strike), 1):
            if x * i in strike:
                strike.remove((x*i))
    return strike