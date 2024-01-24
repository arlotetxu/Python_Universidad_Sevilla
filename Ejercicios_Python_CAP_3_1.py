# ---------------------------------------------------------------------
# Introducción --
# ---------------------------------------------------------------------
# En esta relación se presentan ejercicios con definiciones por
# recursión correspondientes al tema 6 que se encuentra en
# https://jaalonso.github.io/cursos/i1m/temas/tema-6.html
# ---------------------------------------------------------------------
# Importación de librerías auxiliares --
# ---------------------------------------------------------------------
from itertools import islice
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator, TypeVar
from hypothesis import given, strategies as st, settings
from icecream import ic

setrecursionlimit(10**6)


# ---------------------------------------------------------------------
# Ejercio 1. Definir, por recursión, la función
# potencia : (int, int) -> int
# tal que potencia(x, n) es x elevado al número natural n. Por ejemplo,
# potencia(2, 3) == 8
# ---------------------------------------------------------------------
def potencia(x: int, n: int) -> int:
	if n == 0:
		return 1
	res = x * potencia(x, n - 1)
	return res

# ic(potencia(2, 4))


# ---------------------------------------------------------------------
# Ejercicio 1.2. Comprobar con Hypothesis que la función potencia es
# equivalente a la predefinida (^).
# ---------------------------------------------------------------------
# @given(st.integers(), st.integers(min_value=0, max_value=100))
# def test_potecia(x: int, n: int) -> None:
# 	assert potencia(x, n) == x**n


# ---------------------------------------------------------------------
# Ejercicio 2. Dados dos números naturales, a y b, es posible calcular
# su máximo común divisor mediante el Algoritmo de Euclides. Este
# algoritmo se puede resumir en la siguiente fórmula:
# mcd(a,b) = a, si b = 0
# = mcd (b, a módulo b), si b > 0
#
# Definir la función
# mcd : (int, nt) -> int
# tal que mcd(a, b) es el máximo común divisor de a y b calculado
# mediante el algoritmo de Euclides. Por ejemplo,
# mcd(30, 45) == 15
# mcd(45, 30) == 15
#
# Comprobar con Hypothesis que el máximo común divisor de dos números a
# y b (ambos mayores que 0) es siempre mayor o igual que 1 y además es
# menor o igual que el menor de los números a y b.
# ---------------------------------------------------------------------
def mcd(a:int, b:int) -> int:
	return a if b == 0 else mcd(b, a % b)

# ic(mcd(30, 45))
# ic(mcd(45, 30))

# @given(st.integers(min_value=1), st.integers(min_value=1))
# def test_mcd(a: int, b: int) -> None:
# 	assert mcd(a, b) > 0 and mcd(a, b) <= min(a, b)


# ---------------------------------------------------------------------
# Ejercicio 3.1, Definir por recursión la función
# pertenece : (A, list[A]) -> bool
# tal que pertenece(x, ys) se verifica si x pertenece a la lista ys.
# Por ejemplo,
# pertenece(3, [2, 3, 5]) == True
# pertenece(4, [2, 3, 5]) == False
# ---------------------------------------------------------------------
def pertenece(x:int, ys: list[int]) -> bool:
	if ys:
		return x == ys[0] or pertenece(x, ys[1:])
	else:
		return False

# ic(pertenece(3, [2, 3, 5]))
# ic(pertenece(4, [2, 3, 5]))


# ---------------------------------------------------------------------
# Ejercicio 3.2. Comprobar con Hypothesis que pertenece es equivalente
# a in.
# ---------------------------------------------------------------------
# @given(st.integers(min_value=1, max_value=100), st.lists(st.integers()))
# def test_pertenece(x:int, ys:list[int]):
# 	assert pertenece(x, ys) == (x in ys)


# ---------------------------------------------------------------------
# Ejercicio 4. Definir por recursión la función
# concatenaListas :: [[a]] -> [a]
# tal que (concatenaListas xss) es la lista obtenida concatenando las
# listas de xss. Por ejemplo,
# concatenaListas([[1, 3], [5], [2, 4, 6]]) == [1, 3, 5, 2, 4, 6]
# ---------------------------------------------------------------------
def concatenaListas(xss: list[list[int]]) -> list[int]:
	if xss:
		return xss[0] + concatenaListas(xss[1:])
	return []

# ic(concatenaListas([[1, 3], [5], [2, 4, 6]]))


# ---------------------------------------------------------------------
# Ejercicio 5.1. Definir por recursión la función
# coge : (int, list[A]) -> list[A]
# tal que coge(n, xs) es la lista de los n primeros elementos de
# xs. Por ejemplo,
# coge(3, range(4, 12)) == [4, 5, 6]
# ---------------------------------------------------------------------
def coge(n: int, xs:list[int]) ->list[int]:
	if xs and n > 0:
		return [xs[0]] + coge(n - 1, xs[1:])
	return []

# ic(coge(3, range(4, 12)))


# ---------------------------------------------------------------------
# Ejercicio 5.2. Comprobar con Hypothesis que coge(n, xs) es equivalente
# a xs[:n], suponiendo que n >= 0.
# ---------------------------------------------------------------------
# @given(st.integers(min_value=1, max_value=100), st.lists(st.integers()))
# def test_coge(n: int, xs: list[int]) -> None:
# 	assert coge(n, xs) == xs[0:n]


