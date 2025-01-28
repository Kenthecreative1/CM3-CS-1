while True:
    h = int(input("Pyramid height? "))
    if 1<= h <= 8:
        break 
for i in range (1, h+1):
    print(" " * (h - i) + "#" * i + "  " + "#" * i)
while True: 
    h = int(input)