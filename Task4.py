def is_even(n):
    return n % 2 == 0

while True:
    x = int(input())
    if x == 1:
        break
    if is_even(x):
        print(x)
