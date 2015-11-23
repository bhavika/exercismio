
def to_rna(dna):
    complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = []
    for nuc in dna:
        if nuc in complements.keys():
            rna.append(complements[nuc])
        else:
            for k, v in complements.items():
                if v == nuc:
                    rna.append(k)
    return ''.join(rna)
    
    
    



