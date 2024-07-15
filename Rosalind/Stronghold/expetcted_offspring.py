'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Calculating Expected Offspring
Rosalind ID: IEV
Rosalind #: 013
URL: http://rosalind.info/problems/iev/
'''
def calculate_expected_offspring(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa):
    # Calculate the expected number of dominant offspring for each genotype
    expected_AA_AA = AA_AA * 2 * 1  # 2 offspring, both dominant
    expected_AA_Aa = AA_Aa * 2 * 1  # 2 offspring, both dominant
    expected_AA_aa = AA_aa * 2 * 1  # 2 offspring, both dominant
    expected_Aa_Aa = Aa_Aa * 2 * 0.75  # 2 offspring, 75% dominant
    expected_Aa_aa = Aa_aa * 2 * 0.5  # 2 offspring, 50% dominant
    expected_aa_aa = aa_aa * 2 * 0  # 2 offspring, 0% dominant

    # Sum up the expected number of dominant offspring for all genotypes
    total_expected_offspring = (
        expected_AA_AA + expected_AA_Aa + expected_AA_aa +
        expected_Aa_Aa + expected_Aa_aa + expected_aa_aa
    )

    return total_expected_offspring

# Example usage with given numbers
result = calculate_expected_offspring(19710,16445,17978,18181,16326,17644)
print(result)
