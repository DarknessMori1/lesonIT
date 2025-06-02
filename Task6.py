def get_sq_rect(length, width):
    return length * width

def get_sq_square(a):
    return a * a

tp = input().strip()

if tp == "RECT":
    get_sq = get_sq_rect
    # пример вызова:
    print(get_sq(3, 4))
else:
    get_sq = get_sq_square
    # пример вызова:
    print(get_sq(5))