# Python Exercises


> User guessing random number game 

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

> <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/C">Simple Calculator</a>
```python
x,y = input().split()
x = int(x)
y = int (y)
print(f"{x} + {y} = {x+y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} - {y} = {x-y}")
```
> <a href="https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/K">K. Max and Min </a>

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