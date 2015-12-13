from functools import reduce


def slices(series, length):
    numbers = [int(digit) for digit in series]
    if not 1 <= length <= len(numbers):
        raise ValueError("Invalid slice length for this series: "+ str(length))
    return [numbers[i:i + length]
            for i in range(len(numbers) - length + 1)]
            
            
def get_product(series, n):
    large = slices(series,n)
    p = []
    for z in large:
        p.append(reduce(lambda x, y: x*y, z))
    return max(p)