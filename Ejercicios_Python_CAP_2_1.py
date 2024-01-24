# ---------------------------------------------------------------------
# Introducción --
# ---------------------------------------------------------------------
# En esta relación se presentan ejercicios con definiciones por
# comprensión correspondientes al tema 5 que se encuentra en
# https://jaalonso.github.io/cursos/i1m/temas/tema-5.html
# ---------------------------------------------------------------------
# Librerías auxiliares --
# ---------------------------------------------------------------------
from itertools import islice
'''
islice('ABCDEFG', 2, None) --> C D E F G
'''
from math import ceil, e, pi, sin, sqrt, trunc
from sys import setrecursionlimit
'''
Set the maximum depth of the Python interpreter stack to limit. This limit
prevents infinite recursion from causing an overflow of the C stack and crashing
Python.
The highest possible limit is platform-dependent. A user may need to set the
limit higher when they have a program that requires deep recursion and a
platform that supports a higher limit. This should be done with care, because a
too-high limit can lead to a crash.
If the new limit is too low at the current recursion depth, a RecursionError
exception is raised.
Changed in version 3.5.1: A RecursionError exception is now raised if the new
limit is too low at the current recursion depth.
'''
from timeit import Timer, default_timer
'''
This module provides a simple way to time small bits of Python code. It has both
a Command-Line Interface as well as a callable one. It avoids a number of
common traps for measuring execution times.
'''
from typing import Iterator, TypeVar
from hypothesis import given, settings
from hypothesis import strategies as st

from icecream import ic

A = TypeVar('A')
setrecursionlimit(10**6)

# ---------------------------------------------------------------------
# Ejercicio 1.1. (Problema 6 del proyecto Euler) En los distintos
# apartados de este ejercicio se definen funciones para resolver el
# problema 6 del proyecto Euler https://www.projecteuler.net/problem=6
#
# Definir, por comprensión, la función
# suma : (int) -> int
# tal suma(n) es la suma de los n primeros números. Por ejemplo,
# suma(3) == 6
# len(str(suma2(10**100))) == 200
# ---------------------------------------------------------------------
def suma1(n: int) -> int:
	return sum(range(1, n + 1))


def suma2(n: int) -> int:
	return (1 + n) * n // 2


# #Comprobar equivalencia
# @settings(max_examples=50)
# @given(st.integers(min_value=1, max_value=1000))
# def test_suma(n: int):
# 	assert suma1(n) == suma2(n)

# Comparar eficiencia
# def tiempo(ex: str):
# 	'''Tiempo(en segundos) de evaluar la expresión ex.'''
# 	t = Timer(ex,"", default_timer, globals()).timeit(1)
# 	print(f"{t:0.2f} segundos")
#
# tiempo('suma1(10**8)')
# tiempo('suma2(10**8)')


# ---------------------------------------------------------------------
# Ejercicio 1.2. Definir, por comprensión, la función
# sumaDeCuadrados : (int) -> int
# tal sumaDeCuadrados(n) es la suma de los cuadrados de los n primeros
# números naturales. Por ejemplo,
# sumaDeCuadrados(3) == 14
# sumaDeCuadrados(100) == 338350
# len(str(sumaDeCuadrados2(10**100))) == 300
# ---------------------------------------------------------------------
def sumaCuadrados(n: int) -> int:
	res = 0
	for num in range(1, n + 1):
		res = res + num**2
	return res


def sumaCuadrados2(n: int) -> int:
	return sum(x**2 for x in range(1, n + 1))

# ic(sumaCuadrados(100))
# ic(sumaCuadrados2(100))
#
# @given(st.integers(min_value=1, max_value=1000))
# def test_sumaCuadrados(n: int):
# 	assert sumaCuadrados(n) == sumaCuadrados2(n)


# loop = 1
# def timing(ex: str) -> float:
# 	t = Timer(ex, "", default_timer, globals=globals()).timeit()
# 	global loop
# 	print(f"time {loop}: {t:0.2f} segundos")
# 	loop += 1
#
# timing("sumaCuadrados")
# timing("sumaCuadrados2")


