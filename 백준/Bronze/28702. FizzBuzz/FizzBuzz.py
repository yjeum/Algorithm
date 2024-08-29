import sys

input = sys.stdin.readline

for i in range(3):
    temp = input()
    try:
        num = int(temp) + (3 - i)
        break
    except:
        continue

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)