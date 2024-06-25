'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb/
'''
def dominant_probability(k, m, n):
    total_population = k + m + n
    next_population = total_population - 1

    # Probability of producing an individual with a dominant allele in each case
    prob_aa_from_AaAa = 0.25
    prob_aa_from_Aaaa = 0.5
    prob_aa_from_aaaa = 1

    # Calculate the overall probability using the law of total probability
    overall_probability = (
        (m / total_population * (n / next_population) * prob_aa_from_Aaaa) +
        (m / total_population * ((m - 1) / next_population ) * prob_aa_from_AaAa) +
        (n / total_population * (m / next_population) * prob_aa_from_Aaaa) +
        (n  / total_population * ((n - 1) / next_population) * prob_aa_from_aaaa)
    )

    return 1 - overall_probability  # Probability of having a dominant allele

k_value = 25
m_value = 16
n_value = 26

result = dominant_probability(k_value, m_value, n_value)
print(result)
