def is_triangle(a,b,c):
    if((a+b>c) and (a+c>b) and (b+c>a)):
        return("TRUE")
    
    else:
        return("FALSE")

a=int(input("Сторона 1 = "))
b=int(input("Сторона 2 = "))
c=int(input("Сторона 3 = "))
print(is_triangle(a,b,c))