decimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
hexx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
conv = list(zip(decimal, hexx))

def int_hex(int_color):
    res1 = int_color // 16
    res2 = int_color % 16
    hexnum = ""
    for i in conv:
        if res1 == i[0]:
            hexnum += str(i[1])
        if res2 == i[0]:
            hexnum += str(i[1])
    return hexnum

def create_hex(r, g, b):
    return int_hex(r) + int_hex(g) + int_hex(b)

if __name__ == '__main__':
    red = int(input("Enter the red value: "))
    green = int(input("Enter the green value: "))
    blue = int(input("Enter the blue value: "))
    print("#" + create_hex(red, green, blue))
