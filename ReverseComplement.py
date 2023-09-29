# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(pattern):
    complement = Complement(pattern)
    revcomplement = Reverse(complement)
    return revcomplement


# Reverse() function here.
def Reverse(pattern):
    # your code here
    reverse = ""
    n = len(pattern)
    for i in range(n):
        reverse += pattern[n - 1 - i]
    return reverse


# Complement() function here.
def Complement(pattern):
    # your code here
    complement = ""
    n = len(pattern)
    for i in range(n):
        if pattern[i] == "A":
            complement += "T"
        if pattern[i] == "T":
            complement += "A"
        if pattern[i] == "C":
            complement += "G"
        if pattern[i] == "G":
            complement += "C"
    return complement


string = str(input("Input DNA String"))
print(ReverseComplement(string))