# ---------------------------------------------------------------------
# Ejercicio 1.3. Definir la función
# euler6 : (int) -> int
# tal que euler6(n) es la diferencia entre el cuadrado de la suma
# de los n primeros números y la suma de los cuadrados de los n
# primeros números. Por ejemplo,
# euler6(10) == 2640
# euler6(10^10) == 2500000000166666666641666666665000000000
# ---------------------------------------------------------------------
def euler6(n: int) -> int:
	return suma1(n)**2 - sumaCuadrados(n)

# ic(euler6(10))
# ic(euler6(10**8))


# ---------------------------------------------------------------------
# Ejercicio 2. Definir, por comprensión, la función
# replica : (int, A) -> list[A]
# tal que replica(n, x) es la lista formada por n copias del elemento
# x. Por ejemplo,
# replica(4, 7) == [7,7,7,7]
# replica(3, True) == [True, True, True]
# ---------------------------------------------------------------------
def replica(n: int, x) -> list:
	ret = []
	for i in range(n):
		ret.append(x)
	return ret


def replica2(n: int, x) -> list:
	return [x for _ in range(0, n)]

# # ic(replica2(4, 7))
# # ic(replica2(3, True))
#
# Comprobacion equivalencias
# @given(st.integers(min_value=5, max_value=100), st.integers(max_value=100))
# def test_replica(n: int, x: int):
# 	assert replica(n, x) == replica2(n, x)

# Comprobación tiempo
# def timing(ex: str) -> int:
# 	t = Timer(ex, "", default_timer, globals=globals()).timeit()
# 	print(f"{ex}: {t} seconds")
#
# timing("replica(4, 7)")
# timing('replica2(4, 7)')


# ---------------------------------------------------------------------
# Ejercicio 3.1. Los triángulos aritméticos se forman como sigue
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
#
# Definir la función
# linea : (int) -> list[int]
# tal que linea(n) es la línea n-ésima de los triángulos
# aritméticos. Por ejemplo,
# linea(4) == [7, 8, 9, 10]
# linea(5) == [11, 12, 13, 14, 15]
# linea(10**8)[0] == 4999999950000001
# ---------------------------------------------------------------------
def linea(n: int) -> list:
	return list(range(suma1(n - 1) + 1, suma1(n) + 1))

# ic(linea(5))
# ic(linea(4))
# ic(linea(6))
# ic(linea(10**8)[0])


# ---------------------------------------------------------------------
# Ejercicio 3.2. Definir la función
# triangulo : (int) -> list[list[int]]
# tale que triangulo(n) es el triángulo aritmético de altura n. Por
# ejemplo,
# triangulo(3) == [[1], [2, 3], [4, 5, 6]]
# triangulo(4) == [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
# ---------------------------------------------------------------------
def triangulo(n: int) -> list[list[int]]:
	ret = []
	for i in range(1, n + 1):
		ret.append(linea(i))
	return ret


def triangulo2(n: int) -> list[list[int]]:
	return [linea(i) for i in range(1, n+1)]

# ic(triangulo2(3))

# Comprobación equivalencias
# @given(st.integers(min_value=1, max_value=10))
# def test_triangulo(n: int) -> None:
# 	assert triangulo(n) == triangulo2(n)

# Comprobación tiempo
# def timing(ex: str) -> None:
# 	t = Timer(ex, "", default_timer, globals=globals()).timeit()
# 	print(f"{ex}: {t}s")
#
# timing("triangulo(10)")
# timing("triangulo2(10)")


# ---------------------------------------------------------------------
# Ejercicio 4. Un números entero positivo es perfecto si es igual a la
# suma de sus divisores, excluyendo el propio número. Por ejemplo, 6 es
# un número perfecto porque sus divisores propios son 1, 2 y 3; y
# 6 = 1 + 2 + 3.
#
# Definir, por comprensión, la función
# perfectos (int) -> list[int]
# tal que perfectos(n) es la lista de todos los números perfectos
# menores que n. Por ejemplo,
# perfectos(500) == [6, 28, 496]
# perfectos(10**5) == [6, 28, 496, 8128]
# ---------------------------------------------------------------------
def divisores(n: int) -> list[int]:
	return [i for i in range(1, n + 1) if n % i == 0]


def sumaDivisores(n: int) -> int:
	return sum(divisores(n))


def esPerfecto(n: int) -> bool:
	return sumaDivisores(n) - n == n


