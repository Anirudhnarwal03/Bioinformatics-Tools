# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = []  # initializing list of positions
    for i in range(len(Text) - len(Pattern) + 1):  # corrected the range
        if HammingDistance(Pattern, Text[i:i + len(Pattern)]) <= d:
            positions.append(i)
    return positions


def HammingDistance(p, q):
    if len(p) != len(q):
        return -1  # Return -1 or some error value if lengths are not equal

    hamming = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hamming += 1
    return hamming


genome = str(input("Input Genome"))
pattern = str(input("Input DNA Pattern"))
d = int(input("Input Margin of Error"))
print(ApproximatePatternMatching(genome, pattern, d))
