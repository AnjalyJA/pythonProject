firstno = int(input("First num"))
secondno = int(input("Second num"))
sum = 0
for i in range(firstno,secondno+1):
    flag = 0
    for j in range(2,i):
        if(i%j == 0):
            flag = 1
            break
    if flag == 0:
            sum = sum+i
print(sum)