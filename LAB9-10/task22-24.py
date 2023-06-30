from Bio.Seq import Seq

# Create a DNA sequence
dna_sequence = Seq("AATGCGCTTGCGTATTACGAT")

# Transcribe DNA to RNA
rna_sequence = dna_sequence.transcribe()

# Translate RNA to protein
protein_sequence = rna_sequence.translate()

# Print the sequences
print("DNA sequence:", dna_sequence)
print("RNA sequence:", rna_sequence)
print("Protein sequence:", protein_sequence)

# o/p --> DNA sequence: AATGCGCTTGCGTATTACGAT
# RNA sequence: AAUGCGCUUGCGUAUUACGAU
# Protein sequence: NALAYYD

