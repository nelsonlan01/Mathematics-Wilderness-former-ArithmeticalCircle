def tetrahedral_number(n):
    return int((n * (n + 1) * (n + 2)) / 6)

def square_pyramidal_number(n):
    return int((n * (n + 1) * (2 * n + 1)) / 6)

function_name = input("Enter the name of the function to use (t for tetrahedral_number, s for square_pyramidal_number): ")

if function_name not in ['t', 's']:
    print("Invalid function name.")
else:
    try:
        n = int(input("Enter a value of n: "))
        if n < 1:
            print("n must be greater than or equal to 1.")
        else:
            if function_name == "t":
                result = tetrahedral_number(n)
            elif function_name == "s":
                result = square_pyramidal_number(n)
            print(f"The result of {function_name}({n}) is: {result}")
    except ValueError as error:
        print("Invalid input. Please enter a positive integer.")