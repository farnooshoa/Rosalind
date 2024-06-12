def motif(fasta_data):
    sequences = []
    current_sequence = ""

    for line in fasta_data.splitlines():
        if line.startswith(">"):
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = ""
        else:
            current_sequence += line

    if current_sequence:
        sequences.append(current_sequence)

    return sequences

def Count(string):
    count = {}
    k = len(string[0])
    for symbol in "ACGT":
        count[symbol] = [0] * k

    t = len(string)
    for i in range(t):
        for j in range(k):
            symbol = string[i][j]
            count[symbol][j] += 1

    return count

def Consensus(string):
    k = len(string[0])
    count = Count(string)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

t = """
"""
strings = motif(t)
print(Consensus(strings))
count = Count(strings)

for symbol in "ACGT":
    print(f"{symbol}: {' '.join(map(str, count[symbol]))}")