def perfectos(n: int) -> list[int]:
	return [x for x in range(1, n + 1) if esPerfecto(x)]

# ic(perfectos(500))


# ---------------------------------------------------------------------
# Ejercicio 5.1. Un número natural n se denomina abundante si es menor
# que la suma de sus divisores propios. Por ejemplo, 12 es abundante ya
# que la suma de sus divisores propios es 16 (= 1 + 2 + 3 + 4 + 6), pero
# 5 y 28 no lo son.
#
# Definir la función
# numeroAbundante : (int) -> bool
# tal que numeroAbundante(n) se verifica si n es un número
# abundante. Por ejemplo,
# numeroAbundante(5) == False
# numeroAbundante(12) == True
# numeroAbundante(28) == False
# numeroAbundante(30) == True
# numeroAbundante(100000000) == True
# numeroAbundante(100000001) == False
# ---------------------------------------------------------------------
def numeroAbundante(n: int) -> bool:
	return sumaDivisores(n) - n > n

# ic(numeroAbundante(5))
# ic(numeroAbundante(12))
# ic(numeroAbundante(28))
# ic(numeroAbundante(30))
# ic(numeroAbundante(100000000))
# ic(numeroAbundante(100000001))


# ---------------------------------------------------------------------
# Ejercicio 5.2. Definir la función
# numerosAbundantesMenores : (int) -> list[Int]
# tal que numerosAbundantesMenores(n) es la lista de números
# abundantes menores o iguales que n. Por ejemplo,
# numerosAbundantesMenores(50) == [12,18,20,24,30,36,40,42,48]
# numerosAbundantesMenores(48) == [12,18,20,24,30,36,40,42,48]
# leng(numerosAbundantesMenores(10**6)) == 247545
# ---------------------------------------------------------------------
def numerosAbundantesMenores(n: int) -> list[int]:
	return [x for x in range(1, n + 1) if numeroAbundante(x)]

# ic(numerosAbundantesMenores(50))
# ic(numerosAbundantesMenores(48))
# ic(len(numerosAbundantesMenores(10**6)))


# ---------------------------------------------------------------------
# Ejercicio 5.3. Definir la función
# todosPares : (int) -> bool
# tal que todosPares(n) se verifica si todos los números abundantes
# menores o iguales que n son pares. Por ejemplo,
# todosPares(10) == True
# todosPares(100) == True
# todosPares(1000) == False
# ---------------------------------------------------------------------
def todosPares(n: int) -> bool:
	for i in numerosAbundantesMenores(n):
		if i % 2 != 0:
			return False
	return True


def todosPares2(n: int) -> bool:
	return False not in [i % 2 == 0 for i in numerosAbundantesMenores(n)]
	'''Explicacion
	recorre la lista que devuelve la funcion numerosAbundantesMenores()
	y comprueba si cada numero es par, generando una nueva lista de booleanos.
	Si no encuentra False en la lista, retorna True.'''

# Comprobación equivalencias
# @given(st.integers(min_value=1, max_value=1000))
# def test_todosPares(n: int):
# 	assert todosPares(n) == todosPares2(n)

# Comprobación tiempos
# def timing(ex: str):
# 	t = Timer(ex, "", default_timer, globals=globals()).timeit()
# 	print(f"{ex}: {t} seconds")
#
# ic(todosPares2(10))
# ic(todosPares(1000))
# timing("todosPares(10)")
# timing("todosPares2(10)")


# ---------------------------------------------------------------------
# Ejercicio 6. Definir la función
# euler1 : (int) -> int
# tal que euler1(n) es la suma de todos los múltiplos de 3 ó 5 menores
# que n. Por ejemplo,
# euler1(10) == 23
# euler1(10**2) == 2318
# euler1(10**3) == 233168
# euler1(10**4) == 23331668
# euler1(10**5) == 2333316668
# euler1(10**10) == 23333333331666666668
# euler1(10**20) == 2333333333333333333316666666666666666668
#
# Nota: Este ejercicio está basado en el problema 1 del Proyecto Euler
# https://projecteuler.net/problem=1
# ---------------------------------------------------------------------
def euler1(n: int) -> int:
	return sum([x for x in range(1, n) if (x % 3 == 0 or x % 5 == 0)])

