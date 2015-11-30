
def square_of_sum(n):
    p = n * (n+1) / 2
    p = pow (p,2)
    return p
    

def sum_of_squares(n):
    q = n * (2 * n + 1) * (n + 1) / 6
    return q
    


def difference(n):
    return square_of_sum(n) - sum_of_squares(n)