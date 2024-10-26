
N = int(input("Enter a positive integer N: "))

numbers = []

print("Enter the numbers:")
for i in range(N):
    num = int(input())
    numbers.append(num)

X = int(input("Enter an integer X to search for: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)
