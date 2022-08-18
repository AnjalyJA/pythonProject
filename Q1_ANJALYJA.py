
n = 10
m = 10
for i in range(1,20):
    for j in range(1,20):

        if(j>m & j<n):
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
    n=n+1
    m=m-1

for i in range(1,20):
    for j in range(1,20):
        if(j>m & j<n):
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
    n=n-1
    m=m+1