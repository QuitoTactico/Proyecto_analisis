import math

def calculate_errors(x_real, x_approx):
    # Calcula el error absoluto
    absolute_error = abs(x_real - x_approx)

    # Calcula el error relativo
    relative_error = absolute_error / abs(x_real)

    return absolute_error, relative_error

def round_value(x, num_digits):
    # Redondea x a la cantidad especificada de dígitos
    return round(x, num_digits)

def absolute_value(x):
    # Devuelve el valor absoluto de x
    return abs(x)

def to_bits(x, num_bits):
    # Convierte x a una representación de bits con la cantidad especificada de bits
    return bin(x)[2:].zfill(num_bits)

# Prueba las funciones
x_real = 3.14159
x_approx = 3.14
num_digits = 2
num_bits = 8

absolute_error, relative_error = calculate_errors(x_real, x_approx)
x_rounded = round_value(x_real, num_digits)
x_absolute = absolute_value(x_real)
x_bits = to_bits(int(x_real), num_bits)

print(f"Error absoluto: {absolute_error}")
print(f"Error relativo: {relative_error}")
print(f"x redondeada: {x_rounded}")
print(f"x absoluta: {x_absolute}")
print(f"x en bits: {x_bits}")