'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio'''


def num_maximo(num1, num2):
    if num1 > num2:
        return f"El numero maximo es: {num1}"
    else:
        return f"El numero maximo es: {num2}"


resultado = num_maximo(10, 25)
print(resultado)