# ic(euler1(10))
# ic(euler1(10**2))
# ic(euler1(10**4))
# ic(euler1(10**10))


# ---------------------------------------------------------------------
# Ejercicio 7. En el círculo de radio 2 hay 6 puntos cuyas coordenadas
# son puntos naturales:
# (0,0),(0,1),(0,2),(1,0),(1,1),(2,0)
# y en de radio 3 hay 11:
# (0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0)
#
# Definir la función
# circulo : (int) -> int
# tal que circulo(n) es el la cantidad de pares de números naturales
# (x,y) que se encuentran en el círculo de radio n. Por ejemplo,
# circulo(1) == 3
# circulo(2) == 6
# circulo(3) == 11
# circulo(4) == 17
# circulo(100) == 7955
# ---------------------------------------------------------------------
def circulo1(n: int) -> int:
	return len([(x, y) for x in range(0, n + 1) for y in range(0, n + 1)
	            if x * x + y * y <= n * n])

# ic(circulo1(1))
# ic(circulo1(2))
# ic(circulo1(3))
# ic(circulo1(4))
# ic(circulo1(100))


# ---------------------------------------------------------------------
# Ejercicio 8.1. El número e se define como el límite de la sucesión
# (1+1/n)**n; es decir,
# e = lim (1+1/n)**n
#
# Definir la función
# aproxE : (int) -> list[float]
# tal que aproxE(k) es la lista de los k primeros términos de la
# sucesión (1+1/n)**m. Por ejemplo,
# aproxE(4) == [2.0, 2.25, 2.37037037037037, 2.44140625]
# aproxE6(7*10**7)[-1] == 2.7182818287372563
# ---------------------------------------------------------------------
def aproxE(k: int) -> list[float]:
	ret = []
	for i in range(1, k + 1):
		ret.append((1 + 1/i) ** i)
	return ret


def aproxE2(k: int) -> list[float]:
	return [(1 + 1/i) ** i for i in range(1, k + 1)]

# ic(aproxE2(4))
# ic(aproxE2(7*10**7)[-1])

# Comprobación de tiempos
# def timing(ex: str) -> int:
# 	t = Timer(ex, "", default_timer, globals=globals()).timeit()
# 	print(f"{ex}: {t} seconds")
#
# timing("aproxE(4)")
# timing("aproxE2(4)")


# ---------------------------------------------------------------------
# Ejercicio 8.2. Definir la función
# errorAproxE : (float) -> int
# tal que errorE(x) es el menor número de términos de la sucesión
# (1+1/m)**m necesarios para obtener su límite con un error menor que
# x. Por ejemplo,
# errorAproxE(0.1) == 13
# errorAproxE(0.01) == 135
# errorAproxE(0.001) == 1359
# ---------------------------------------------------------------------
# naturales es el generador de los números naturales positivos, Por
# ejemplo,
# >>> list(islice(naturales(), 5))
# [1, 2, 3, 4, 5]
'''
La parte del `yield` en una función generadora es esencial
para entender cómo funciona el generador y cómo se comporta cuando se utiliza
en un bucle o al obtener un iterador.

En este caso:

```python
yield i
```

La función `naturales` produce el valor actual de la variable `i` utilizando la
instrucción `yield`. Cuando la función es llamada por primera vez, produce el
número 1, y en cada llamada subsiguiente, produce el siguiente número
natural (2, 3, 4, y así sucesivamente).

Aquí hay un ejemplo de cómo podrías usar la función `naturales` en un bucle `for`
para imprimir los primeros cinco números naturales:

for numero in naturales():
    print(numero)
    if numero == 5:
        break

Este bucle imprimirá los números del 1 al 5 y luego se romperá, pero la función
`naturales` podría seguir utilizándose para generar más números naturales si
fuera necesario. La clave aquí es que la función `naturales` mantiene su estado
entre las llamadas, gracias al uso de `yield`. Cada vez que se alcanza la
instrucción `yield`, la función se pausa y retiene su estado, permitiendo que
se reanude desde ese punto en la próxima llamada.
'''
def naturales() -> Iterator[int]:
	i = 1
	while True:
		yield i
		i += 1

def errorAproxE(x: float) -> int:
	return list(islice((n for n in naturales()
	                    if abs(e - (1 + 1/n)**n) < x), 1))[0]

