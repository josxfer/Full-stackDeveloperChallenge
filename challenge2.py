S = 5

def sortedSquares(list, S):
    # Crear una lista vacía para almacenar los resultados
    result = []
    left, right = 0, len(list) - 1
    max_square = int(str(S) * 2)  # Máximo valor permitido (SS)
    
    while left <= right:
        left_square = list[left] ** 2
        right_square = list[right] ** 2
        
        if left_square <= right_square:
            if right_square <= max_square:
                result.append(right_square)
            right -= 1
        else:
            if left_square <= max_square:
                result.append(left_square)
            left += 1
    
    # Como los mayores cuadrados fueron añadidos primero, invertimos la lista
    return result[::-1]

# Ejemplos

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Lista original: ", list)
print("Resultado: ", sortedSquares(list, S))
print("-----------------------------------")

list = [-2, -1]
print("Lista original: ", list)
print("Resultado: ", sortedSquares(list, S))
print("-----------------------------------")

list = [-6, -5, 0, 5, 6]
print("Lista original: ", list)
print("Resultado: ", sortedSquares(list, S))
print("-----------------------------------")

list = [-10, 10]
print("Lista original: ", list)
print("Resultado: ", sortedSquares(list, S))
print("-----------------------------------")
