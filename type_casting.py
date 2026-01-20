PI = 3.14159  # a named constant

distance_as_an_integer = 0
distance_as_a_float = 0.0

# Demonstrate assignment with casting
distance_as_a_float = float(input("Enter the distance as a float: "))
distance_as_an_integer = int(distance_as_a_float)  # cast float to int
print(f"Distance as a float {distance_as_a_float}")
print(f"Distance cast to an int {distance_as_an_integer}")
print()

distance_as_an_integer = int(input("Enter the distance as an int: "))
distance_as_a_float = float(distance_as_an_integer)  # convert int to float
print(f"Distance as an int {distance_as_an_integer}")
print(f"Distance assigned to a float {distance_as_a_float}")
