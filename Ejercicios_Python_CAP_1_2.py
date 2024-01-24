# ---------------------------------------------------------------------
# Introducción --
# ---------------------------------------------------------------------
# En esta relación se plantean ejercicios con definiciones de funciones
# por composición sobre números, listas y booleanos.
# ----------------------------------------------------------------------
# Cabecera
# ----------------------------------------------------------------------

from math import *
from typing import TypeVar

from hypothesis import assume, given, settings
from hypothesis import strategies as st

from icecream import ic

# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# divisionSegura : (float, float) -> float
# tal que divisionSegura(x, y) es x/y si y no es cero y 9999 en caso
# contrario. Por ejemplo,
# divisionSegura(7, 2) == 3.5
# divisionSegura(7, 0) == 9999.0
# ---------------------------------------------------------------------
def divisionSegura1 (x: float, y: float) -> float:
	return (9999 if y == 0 else x/y)

def divisionSegura2 (x: float, y: float) -> float:
	if y == 0:
		return 9999
	else:
		return x / y

def divisionSegura3 (x: float, y: float) -> float:
	match y:
		case 0:
			return (9999)
		case _:
			return (x / y)

# @given(st.floats, st.floats)
# def test_divisionSegura(x: float, y: float) -> float:
# 	assert divisionSegura1(x, y) == divisionSegura2(x, y) == divisionSegura3(
# 		x, y)
#
# # ic(divisionSegura1(7, 2))
# # ic(divisionSegura1(7, 0))


# ---------------------------------------------------------------------
# Ejercicio 2. La disyunción excluyente de dos fórmulas se verifica si
# una es verdadera y la otra es falsa. Su tabla de verdad es
# x | y | xor x y
# ------+-------+---------
# True | True | False
# True | False | True
# False | True | True
# False | False | False
#
# Definir la función
# xor : (bool, bool) -> bool
# tal que xor(x, y) es la disyunción excluyente de x e y. Por ejemplo,
# xor(True, True) == False
# xor(True, False) == True
# xor(False, True) == True
# xor(False, False) == False
# ---------------------------------------------------------------------
def xor(x: bool, y: bool) -> bool:
	if (x == True and y == True) or (x == False and y == False):
		return False
	else:
		return True

def xor1(x: bool, y: bool) -> bool:
	if (x and y) or (not x and not y):
		return False
	else:
		return True

def xor2(x: bool, y: bool) -> bool:
	return x != y

# @given(st.booleans, st.booleans)
# def test_xor(x: bool, y: bool) -> bool:
# 	assert xor(x, y) == xor1(x, y) == xor2(x, y)
#
# # ic(xor2(True, True))
# # ic(xor2(True, False))
# # ic(xor2(False, True))
# # ic(xor2(False, False))


# ---------------------------------------------------------------------
# Ejercicio 3. Las dimensiones de los rectángulos puede representarse
# por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y
# altura 3.
#
# Definir la función
# mayorRectangulo : (tuple[float, float], tuple[float, float])
# -> tuple[float, float]
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
# r1 y r2. Por ejemplo,
# mayorRectangulo((4, 6), (3, 7)) == (4, 6)
# mayorRectangulo((4, 6), (3, 8)) == (4, 6)
# mayorRectangulo((4, 6), (3, 9)) == (3, 9)
# ---------------------------------------------------------------------
def mayorRectangulo(r1: tuple[float, float], r2: tuple[float, float]) -> (
		tuple)[float, float]:
	return r1 if (r1[0] * r1[1]) >= (r2[0] * r2[1]) else r2

# ic(mayorRectangulo((4, 6), (3, 7)))
# ic(mayorRectangulo((4, 6), (3, 8)))
# ic(mayorRectangulo((4, 6), (3, 9)))


# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# intercambia : (tuple[A, B]) -> tuple[B, A]
# tal que intercambia(p) es el punto obtenido intercambiando las
# coordenadas del punto p. Por ejemplo,
# intercambia((2,5)) == (5,2)
# intercambia((5,2)) == (2,5)
#
# Comprobar con Hypothesis que la función intercambia esidempotente; es
# decir, si se aplica dos veces es lo mismo que no aplicarla ninguna.
# ---------------------------------------------------------------------
def intercambia(p: tuple) -> tuple:
	return (p[1], p[0])

# #test = ic(intercambia((2, 5)))
# @given(st.tuples(st.integers, st.integers))
# def test_Itercambia(p):
# 	assert intercambia(intercambia(p)) == p


# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# distancia : (tuple[float, float], tuple[float, float]) -> float
# tal que distancia(p1, p2) es la distancia entre los puntos p1 y
# p2. Por ejemplo,
# distancia((1, 2), (4, 6)) == 5.0
#
# Comprobar con Hypothesis que se verifica la propiedad triangular de
# la distancia; es decir, dados tres puntos p1, p2 y p3, la distancia
# de p1 a p3 es menor o igual que la suma de la distancia de p1 a p2 y
# la de p2 a p3.
# ---------------------------------------------------------------------
def distancia(p1: tuple[float, float], p2: tuple[float, float]) -> float:
	return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cota = 2**30
# @given(st.tuples(st.integers(min_value=0, max_value=cota),
#                  st.integers(min_value=0, max_value=cota)),
#        st.tuples(st.integers(min_value=0, max_value=cota),
#                  st.integers(min_value=0, max_value=cota)),
#        st.tuples(st.integers(min_value=0, max_value=cota),
#                  st.integers(min_value=0, max_value=cota)))
# def test_distancia(p1, p2, p3):
# 	assert distancia(p1, p3) <= (distancia(p1, p2) + distancia(p2, p3))
#
# Nota: Por problemas de redondeo, la propiedad no se cumple en
# general
# #ic(distancia((1, 2), (4, 6)))


# ---------------------------------------------------------------------
# Ejercicio 6. Definir una función
# ciclo : (list[A]) -> list[A]
# tal que ciclo(xs) es la lista obtenida permutando cíclicamente los
# elementos de la lista xs, pasando el último elemento al principio de
# la lista. Por ejemplo,
# ciclo([2, 5, 7, 9]) == [9, 2, 5, 7]
# ciclo([]) == []
# ciclo([2]) == [2]
#
# Comprobar que la longitud es un invariante de la función ciclo; es
# decir, la longitud de (ciclo xs) es la misma que la de xs.
# ---------------------------------------------------------------------
def ciclo(xs: list) -> list:
	if xs == []:
		return []
	return ([xs[-1]] + xs[: -1])

# # test = ic(ciclo([2, 5, 7, 9]))
# # print(type(test))
# @settings(max_examples=20)
# @given(st.lists(st.integers()))
# def test_ciclo(xs):
# 	print(xs)
# 	assert len(xs) == len(ciclo(xs))


# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# numeroMayor : (int, int) -> int
# tal que numeroMayor(x, y) es el mayor número de dos cifras que puede
# construirse con los dígitos x e y. Por ejemplo,
# numeroMayor(2, 5) == 52
# numeroMayor(5, 2) == 52
# ---------------------------------------------------------------------
def numeroMayor(x: int, y: int) -> int:
	return ((x*10) + y) if x >= y else ((y*10) + x)

def numeroMayor1(x: int, y: int) -> int:
	return (max(x, y) * 10) + (min(x, y))

# ic(numeroMayor1(2, -5))
# ic(numeroMayor1(5, 5))
# @settings(max_examples= 50)
# @given(st.integers(min_value=0), st.integers(min_value=0))
# def test_numeroMayor(x, y):
# 	print(f"x: {x} -- y: {y}")
# 	assert numeroMayor(x, y) == numeroMayor1(x, y)


# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# numeroDeRaices : (float, float, float) -> float
# tal que numeroDeRaices(a, b, c) es el número de raíces reales de la
# ecuación a*x^2 + b*x + c = 0. Por ejemplo,
# numeroDeRaices(2, 0, 3) == 0
# numeroDeRaices(4, 4, 1) == 1
# numeroDeRaices(5, 23, 12) == 2
# ---------------------------------------------------------------------
'''
La "raíz real" se refiere a las soluciones reales de una ecuación cuadrática o
polinómica. En matemáticas, la raíz de una ecuación es el valor que, cuando se
sustituye en la ecuación, hace que la ecuación sea verdadera.

Para una ecuación cuadrática de la forma \(ax^2 + bx + c = 0\), las raíces
reales se pueden encontrar utilizando la fórmula cuadrática:

[x = -b +-\sqrt{b^2 - 4ac}}/{2a}]

Donde sqrt{b^2 - 4ac} es la parte bajo el signo de la raíz cuadrada.
Si esta parte es positiva, la ecuación tiene dos raíces reales distintas.
Si es igual a cero, hay una raíz real (una raíz doble). Si es negativa,
la ecuación no tiene raíces reales.

Por ejemplo, considera la ecuación cuadrática x^2 - 4x + 4 = 0.
Al aplicar la fórmula cuadrática, obtienes x = 2 dos veces como solución.
En este caso, 2 es la raíz real doble porque la parte bajo la raíz cuadrada
es cero b^2 - 4ac = 0.

En general, la "raíz real" de una ecuación se refiere al valor real de la
variable que satisface la ecuación. Puede haber una, dos o ninguna raíz real,
dependiendo de la naturaleza de la ecuación y los coeficientes involucrados.
'''
def numeroDeRaices(a: float, b:float, c:float) -> float:
	res = b**2 - 4 * a * c
	if res > 0:
		return 2
	elif res == 0:
		return 1
	else:
		return 0

