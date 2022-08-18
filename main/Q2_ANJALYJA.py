limit = int(input("Enter limit"))
i = 1
j = 1
while (i <= limit):
    n = i
    m = limit-1
    j = 1
    while (j <= i):
        print(n, end=" ")
        n = n + m
        m = m - 1
        j = j + 1

    print("\n")

    i = i + 1

