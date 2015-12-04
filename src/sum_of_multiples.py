
def sum_of_multiples(n, m=None):
    if m == None:
        m = [3, 5]
    elif m[0] == 0:
        m = m[1:]
    return sum(value for value in range(n)
               if any(value % multiple == 0 for multiple in m))

