from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction




def gc_content(sequence):
    sequence = sequence.upper()  
    gc_precentage = gc_fraction(Seq(sequence)) * 100
    return gc_precentage






def validate_sequence(sequence):
    sequence = sequence.upper()   
    if sequence == '':
        raise ValueError("Invalid sequence. Please enter a valid DNA sequence.")
    for nucleotide in sequence:
        if nucleotide not in {'A', 'T', 'C', 'G'}:
            raise ValueError("Invalid sequence. Please enter a valid DNA sequence.")
    return True





def quality_verdict(gc_percent):
    if gc_percent >= 50:
        return "Stable"
    else:
        return "Unstable"




def main():
    sequence = "ATCGATCGATCG"
    validate_sequence(sequence)
    gc = gc_content(sequence)
    verdict = quality_verdict(gc)
    
    print(f"Sequence: {sequence}")
    print(f"GC Content: {gc:.2f}%")
    print(f"Verdict: {verdict}")


main()