# ic(errorAproxE(0.1))
# ic(errorAproxE(0.01))
# ic(errorAproxE(0.001))


# ---------------------------------------------------------------------
# Ejercicio 10.1. El número π puede calcularse con la fórmula de
# Leibniz
# π/4 = 1 - 1/3 + 1/5 - 1/7 + ...+ (-1)**n/(2*n+1) + ...
#
# Definir la función
# calculaPi : (int) -> float
# tal que calculaPi(n) es la aproximación del número π calculada
# mediante la expresión
# 4*(1 - 1/3 + 1/5 - 1/7 + ...+ (-1)**n/(2*n+1))
# Por ejemplo,
# calculaPi(3) == 2.8952380952380956
# calculaPi(300) == 3.1449149035588526
# ---------------------------------------------------------------------
def calculaPi(n: int) -> float:
	return 4 * sum((-1) ** x / (2 * x + 1) for x in range (n + 1))

# ic(calculaPi(0))
# ic(calculaPi(3))
# ic(calculaPi(300))


# ---------------------------------------------------------------------
# Ejercicio 11.1. Una terna (x,y,z) de enteros positivos es pitagórica
# si x^2 + y^2 = z^2 y x < y < z.
# Definir, por comprensión, la función
# pitagoricas : (int) -> list[tuple[int,int,int]]
# tal que pitagoricas(n) es la lista de todas las ternas pitagóricas
# cuyas componentes están entre 1 y n. Por ejemplo,
# pitagoricas(10) == [(3, 4, 5), (6, 8, 10)]
# pitagoricas(15) == [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)]
# ---------------------------------------------------------------------
def pitagoricas(n: int) -> list[tuple[int, int, int]]:
	return [(x, y, z) for x in range(1, n + 1)
	        for y in range(1, n + 1)
	        for z in range(1, n + 1)
	        if x**2 + y**2 == z**2 and x < y < z ]

def pitagoricas2(n: int) -> list[tuple[int, int, int]]:
	ret = []
	for x in range(1, n + 1):
		for y in range(1, n + 1):
			for z in range(1, n + 1):
				if (x**2 + y**2 == z**2) and x < y < z:
					ret.append((x, y, z))
	return ret

# ic(pitagoricas2(10))
# ic(pitagoricas2(15))

# Comprobación equivalencias

# @given(st.integers(min_value=1, max_value=10))
# def test_pitagoricas(n: int):
# 	assert pitagoricas(n) == pitagoricas2(n)


# ---------------------------------------------------------------------
# Ejercicio 11.2. Definir la función
# numeroDePares : (int, int, int) -> int
# tal que numeroDePares(t) es el número de elementos pares de la terna
# t. Por ejemplo,
# numeroDePares(3, 5, 7) == 0
# numeroDePares(3, 6, 7) == 1
# numeroDePares(3, 6, 4) == 2
# numeroDePares(4, 6, 4) == 3
# ---------------------------------------------------------------------
def numeroDePares(x: int, y:int, z: int) -> int:
	return len([par for par in [x, y, z] if par % 2 == 0])

# ic(numeroDePares(3, 5, 7))
# ic(numeroDePares(3, 6, 7))
# ic(numeroDePares(4, 6, 4))


# ---------------------------------------------------------------------
# Ejercicio 11.3. Definir la función
# conjetura : (int) -> bool
# tal que conjetura(n) se verifica si todas las ternas pitagóricas
# cuyas componentes están entre 1 y n tiene un número impar de números
# pares. Por ejemplo,
# conjetura(10) == True
# ---------------------------------------------------------------------
def conjetura(n: int) -> bool:
	return False not in [numeroDePares(x, y, z) % 2 == 1
	                     for (x, y, z) in pitagoricas(n)]
# ic(conjetura(10))


# ---------------------------------------------------------------------
# Ejercicio 13. El producto escalar de dos listas de enteros xs y ys de
# longitud n viene dado por la suma de los productos de los elementos
# correspondientes.
#
# Definir, por comprensión, la función
# productoEscalar : (list[int], list[int]) -> int
# tal que productoEscalar(xs, ys) es el producto escalar de las listas
# xs e ys. Por ejemplo,
# productoEscalar([1, 2, 3], [4, 5, 6]) == 32
# ---------------------------------------------------------------------
def productoEscalar(xs: list[int], ys: list[int]) -> int:
	return sum(xs[i] * ys[i] for i in range(0, len(xs)))

