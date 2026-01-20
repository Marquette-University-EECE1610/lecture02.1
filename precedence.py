"""
Operator Precedence in Python
=============================
This program demonstrates the rules of operator precedence in Python.
"""

print("=" * 60)
print("OPERATOR PRECEDENCE IN PYTHON")
print("=" * 60)

print("\n1. BASIC ARITHMETIC OPERATORS (work on two operands)")
print("-" * 60)

print("\nAddition (+):")
print("  5 + 3 =", 5 + 3)

print("\nSubtraction (-):")
print("  10 - 4 =", 10 - 4)

print("\nMultiplication (*):")
print("  6 * 7 =", 6 * 7)

print("\nDivision (/):")
print("  15 / 4 =", 15 / 4)

print("\nFloor Division (//):")
print("  15 // 4 =", 15 // 4)

print("\nModulus (%):")
print("  15 % 4 =", 15 % 4)

print("\nExponentiation (**):")
print("  2 ** 3 =", 2**3)

print("\n\n2. UNARY OPERATORS (work on one operand)")
print("-" * 60)

print("\nUnary Plus (+):")
print("  +5 =", +5)

print("\nUnary Minus (-):")
print("  -5 =", -5)
print("  -(10 - 3) =", -(10 - 3))

print("\n\n3. OPERATOR PRECEDENCE RULES")
print("-" * 60)
print("\nOrder (highest to lowest):")
print("  1. Parentheses ()")
print("  2. Exponentiation **")
print("  3. Unary +, -")
print("  4. Multiplication *, Division /, Floor Division //, Modulus %")
print("  5. Addition +, Subtraction -")

print("\n\nEXAMPLES:")
print("-" * 60)

print("\nExample 1: Multiplication before Addition")
print("  2 + 3 * 4")
print("  = 2 + 12")
print("  =", 2 + 3 * 4)

print("\nExample 2: Exponentiation before Multiplication")
print("  2 * 3 ** 2")
print("  = 2 * 9")
print("  =", 2 * 3**2)

print("\nExample 3: Division before Subtraction")
print("  10 - 8 / 2")
print("  = 10 - 4.0")
print("  =", 10 - 8 / 2)

print("\nExample 4: Parentheses override precedence")
print("  (2 + 3) * 4")
print("  = 5 * 4")
print("  =", (2 + 3) * 4)

print("\nExample 5: Complex expression")
print("  2 + 3 * 4 ** 2 / 2")
print("  = 2 + 3 * 16 / 2")
print("  = 2 + 48 / 2")
print("  = 2 + 24.0")
print("  =", 2 + 3 * 4**2 / 2)

print("\nExample 6: Unary minus with exponentiation")
print("  -2 ** 2")
print("  = -(2 ** 2)  [** has higher precedence than unary -]")
print("  = -4")
print("  =", -(2**2))

print("\n  (-2) ** 2")
print("  = 4")
print("  =", (-2) ** 2)

print("\nExample 7: Same precedence (left to right)")
print("  20 / 4 * 5")
print("  = 5.0 * 5")
print("  =", 20 / 4 * 5)

print("\nExample 8: Modulus with other operations")
print("  10 + 15 % 4 * 2")
print("  = 10 + 3 * 2")
print("  = 10 + 6")
print("  =", 10 + 15 % 4 * 2)

print("\nExample 9: Floor division in expression")
print("  17 // 5 + 3 * 2")
print("  = 3 + 3 * 2")
print("  = 3 + 6")
print("  =", 17 // 5 + 3 * 2)

print("\nExample 10: Unary and binary operators")
print("  -5 + 3 * -2")
print("  = -5 + (3 * -2)")
print("  = -5 + (-6)")
print("  =", -5 + 3 * -2)

print("\nExample 11: Unary minus with three exponentiations")
print("  -2 ** 2 ** 3")
print("  = -2 ** (2 ** 3)  [** is right-associative]")
print("  = -2 ** 8")
print("  = -(2 ** 8)")
print("  = -256")
print("  =", -(2**2**3))

print("\n  (-2) ** 2 ** 3")
print("  = (-2) ** (2 ** 3)")
print("  = (-2) ** 8")
print("  = 256")
print("  =", (-2) ** 2**3)
