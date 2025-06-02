def is_even(n: int) -> bool:
    return n % 2 == 0

def process_numbers():
    while True:
        x = int(input())
        if x == 1:
            break
        if is_even(x):
            print(x)
