homozygotes_dominant = 100
heterozygotes = 200
homozygotes_recessive = 100

total_individuals = homozygotes_dominant + heterozygotes + homozygotes_recessive

# frequency of the dominant allele (A)
frequency_dominant_allele = (homozygotes_dominant + (0.5 * heterozygotes)) / total_individuals

#  frequency of the recessive allele (a)
frequency_recessive_allele = (homozygotes_recessive + (0.5 * heterozygotes)) / total_individuals

print("Frequency of the dominant allele (A):", frequency_dominant_allele)
print("Frequency of the recessive allele (a):", frequency_recessive_allele)
