def polygonal_number(n, i):
    if n < 3:
        raise ValueError("n must be greater than or equal to 3")
    elif i < 1:
        raise ValueError("i must be greater than or equal to 1")
    else:
        return int((i * ((n - 2) * i - (n - 4))) / 2)

try:
    n = int(input("Enter the number of sides of the polygon (n): "))
    if n < 3:
        raise ValueError("n must be greater than or equal to 3")
    i = int(input("Enter the index of the polygonal number (i): "))
    if i < 1:
        raise ValueError("i must be greater than or equal to 1")
    polygonal_num = polygonal_number(n, i)
    print(f"The {i}th {n}-gonal number is: {polygonal_num}")
except ValueError as error:
    print(error)

