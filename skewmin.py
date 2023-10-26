# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = []  # output variable
    skew = SkewArray(Genome)
    for i in range(len(Genome)):
        if (skew[i] == min(skew)):
            positions.append(i)
    return positions


# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    # your code here
    n = 0
    Skew = [0]
    for i in range(len(Genome)):
        if (Genome[i] == "C"):
            n -= 1
        if (Genome[i] == "G"):
            n += 1
        Skew.append(n)
    return Skew


genome = str(input("Input Genome"))
print(MinimumSkew(genome))
