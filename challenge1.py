def deleteDigit(list, S):
    new_list = []
    for num in list:
        # Convertimos el número a cadena y eliminamos los dígitos mayores o iguales a S
        new_num_str = ''.join([digit for digit in str(num) if int(digit) < S])
        if new_num_str:  # Verificamos que no sea una cadena vacía
            new_list.append(int(new_num_str))
    return new_list

# Función para invertir la lista
def reverseList(list):
    return list[::-1]

# Lista de ejemplo
list = [5, 36, 25, 45, 1, 4, 3, 81, 53, 96, 5, 33, 35]
print("Lista original:", list)

# Aplicamos la función para eliminar dígitos mayores o iguales a S
S = 5
result = deleteDigit(list, S)
print("Lista después de eliminar dígitos mayores o iguales a S:", result)

# Invertimos la lista resultante
result = reverseList(result)
print("Lista final invertida:", result)
