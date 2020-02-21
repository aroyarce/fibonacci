# Fibonacci
Calcula la sucesion de Fibonacci

## **Descripcion:**

Mediante la formula Fn = Fn-1 + Fn-2; calcula el valor N de la sucesión de Fibonacci y en numero N-1.
El resultado lo muestra en una tabla dentro de la pagina.

## **Desarrollo:**

Se utilizaron tres metodos para el calculo; un metodo recursivo el cual ocupa demasiado recursos y solo funciona bien hasta N=40; y un metodo loop el cual funciona para valores mucho mayores. Sin embargo a partir de 100, el largo de los numeros sobrepasan el largo visible de la pagina, por lo que solo se limitó a 100.

## **Dependencias:**

Funciona con HTML5 y ECMAScript 7. Esto aplica para las ultimas versioones de Firefox, Chrome y a partir de IE Edge 10.
la página esta cargada en una instancia EC2 de AWS, además de una API también creada en AWS. Se adjunta el código fuente de la función lambda utilizada.

## Ejecución:

La pagina de prueba del algoritmo se encuentra en el siguiente link:

http://18.191.64.70/


## Test:

Se realizaron las siguientes pruebas:

1. Valores negativos: Los algoritmos no funcionan con numeros negativos, por lo que se utilizó un filtro para prevenir el ingreso de éstos.
1. Caracteres no numericos: Del mismo modo anterior, se utilizó un filtro para prevenir el ingreso de caracteres o strings.
1. Copy-Paste: Se deshabilitó la opcion de Paste en el text field para evitar el ingreso de cualquier tipo de caracter no numerico, pero se habilitó el backspace y suprimir para permitir borrar los numeros.
1. Largo Máximo: Se limitó el máximo de digitos a ingresar a 3, para evitar over processing.
1. Límite de Rango: Se limitó el máximo numero a ingresar en un rango entre 0 y 100. 
1. Utilizando POSTMAN se creó un script de pruebas entre 1 y 100, el cual se comparó con una tabla prefabricada con los valores de la serie de fibonacci. 
