import  os
def compareTriplets(a, b):
    # Initialize points for Alice and Bob
    alice_points = 0
    bob_points = 0

    # Compare each element of the triplets
    for i in range(3):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
        # If a[i] == b[i], no points are awarded to either

    # Return the comparison points as a list
    return [alice_points, bob_points]
if __name__ == '__main__':
    a = list(map(int, input("enter a").rstrip().split()))
    b = list(map(int, input("Enter b").rstrip().split()))
    result = compareTriplets(a, b)