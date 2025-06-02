tp = input().strip()

if tp == "RECT":
    def get_sq(length, width):
        return length * width
else:
    def get_sq(a):
        return a * a