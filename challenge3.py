def minimum_change(coins):
    # Ordenar la lista de monedas
    coins.sort()
    
    # Inicializar la cantidad de cambio que no se puede representar
    min_change = 1
    
    # Recorrer cada moneda en la lista ordenada
    for coin in coins:
        # Si la moneda es mayor que la cantidad de cambio que no se puede representar, salimos del bucle
        if coin > min_change:
            break
        
        # Si no,  se actualiza la cantidad mínima de cambio que no se puede representar
        min_change += coin
    
    return min_change

list1 = [5, 7, 1, 1, 2, 3, 22]
list2 = [1, 1, 1, 1, 1]
list3 = [1, 5, 1, 1, 1, 10, 15, 20, 100]

# Ejemplos:
print("Monedas: ", list1)
print("Cantidad minima que no se puede representar con estas monedas: ", minimum_change(list1))
print("-------------------------------------------")
print("Monedas: ", list2)
print("Cantidad minima que no se puede representar con estas monedas: ", minimum_change(list2))
print("-------------------------------------------")
print("Monedas: ", list3)
print("Cantidad minima que no se puede representar con estas monedas: ", minimum_change(list3))