# ic(numeroDeRaices(2, 0, 3))
# ic(numeroDeRaices(4, 4, 1))
# ic(numeroDeRaices(5, 23, 12))


# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# raices : (float, float, float) -> list[float]
# tal que raices(a, b, c) es la lista de las raíces reales de la
# ecuación ax^2 + bx + c = 0. Por ejemplo,
# raices(1, 3, 2) == [-1.0,-2.0]
# raices(1, (-2), 1) == [1.0,1.0]
# raices(1, 0, 1) == []
#
# Comprobar con Hypothesis que la suma de las raíces de la ecuación
# ax^2 + bx + c = 0 (con a no nulo) es -b/a y su producto es c/a.
# ---------------------------------------------------------------------
def raices(a: float, b:float, c:float) -> list:
	d = b**2 - (4 * a * c)
	if d >= 0:
		e = sqrt(d)
		t = 2 * a
		return [(-b + e) / t, (-b -e) / t]
	return []

# # ic(raices(1, 3, 2))
# # ic(raices(1, (-2), 1))
# # ic(raices(1, 0, 1))

# Para comprobar la propiedad se usará la función
# casiIguales : (float, float) -> bool
# tal que casiIguales(x, y) se verifica si x e y son casi iguales; es
# decir si el valor absoluto de su diferencia es menor que una
# milésima. Por ejemplo,
# casiIguales(12.3457, 12.3459) == True
# casiIguales(12.3457, 12.3479) == False
def casiIguales(x:float, y:float) -> bool:
	return abs(x - y) < 0.001

# # ic(casiIguales(12.3457, 12.3459))
# # ic(casiIguales(12.3457, 12.3479))
# @settings(max_examples=100)
# @given(st.floats(min_value=-100, max_value=100),
#        st.floats(min_value=-100, max_value=100),
#        st.floats(min_value=-100, max_value=100))
# def test_raices(a, b, c):
# 	assume(abs(a) > 0.1)
# 	xs = raices(a, b, c)
# 	assume(xs)
# 	assert casiIguales(xs[0] + xs[1], -b / a)
# 	assert casiIguales(xs[0] * xs[1], c / a)


# ---------------------------------------------------------------------
# Ejercicio 10. La fórmula de Herón, descubierta por Herón de
# Alejandría, dice que el área de un triángulo cuyo lados miden a, b y c
# es la raíz cuadrada de s(s-a)(s-b)(s-c) donde s es el semiperímetro
# s = (a+b+c)/2
#
# Definir la función
# area : (float, float, float) -> float
# tal que area(a, b, c) es el área del triángulo de lados a, b y c. Por
# ejemplo,
# area(3, 4, 5) == 6.0
# ---------------------------------------------------------------------
def area(a: float, b:float, c: float) -> float:
	s = (a + b + c) / 2
	return sqrt(s*(s-a)*(s-b)*(s-c))

# ic(area(3, 4, 5))


# ---------------------------------------------------------------------
# Ejercicio 11. Los intervalos cerrados se pueden representar mediante
# una lista de dos números (el primero es el extremo inferior del
# intervalo y el segundo el superior).
#
# Definir la función
# interseccion : (list[float], list[float]) -> list[float]
# tal que interseccion(i1, i2) es la intersección de los intervalos i1 e
# i2. Por ejemplo,
# interseccion([], [3, 5]) == []
# interseccion([3, 5], []) == []
# interseccion([2, 4], [6, 9]) == []
# interseccion([2, 6], [6, 9]) == [6, 6]
# interseccion([2, 6], [0, 9]) == [2, 6]
# interseccion([2, 6], [0, 4]) == [2, 4]
# interseccion([4, 6], [0, 4]) == [4, 4]
# interseccion([5, 6], [0, 4]) == []
#
# Comprobar con Hypothesis que la intersección de intervalos es
# conmutativa.
# ---------------------------------------------------------------------
def interseccion(i1: list[float], i2: list[float]) -> list[float]:
	if i1 == [] or i2 == []:
		return []
	[x1, y1] = i1
	[x2, y2] = i2
	x = max(x1, x2)
	y = min(y1, y2)
	if x <= y:
		return [x, y]
	return []

