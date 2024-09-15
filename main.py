import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Introduce la longitud de la contraseña: "))

contrasena_generada = ""

for _ in range(longitud):
    contrasena_generada += random.choice(caracteres)

print("Contraseña generada:", contrasena_generada)