def productoEscalar2(xs: list[int], ys: list[int]) -> int:
	return sum(x * y for (x, y) in zip(xs, ys))

# ic(productoEscalar2([1, 2, 3], [4, 5, 6]))

#Comprobaciòn equivalencia
# @given(st.lists(st.integers(),min_size=10, max_size=10),
#        st.lists(st.integers(),min_size=10, max_size=10))
# def test_productoEscalar(xs: list[int], ys: list[int]):
# 	assert productoEscalar(xs, ys) == productoEscalar2(xs, ys)

#Comprobación tiempos
# def timing(ex: str) -> int:
# 	t = Timer(ex, "", default_timer, globals=globals()).timeit()
# 	print(f"{ex}: {t} seconds")
#
# timing("productoEscalar([1, 2, 3], [4, 5, 6])")
# timing("productoEscalar2([1, 2, 3], [4, 5, 6])")


# ---------------------------------------------------------------------
# Ejercicio 14. Definir , por comprensión,la función
# sumaConsecutivos : (list[int]) -> list[int]
# tal que sumaConsecutivos(xs) es la suma de los pares de elementos
# consecutivos de la lista xs. Por ejemplo,
# sumaConsecutivos([3, 1, 5, 2]) == [4, 6, 7]
# sumaConsecutivos([3]) == []
# sumaConsecutivos(range(1, 1+10**8))[-1] == 199999999
# ---------------------------------------------------------------------
def sumaConsecutivos(xs: list[int]) -> list[int]:
	sum = []
	i = 0
	j = 0
	while i < len(xs) - 1:
		j = i + 1
		sum.append(xs[i] + xs[j])
		i += 1
	return sum


def sumaConsecutivos2(xs: list[int]) -> list[int]:
	return [(x + y) for (x, y) in zip(xs[:], xs[1:])]

# ic(sumaConsecutivos2([2, 3, 4]))
# ic(sumaConsecutivos2([3, 1, 5, 2]))
# ic(sumaConsecutivos2([3]))


# Ejercicio 15. Los polinomios pueden representarse de forma dispersa o
# densa. Por ejemplo, el polinomio 6x^4-5x^2+4x-7 se puede representar
# de forma dispersa por [6,0,-5,4,-7] y de forma densa por
# [(4,6),(2,-5),(1,4),(0,-7)].
#
# Definir la función
# densa : (list[int]) -> list[tuple[int, int]]
# tal que densa(xs) es la representación densa del polinomio cuya
# representación dispersa es xs. Por ejemplo,
# densa([6, 0, -5, 4, -7]) == [(4, 6), (2, -5), (1, 4), (0, -7)]
# densa([6, 0, 0, 3, 0, 4]) == [(5, 6), (2, 3), (0, 4)]
# densa([0]) == [(0, 0)]
# ---------------------------------------------------------------------
def densa(xs: list[int]) -> list[tuple[int, int]]:
	ret = []
	size = len(xs) -1
	for i in xs:
		if i != 0:
			ret.append((size, i))
		size -= 1
	return ret

# ic(densa([6, 0, -5, 4, -7]))
# ic(densa([6, 0, 0, 3, 0, 4]))
# ic(densa([0]))