# ---------------------------------------------------------------------
# Ejercicio 6.1. Definir, por recursión la función
# sumaDeCuadradosR : (int) -> int
# tal sumaDeCuadradosR(n) es la suma de los cuadrados de los n primeros
# números naturales. Por ejemplo,
# sumaDeCuadradosR(3) == 14
# sumaDeCuadradosR(100) == 338350
# ---------------------------------------------------------------------
def sumaDeCuadradosR(n: int) -> int:
	if n > 0:
		return n**2 + sumaDeCuadradosR(n - 1)
	return 0

# ic(sumaDeCuadradosR(3))
# ic(sumaDeCuadradosR(100))


# ---------------------------------------------------------------------
# Ejercicio 6.3. Definir, por comprensión, la función
# sumaDeCuadradosC : (int) -> int
# tal sumaDeCuadradosC(n) es la suma de los cuadrados de los n primeros
# números naturales. Por ejemplo,
# sumaDeCuadradosC(3) == 14
# sumaDeCuadradosC(100) == 338350
# ---------------------------------------------------------------------
def sumaDeCuadradosC(n: int) -> int:
	if n == 1:
		return 1
	return sum(n**2 for n in range(1, n+1))

# ic(sumaDeCuadradosC(3))
# ic(sumaDeCuadradosC(100))


# ---------------------------------------------------------------------
# Ejercicio 6.4. Comprobar con Hypothesis que las funciones
# sumaCuadradosR y sumaCuadradosC son equivalentes sobre los números
# naturales.
# ---------------------------------------------------------------------
# @given(st.integers(min_value=1, max_value=100))
# @settings(max_examples=500)
# def test_suma_de_cuadrados(n: int):
# 	assert sumaDeCuadradosR(n) == sumaDeCuadradosC(n)


# ---------------------------------------------------------------------
# Ejercicio 7.1. Definir, por recursión, la función
# digitosR : (int) -> list[int]
# tal que digitosR(n) es la lista de los dígitos del número n. Por
# ejemplo,
# digitosR(320274) == [3, 2, 0, 2, 7, 4]
# ---------------------------------------------------------------------
def digitosR(n: int) -> list[int]:
	if n < 10:
		return [n]
	return digitosR(n//10) + [n % 10]

# ic(digitosR(320274))


# ---------------------------------------------------------------------
# Ejercicio 7.2. Definir, por comprensión, la función
# digitosC : (int) -> list[int]
# tal que digitosC(n) es la lista de los dígitos del número n. Por
# ejemplo,
# digitosC(320274) == [3, 2, 0, 2, 7, 4]
# ---------------------------------------------------------------------
def digitosC(n: int) -> list[int]:
	ret = []
	while n > 0:
		ret.append(n % 10)
		n //= 10
	return list(reversed(ret))


def digitosC2(n: int) -> list[int]:
	return [int(x) for x in str(n)]

# Comprobación de tiempos
def timing(ex: str) -> int:
	t = Timer(ex, "", default_timer, globals=globals()).timeit()
	print(f"{ex}: {t} segundos")

# ic(digitosC2(320274))
# timing("digitosC(320274)")
# timing("digitosC2(320274)")


# ---------------------------------------------------------------------
# Ejercicio 7.3. Comprobar con Hypothesis que las funciones digitosR y
# digitosC son equivalentes.
# ---------------------------------------------------------------------
# @given(st.integers(min_value=1, max_value=100))
# @settings(max_examples=500)
# def test_digitos(n: int) -> None:
# 	assert digitosR(n) == digitosC(n) == digitosC2(n)


# ---------------------------------------------------------------------
# Ejercicio 8.1. Definir, por recursión, la función
# sumaDigitosR : (int) -> int
# tal que sumaDigitosR(n) es la suma de los dígitos de n. Por ejemplo,
# sumaDigitosR(3) == 3
# sumaDigitosR(2454) == 15
# sumaDigitosR(20045) == 11
# ---------------------------------------------------------------------
def sumaDigitosR(n: int) -> int:
	if n < 10:
		return n
	return n % 10 + sumaDigitosR(n // 10)

# ic(sumaDigitosR(3))
# ic(sumaDigitosR(2454))
# ic(sumaDigitosR(20045))


# ---------------------------------------------------------------------
# Ejercicio 8.2. Definir, sin usar recursión, la función
# sumaDigitosNR : (int) -> int
# tal que sumaDigitosNR(n) es la suma de los dígitos de n. Por ejemplo,
# sumaDigitosNR(3) == 3
# sumaDigitosNR(2454) == 15
# sumaDigitosNR(20045) == 11
# ---------------------------------------------------------------------
def sumaDigitosNR(n: int) -> int:
	return sum(int(x) for x in str(n))

# ic(sumaDigitosNR(3))
# ic(sumaDigitosNR(2454))
# ic(sumaDigitosNR(20045))


# ---------------------------------------------------------------------
# Ejercicio 8.3. Comprobar con Hypothesis que las funciones sumaDigitosR
# y sumaDigitosNR son equivalentes.
# ---------------------------------------------------------------------
# @given(st.integers(min_value=1, max_value=500))
# @settings(max_examples=500)
# def test_sumaDigitos(n: int) -> None:
# 	assert sumaDigitosR(n) == sumaDigitosNR(n)


# ---------------------------------------------------------------------
# Ejercicio 9.1. Definir, por recursión, la función
# listaNumeroR : (list[int]) -> int
# tal que listaNumeroR(xs) es el número formado por los dígitos xs. Por
# ejemplo,
# listaNumeroR([5]) == 5
# listaNumeroR([1, 3, 4, 7]) == 1347
# listaNumeroR([0, 0, 1]) == 1
# ---------------------------------------------------------------------
