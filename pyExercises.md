# Python Exercises


> #### User guessing random number game 

```python
import random
num_guessed = random.randint(1,10)
x = -1
while(x != num_guessed):
    x = int(input("\n try to guess the number ! : "))
    if(x > num_guessed):
        print("\n You entered a larger number, try again please")
    elif(x < num_guessed):
        print("\n you entered a smaller number, try again please ")
else:
    print("\n Nice! You got it right the right number is " + str(num_guessed) + " !")
```

- #### <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/C">C. Simple Calculator</a>
```python
x,y = input().split()
x = int(x)
y = int (y)
print(f"{x} + {y} = {x+y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} - {y} = {x-y}")
```
- #### <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K">K. Max and Min </a>

```python
x, y, z = map(int,input().split())
if x >= y and x >= z:
    if y <= z:
        print(f"{y} {x}")
    else:
        print(f"{z} {x}")
elif y >= z and y >= x:
    if z <= x:
        print(f"{z} {y}")
    else:
        print(f"{x} {y}")
else:
    if x <= y:
        print(f"{x} {z}")
    else:
        print(f"{y} {z}")

```

- #### <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/F">F. Digits Summation</a>

```python
x,y = input().split()
print(f"{int(x[-1])+int(y[-1])}")
```
- #### <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q">Q. Digits </a>

```python
n = int(input())
for _ in range (n):
    num = int(input())
    num_str = str(num)
    num_array = [int(num_array) for num_array in num_str]
    reverse = reversed(num_array)
    print(*reverse)
```

- #### <a href = "https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S">S. Sum of Consecutive Odd Numbers</a>
```python 
n = int(input())

for _ in range (n):
    num1, num2 = map(int,input().split())
    if num1 > num2:
        num1, num2 = num2, num1
    sum = 0
    for i in range(num1+1,num2):
        if i % 2 != 0 :
            sum += i
    print(sum)     
```

- #### <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/K">K. Divisors</a>

```python
n = int(input())
for i in range(1,n+1):
    if n % i == 0:
        print(i)
```
- #### <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/J">J. Primes from 1 to n</a>

```python
n = int(input())

for num in range(2, n+1):

    isPrime = True

    for i in range (2,int(num**0.5) + 1) :
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print( num,end=" ")
```