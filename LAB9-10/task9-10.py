dna_sequence = "ATGCTACGATCGTACGGCGCAAATAGCTAGCTAGCTAGC"

gc_count = dna_sequence.count('G') + dna_sequence.count('C')
sequence_length = len(dna_sequence)

gc_percentage = (gc_count / sequence_length) * 100

print("GC percentage:", gc_percentage)
