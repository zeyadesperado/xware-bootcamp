n = int(input())

for num in range(2, n+1):

    isPrime = True

    for i in range (2,int(num**0.5) + 1) :
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print( num,end=" ")