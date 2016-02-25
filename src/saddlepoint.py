def saddle_points(matrix):
    if any(len(r) != len(matrix[0]) for r in matrix):
        raise ValueError('Irregular matrix')
    if not matrix:
        return set()
    g = [max(r) for r in matrix]
    s = [min(c) for c in zip(*matrix)]
    positions = [(i, j) for i in range(len(matrix))
                 for j in range(len(matrix[0])) if g[i] == s[j]]
    return set(positions)
