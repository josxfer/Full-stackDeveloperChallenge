# Full-stackDeveloperChallenge

En este repositorio se encuentran tres desafíos desarrollados en **Python**.

Para desarrollar el reto, lo primero que debemos hacer es obtener un número al que vamos a llamar **“S”**, este número lo obtenemos de la URL https://www.md5hashgenerator.com. 

Allí vamos a colocar nuestro nombre y el sistema nos arrojará un *hash*, la idea es trabajar con el primer número que contenga este hash, en mi caso fue el número **5**.

![alt text|50](/img/image.png)




## Desafio 1.

Para este primer desafío, creamos un programa que reciba una lista de números, debemos eliminar todos los dígitos de la lista que sean iguales o superiores a **S (5)** y la lista resultante debemos invertirle su orden, por ejemplo:

**Lista original:** [5, 36, 25, 45, 1, 4, 3, 81, 53, 96, 5, 33, 35]

**Lista después de eliminar dígitos mayores o iguales a S:** [3, 2, 4, 1, 4, 3, 1, 3, 33, 3]

**Lista final invertida:** [3, 33, 3, 1, 3, 4, 1, 4, 2, 3]

Para resolverlo, desarrollamos una función que itera sobre los elementos de la lista, los convierte a String para poder iterar dígito por dígito y hacer una comparación de cada dígito con el valor S, para que al final solo se almacene en una nueva lista el arreglo sin los dígitos que sean iguales o superiores a 5.

![alt text|20](/img/image-1.png)

Posteriormente, con otra función, invertimos el orden de la lista y así obtendremos el resultado esperado.

![alt text](/img/image-2.png)



## Desafio 2.

Acá también vamos a recibir un arreglo de números, pero en esta ocasión estarán ordenados de forma ascendente. La idea es entregar un arreglo también ordenado de forma ascendente, pero con los cuadrados de cada número. Adicional, si quizás hay números que superen al número repetido de la variable S **(en este caso 55)**, tampoco deben estar incluidos en el nuevo arreglo.

Para este reto, es muy importante tener en cuenta que en la lista inicial puede haber números negativos, lo que hará que hagamos un cálculo adicional para que la lista resultante quede en orden ascendente, por ejemplo:

**Lista original:**  [-6, -5, 0, 5, 6]

**Resultado:** [0, 25, 25, 36, 36]

Para desarrollarlo, en la función se declararon dos variables iniciales, *left y right*, estas variables representan los extremos de la lista y la idea es que en cada iteración del bucle se haga una comparación para saber si el número mayor está al principio o al final, de esta forma nos aseguramos de que la lista final quede ordenada de forma descendente.

![alt text](/img/image-4.png)

Ya con esto, lo único que hacemos es invertir el orden de la lista para obtener el resultado final.

![alt text](/img/image-5.png)



## Desafio 3.

En este desafío final, recibimos una lista de números que representan monedas y debemos encontrar la cantidad mínima que **no** se puede representar con estas monedas, por ejemplo:

**Monedas:** [5, 7, 1, 1, 2, 3, 22]

**Cantidad mínima que no se puede representar con estas monedas:**  20

Para encontrar este valor, la forma más fácil es, primero que todo, ordenar la lista de forma ascendente:

![alt text](/img/image6.png)

 Después de ordenada, recorremos la lista, pero en una variable inicializada en 1, vamos sumando el valor de cada moneda. En el momento que el valor de la siguiente moneda, sea mayor al acumulado de la variable, finalizará el bucle y ese valor acumulado será el número mínimo que no se puede representar con esas monedas.

 ![alt text](/img/image7.png)


