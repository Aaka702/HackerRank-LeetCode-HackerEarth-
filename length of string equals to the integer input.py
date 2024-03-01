# Read different types of data from standard input, process them as shown in output format and print the answer to standard output.
#
# Input format:
# First line contains integer N.
# Second line contains string S.
#
# Output format:
# First line should contain N x 2.
# Second line should contain the same string S.
N=int(input(""))
if N>=10:
    print("Invalid")
S=input("")
d=len(S)
if d>=15:
    print("Invalid")
print(N*2)
print(S)
