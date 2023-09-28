# Objective - Find the most frequent nucleotide segments of a given length in the genomic data inputted
def FrequentWords(text, k):
    # your code here
    words = []
    freq = FrequencyMap(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)

    return words


def FrequencyMap(text, k):
    freq = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        freq[pattern] = 0
        # Another for loop here to range over each k-mer Pattern of text and increase freq[Pattern] by 1 each time
        for x in range(n - k + 1):
            check = text[x:x + k]
            if check == pattern:
                freq[pattern] += 1
    return freq


Text = str(input("Input Genomic Data"))
K = int(input("Length of Nucleotide Pattern to be found"))
print(FrequentWords(Text, K))
