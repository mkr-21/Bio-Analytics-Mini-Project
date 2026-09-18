def gc_content(sequence):
    sequence = sequence.upper()  

    count = 0
    gc_precentage = 0

    for nucleotide in sequence:
        if nucleotide == 'G' or nucleotide == 'C':
            count += 1

    
    gc_precentage = (count/ len(sequence)) *100
    return gc_precentage

seq = 'ATGCGC'
print(gc_content(seq))