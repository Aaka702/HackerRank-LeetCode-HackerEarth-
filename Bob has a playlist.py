# Bob has a playlist of N songs, each song has a singer associated with it (denoted by an integer)
#
# Favourite singer of Bob is the one whose songs are the most on the playlist
#
# Count the number of Favourite Singers of Bob
#
# Input Format
#
# The first line contains an integer
# , denoting the number of songs in Bob's playlist.
#
# The following input contains
#  integers,
#  integer denoting the singer of the
#  song.
#
# Output Format
#
# Output a single integer, the number of favourite singers of Bob
#
# Note: Use 64 bit data type
N = int(input(""))
sequence = []
n = 1
for i in range(N//2):
    sequence.extend([n,n])
    n *= 2
    print(n)
count={}
for num in sequence:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
for num,count in count.items():
    print(f"{count}")

    


