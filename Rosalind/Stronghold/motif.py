def longest_common_substring(dna_strings):
    if not dna_strings:
        return ""

    # Function to find the longest common prefix of two strings
    def common_prefix(s1, s2):
        common_len = min(len(s1), len(s2))
        for i in range(common_len):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:common_len]

    # Find the common prefix of all strings
    common_prefix_str = dna_strings[0]
    for i in range(1, len(dna_strings)):
        common_prefix_str = common_prefix(common_prefix_str, dna_strings[i])

    return common_prefix_str

# Example usage:
dna_strings = [
    "ACCTAGC",
    "TAGCTAC",
    "TCAGAGT",
    "GAGTAGC"
]

result = longest_common_substring(dna_strings)
print("Longest Common Substring:", result)