# # ic(interseccion([], [3, 5]))
# # ic(interseccion([3, 5], []))
# # ic(interseccion([2, 4], [6, 9]))
# # ic(interseccion([2, 6], [6, 9]))
# # ic(interseccion([2, 6], [0, 9]))
# # ic(interseccion([2, 6], [0, 4]))
# # ic(interseccion([4, 6], [0, 4]))
# # ic(interseccion([5, 6], [0, 4]))
# @given(st.floats(), st.floats(),st.floats(), st.floats())
# def test_interseccion(i1, i2, i3, i4):
# 	assume(i1 <= i2 and i3 <= i4)
# 	assert (interseccion([i1, i2], [i3, i4])
# 	        == interseccion([i3, i4], [i1, i2]))


# ---------------------------------------------------------------------
# Ejercicio 12.1. Los números racionales pueden representarse mediante
# pares de números enteros. Por ejemplo, el número 2/5 puede
# representarse mediante el par (2,5).
#
# El tipo de los racionales se define por
# Racional = tuple[int, int]
#
# Definir la función
# formaReducida : (Racional) -> Racional
# tal que formaReducida(x) es la forma reducida del número racional
# x. Por ejemplo,
# formaReducida((4, 10)) == (2, 5)
# formaReducida((0, 5)) == (0, 1)
# La forma reducida se obtiene de la division de cada par entre el máximo comun
# divisor de los mismos
# ---------------------------------------------------------------------
def formaReducida(x: tuple[int, int]) -> tuple[int, int]:
	[x1, x2] = x
	mcd = gcd(x1, x2)
	return (x1 // mcd, x2 // mcd)

# ic(formaReducida((4, 10)))
# ic(formaReducida((0, 5)))


# ---------------------------------------------------------------------
# Ejercicio 12.2. Definir la función
# sumaRacional : (Racional, Racional) -> Racional
# tal que sumaRacional(x, y) es la suma de los números racionales x e y,
# expresada en forma reducida. Por ejemplo,
# sumaRacional((2, 3), (5, 6)) == (3, 2)
# sumaRacional((3, 5), (-3, 5)) == (0, 1)
# ---------------------------------------------------------------------
def sumaRacional(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
	[a, b] = x
	[c, d] = y
	return formaReducida((a*d + b*c, b*d))

# ic(sumaRacional((2, 3), (5, 6)))
# ic(sumaRacional((3, 5), (-3, 5)))


# ---------------------------------------------------------------------
# Ejercicio 12.3. Definir la función
# productoRacional : (Racional, Racional) -> Racional
# tal que productoRacional(x, y) es el producto de los números
# racionales x e y, expresada en forma reducida. Por ejemplo,
# productoRacional((2, 3), (5, 6)) == (5, 9)
# ---------------------------------------------------------------------
def productoRacional(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
	[a, b] = x
	[c, d] = y
	return formaReducida((a*c, b*d))

# ic(productoRacional((2, 3), (5, 6)))


# ---------------------------------------------------------------------
# Ejercicio 12.4. Definir la función
# igualdadRacional : (Racional, Racional) -> bool
# tal que igualdadRacional(x, y) se verifica si los números racionales x
# e y son iguales. Por ejemplo,
# igualdadRacional((6, 9), (10, 15)) == True
# igualdadRacional((6, 9), (11, 15)) == False
# igualdadRacional((0, 2), (0, -5)) == True
# ---------------------------------------------------------------------
def igualdadRacional(x: tuple[int, int], y: tuple[int, int]) -> bool:
	[a, b] = x
	[c, d] = y
	return a*d == b*c

# ic(igualdadRacional((6, 9), (10, 15)))
# ic(igualdadRacional((6, 9), (11, 15)))
# ic(igualdadRacional((0, 2), (0, -5)))