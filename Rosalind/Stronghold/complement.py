def complement (text):
   return text.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]


text = "AATATTAGTCTTAACCAGTATTTCCGATATTACGTAGCAAGGATTGTCTGCTTAGAACGCCTAAATACGCGTTGGACGTTACAGGGCCTCCATATTAAGTTGCGATCCTCGTTTCATTCGTTCTTGTCGTTATACGACGTCCATTTCAGGCCTCTATTTAAGCTCACCTAATTCATATGATAGGAGGGGCCGGATGGACCCGAGGTATTGGAAATAAGTTATGGATGGAGCCATCTTTGGAAAAAGTCAGCACATATGCAATTTTAGCTTGGAAAGATTCAGCTCCAGTCAAGGCCTCCTAGAACCTGTCCCGTGATCCACATAGGAGACTGATGGGCCACTGTATTTCAACGCTGAGTCGCATCAAGCAGCGTTTTACCTATGGTTGAGGTGAACGGAATTATTGTTCGACCCGGCTCAACCAAAAACGGGCGTACCCCGTGGGCCTGCTCTCTGGTGGCAGGCTTTCCCGCCGTTAACTATATGGTGGTAACCATTCCTCTATGGAGAGCCTACGTATCTTCCCAACTTATCGGCGGAGTGTGGAAACCATTCCCATAGCAATATGGGAAAAATCCGAAGGGATCAACATATATGAGCGCGTGTGGGGGTTAGAGCCTCCATTGTTCCCTTACTCTTTGCCAGTTGTGAGGGAGCTGCCGTCAAGTTGAGGATGTCGTGCTGTCACTAGAATAAAGATGATGATCTCTGACTATCCAGAGACCCTCCGAAGCTGCATCGATGTGATTCCAGCCGTGGCAGGTTCACATATGTAGTAAAACTCTAATTGTGGCCGCAAGTACTTTAGCGTCAACCTGCTATGCT"
print (complement(text))