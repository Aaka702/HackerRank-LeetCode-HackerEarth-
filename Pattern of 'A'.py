#n=int(input("Enter the number"))
n=8
for i in range(n):
    for j in range(n):
        if((i+j)/2 <=n ):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
