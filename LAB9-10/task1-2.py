dna_sequence = "ATGCTACGATCGTAGCTAGCTAGCTAGCTAGC"

# Initialize nucleotide counters
adenine_count = 0
cytosine_count = 0
guanine_count = 0
thymine_count = 0

# Going through every nucleotide in the DNA sequence
for nucleotide in dna_sequence:
    if nucleotide == "A":
        adenine_count += 1
    elif nucleotide == "C":
        cytosine_count += 1
    elif nucleotide == "G":
        guanine_count += 1
    elif nucleotide == "T":
        thymine_count += 1

# Print the counts of each nucleotide
print("Adenine count:", adenine_count)
print("Cytosine count:", cytosine_count)
print("Guanine count:", guanine_count)
print("Thymine count:", thymine_count)
