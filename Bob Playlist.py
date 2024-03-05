# Bob has a playlist of songs, each song has a singer associated with it (denoted by an integer)
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
#
# Constraints





def count_favourite_singers(num_songs, playlist):
    singer_counts = {}
    max_count = 0

    # Count the occurrences of each singer
    for singer in playlist:
        singer_counts[singer] = singer_counts.get(singer, 0) + 1
        max_count = max(max_count, singer_counts[singer])

    # Count the number of favourite singers
    favourite_singers_count = sum(1 for count in singer_counts.values() if count == max_count)

    return favourite_singers_count

# Read input
num_songs = int(input())
playlist = list(map(int, input().split()))

# Call the function and print the result
print(count_favourite_singers(num_songs, playlist))