# ---------------------------------------------------------------------
# Ejercicio 16. Las bases de datos sobre actividades de personas pueden
# representarse mediante listas de elementos de la forma (a,b,c,d),
# donde a es el nombre de la persona, b su actividad, c su fecha de
# nacimiento y d la de su fallecimiento. Un ejemplo es la siguiente que
# usaremos a lo largo de este ejercicio,
# BD = list[tuple[str, str, int, int]]
#
# personas: BD = [
# (”Cervantes”, ”Literatura”, 1547, 1616),
# (”Velazquez”, ”Pintura”, 1599, 1660),
# (”Picasso”, ”Pintura”, 1881, 1973),
# (”Beethoven”, ”Musica”, 1770, 1823),
# (”Poincare”, ”Ciencia”, 1854, 1912),
# (”Quevedo”, ”Literatura”, 1580, 1654),
# (”Goya”, ”Pintura”, 1746, 1828),
# (”Einstein”, ”Ciencia”, 1879, 1955),
# (”Mozart”, ”Musica”, 1756, 1791),
# (”Botticelli”, ”Pintura”, 1445, 1510),
# (”Borromini”, ”Arquitectura”, 1599, 1667)
# (”Bach”, ”Musica”, 1685, 1750)]
# ---------------------------------------------------------------------
BD = list[tuple[str, str, int, int]]
personas: BD = [
	('Cervantes', 'Literatura', 1547, 1616),
	('Velazquez', 'Pintura', 1599, 1660),
	('Picasso', 'Pintura', 1881, 1973),
	('Beethoven', 'Musica', 1770, 1823),
	('Poincare', 'Ciencia', 1854, 1912),
	('Quevedo', 'Literatura', 1580, 1654),
	('Goya', 'Pintura', 1746, 1828),
	('Einstein', 'Ciencia', 1879, 1955),
	('Mozart', 'Musica', 1756, 1791),
	('Botticelli', 'Pintura', 1445, 1510),
	('Borromini', 'Arquitectura', 1599, 1667),
	('Bach', 'Musica', 1685, 1750)]


# ---------------------------------------------------------------------
# Ejercicio 16.1. Definir la función
# nombres : (BD) -> list[str]
# tal que nombres(bd) es la lista de los nombres de las personas de la-
# base de datos bd. Por ejemplo,
# >>> nombres(personas)
# ['Cervantes', 'Velazquez', 'Picasso', 'Beethoven', 'Poincare',
# 'Quevedo', 'Goya', 'Einstein', 'Mozart', 'Botticelli', 'Borromini',
# 'Bach']
# ---------------------------------------------------------------------
def nombres(personas: BD) -> list[str]:
	return [name[0] for name in personas]

# ic(nombres(personas))


# ---------------------------------------------------------------------
# Ejercicio 16.2. Definir la función
# musicos : (BD) -> list[str]
# tal que musicos(bd) es la lista de los nombres de los músicos de la
# base de datos bd. Por ejemplo,
# musicos(personas) == ['Beethoven', 'Mozart', 'Bach']
# ---------------------------------------------------------------------
def musicos(bd: BD) -> list[str]:
	return [name[0] for name in bd if name[1] == 'Musica']

# ic(musicos(personas))


# ---------------------------------------------------------------------
# Ejercicio 16.3. Definir la función
# seleccion : (BD, str) -> list[str]
# tal que seleccion(bd, m) es la lista de los nombres de las personas de
# la base de datos bd cuya actividad es m. Por ejemplo,
# >>> seleccion(personas, 'Pintura')
# ['Velazquez', 'Picasso', 'Goya', 'Botticelli']
# >>> seleccion(personas, 'Musica')
# ['Beethoven', 'Mozart', 'Bach']
# ---------------------------------------------------------------------
def seleccion(bd: BD, m: str) -> list[str]:
	return [x[0] for x in bd if x[1] == m]

# ic(seleccion(personas, 'Pintura'))
# ic(seleccion(personas, 'Musica'))


# ---------------------------------------------------------------------
# Ejercicio 16.4. Definir la función
# musicos2 : (BD) -> list[str]
# tal que musicos2(bd) es la lista de los nombres de los músicos de la
# base de datos bd. Por ejemplo,
# musicos2(personas) == ['Beethoven','Mozart','Bach']
# ---------------------------------------------------------------------
def musicos2(bd: BD) -> list[str]:
	return seleccion(bd, 'Musica')

# ic(musicos2(personas))


# ---------------------------------------------------------------------
# Ejercicio 16.5. Definir la función
# vivas : (BD, int) -> list[str]
# tal que vivas(bd, a) es la lista de los nombres de las personas de la
# base de datos bd que estaban vivas en el año a. Por ejemplo,
# >>> vivas(personas, 1600)
# ['Cervantes', 'Velazquez', 'Quevedo', 'Borromini']
# ---------------------------------------------------------------------
def vivas(bd: BD, a: int) -> list[str]:
	return [x[0] for x in bd if x[2] <= a <= x[3]]

# ic(vivas(personas, 1600))