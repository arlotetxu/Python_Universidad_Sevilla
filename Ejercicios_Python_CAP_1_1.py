from math import pi
from typing import TypeVar
# Con la libreria icecream se hacen comprobaciones del codigo que aportan mas
# informacion que haciendolas con la funcion print.
from icecream import ic
# La libreria hypothesys genera test a funciones mediante el uso de decoradores
from hypothesis import given
from hypothesis import strategies as st


A = TypeVar('A')

# ---------------------------------------------------------------------
# Ejercicio 1. Definir la función
# media3 : (float, float, float) -> float
# tal que (media3 x y z) es la media aritmética de los números x, y y
# z. Por ejemplo,
# media3(1, 3, 8) == 4.0
# media3(-1, 0, 7) == 2.0
# media3(-3, 0, 3) == 0.0
# ---------------------------------------------------------------------
def media3 (a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


# ---------------------------------------------------------------------
# Ejercicio 2. Definir la función
# sumaMonedas : (int, int, int, int, int) -> int
# tal que sumaMonedas(a, b, c, d, e) es la suma de los euros
# correspondientes a a monedas de 1 euro, b de 2 euros, c de 5 euros, d
# 10 euros y e de 20 euros. Por ejemplo,
# sumaMonedas(0, 0, 0, 0, 1) == 20
# sumaMonedas(0, 0, 8, 0, 3) == 100
# sumaMonedas(1, 1, 1, 1, 1) == 38
# ---------------------------------------------------------------------
def sumaMonedas(a: int, b: int, c: int, d: int, e: int) -> int:
    return ((a) + (b * 2) + (c * 5) + (d * 10) + (e * 20))

'''
#Probando decorador
@given(st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=0), st.integers(min_value=0))
def test_sumaMonedas(a: int, b: int, c: int, d: int, e: int):
    resultado = sumaMonedas(a, b, c, d, e)
    assert resultado >= 0

test_sumaMonedas()
'''

# ---------------------------------------------------------------------
# Ejercicio 3. Definir la función
# volumenEsfera : (float) -> float
# tal que volumenEsfera(r) es el volumen de la esfera de radio r. Por
# ejemplo,
# volumenEsfera(10) == 4188.790204786391
# ---------------------------------------------------------------------
def volumenEsfera(r: float) -> float:
    return ((4/3) * pi * r**3)

'''
#Probando decorador
@given(st.floats(min_value=1, max_value=10))
def test_volumenEsfera(r: float):
    resultado = volumenEsfera(r)
    assert resultado >= 0

test_volumenEsfera()
'''

# ---------------------------------------------------------------------
# Ejercicio 4. Definir la función
# areaDeCoronaCircular : (float, float) -> float
# tal que areaDeCoronaCircular(r1, r2) es el área de una corona
# circular de radio interior r1 y radio exterior r2. Por ejemplo,
# areaDeCoronaCircular(1, 2) == 9.42477796076938
# areaDeCoronaCircular(2, 5) == 65.97344572538566
# areaDeCoronaCircular(3, 5) == 50.26548245743669
# ---------------------------------------------------------------------
def areaDeCoronaCircular(r1: float, r2: float) -> float:
    return (pi * (r2**2 - r1**2))


# ---------------------------------------------------------------------
# Ejercicio 5. Definir la función
# ultimoDigito : (int) -> int
# tal que ultimoDigito(x) es el último dígito del número x. Por
# ejemplo,
# ultimoDigito(325) == 5
# ---------------------------------------------------------------------
def ultimoDigito(n: int) -> int:
    return (n % 10)

'''
#probando decoradores
@given(st.integers())
def	test_ultimoDigito(n: int):
    res = ultimoDigito(n)
    assert res == n % 10

test_ultimoDigito()
'''


# ---------------------------------------------------------------------
# Ejercicio 6. Definir la función
# maxTres : (int, int, int) -> int
# tal que maxTres(x, y, z) es el máximo de x, y y z. Por ejemplo,
# maxTres(6, 2, 4) == 6
# maxTres(6, 7, 4) == 7
# maxTres(6, 7, 9) == 9
# ---------------------------------------------------------------------
def	maxTres(x: int, y: int, z: int) -> int:
    return max(x, y , z)

'''
@given(st.integers(), st.integers(), st.integers())
def	test_maxTres(x: int, y: int, z: int):
    res = maxTres(x, y, z)
    assert res == max(x, y, z)
    
test_maxTres()
'''


# ---------------------------------------------------------------------
# Ejercicio 7. Definir la función
# rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista. Por ejemplo,
# rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
# rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
# ---------------------------------------------------------------------
def	rota1a(xs: list) -> list:
    if xs == []:
        return []
    popped = xs.pop(xs[0])
    return (xs.append(popped))

def	rota1b(xs: list) -> list:
    if xs == []:
        return []
    return (xs[1:] + [xs[0]])

def	rota1c(xs: list) -> list:
    if xs == []:
        return []
    xy = xs[1:]
    xy.append(xs[0])
    return xy

def	rota1d(xs: list) -> list:
    if xs == []:
        return []
    y, *ys = xs
    return (ys + [y])

'''
@given(st.lists(st.integers(), max_size=10))
def	test_rota1(xs: list):
    assert rota1b(xs) == rota1c(xs) == rota1d(xs)

test_rota1()
'''


# ---------------------------------------------------------------------
# Ejercicio 8. Definir la función
# rota : (int, List[A]) -> List[A]
# tal que rota(n, xs) es la lista obtenida poniendo los n primeros
# elementos de xs al final de la lista. Por ejemplo,
# rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]
# rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]
# rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]
# ---------------------------------------------------------------------
def rota(n: int, xs: list) -> list:
    xy = xs[:n]
    return (xs[n:] + xy)


# ---------------------------------------------------------------------
# Ejercicio 9. Definir la función
# rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
# rango([3, 2, 7, 5]) == [2, 7]
# ---------------------------------------------------------------------
def rango(xs: list) -> list:
    return ([min(xs), max(xs)])


# ---------------------------------------------------------------------
# Ejercicio 10. Definir la función
# palindromo : (List[A]) -> bool
# tal que palindromo(xs) se verifica si xs es un palíndromo; es decir,
# es lo mismo leer xs de izquierda a derecha que de derecha a
# izquierda. Por ejemplo,
# palindromo([3, 2, 5, 2, 3]) == True
# palindromo([3, 2, 5, 6, 2, 3]) == False
# ---------------------------------------------------------------------
def palindromo(xs: list) -> bool:
    if xs[::-1] == xs:
        return True
    else:
        return False


# ---------------------------------------------------------------------
# Ejercicio 11. Definir la función
# interior : (list[A]) -> list[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
# interior([2, 5, 3, 7, 3]) == [5, 3, 7]
# ---------------------------------------------------------------------
def	interior(xs: list) -> list:
    return xs[1:-1]

# print((interior([0, 1, 2, 3, 4, 5])))
# ic(interior([0, 1, 2, 3, 4, 5]))


# ---------------------------------------------------------------------
# Ejercicio 12. Definir la función
# finales : (int, list[A]) -> list[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
# finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
# ---------------------------------------------------------------------
def    finales(n: int, xs: list) -> list:
    if n >= len(xs):
        return xs
    return xs[len(xs) - n : ]

# ic(finales(5, [0, 2, 4, 6, 8, 10, 12, 14, 16]))


# ---------------------------------------------------------------------
# Ejercicio 13. Definir la función
# segmento : (int, int, list[A]) -> list[A]
# tal que segmento(m, n, xs) es la lista de los elementos de xs
# comprendidos entre las posiciones m y n. Por ejemplo,
# segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
# segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
# segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
# ---------------------------------------------------------------------
def segmento (m: int, n: int, xs: list) -> list:
	return xs[m - 1 : n]

# ic(segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]))
# ic(segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]))
# ic(segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]))


# ---------------------------------------------------------------------
# Ejercicio 14. Definir la función
# extremos : (int, list[A]) -> list[A]
# tal que extremos(n, xs) es la lista formada por los n primeros
# elementos de xs y los n finales elementos de xs. Por ejemplo,
# extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]
# ---------------------------------------------------------------------
def extremos(n: int, xs: list) -> list:
	return (xs[0 : n] + xs[-n: ])

# ic(extremos(2, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]))


# ---------------------------------------------------------------------
# Ejercicio 15. Definir la función
# mediano : (int, int, int) -> int
# tal que mediano(x, y, z) es el número mediano de los tres números x, y
# y z. Por ejemplo,
# mediano(3, 2, 5) == 3
# mediano(2, 4, 5) == 4
# mediano(2, 6, 5) == 5
# mediano(2, 6, 6) == 6
# ---------------------------------------------------------------------
def mediano(x: int, y: int, z: int) -> int:
	return (x + y + z - max([x, y, z]) - min ([x, y, z]))

# ic(mediano(3, 2, 5))
# ic(mediano(2, 4, 5))
# ic(mediano(2, 6, 5))
# ic(mediano(2, 6, 6))


# ---------------------------------------------------------------------
# Ejercicio 16. Definir la función
# tresIguales : (int, int, int) -> bool
# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
# tresIguales(4, 4, 4) == True
# tresIguales(4, 3, 4) == False
# ---------------------------------------------------------------------
def tresIguales(x: int, y: int, z: int) -> bool:
    if x == y == z:
        return True
    else:
        return False

# ic(tresIguales(4, 4, 4))
# ic(tresIguales(4, 3, 4))


# ---------------------------------------------------------------------
# Ejercicio 17. Definir la función
# tresDiferentes : (int, int, int) -> bool
# tal que tresDiferentes(x, y, z) se verifica si los elementos x, y y z
# son distintos. Por ejemplo,
# tresDiferentes(3, 5, 2) == True
# tresDiferentes(3, 5, 3) == False
# ---------------------------------------------------------------------
def tresDiferentes (x: int, y: int, z: int) -> bool:
    if x != y and x != z and y != z:
        return True
    else:
        return False

# ic(tresDiferentes(3, 5, 2))
# ic(tresDiferentes(3, 5, 3))
# ic(tresDiferentes(3, 5, 5))


# ---------------------------------------------------------------------
# Ejercicio 18. Definir la función
# cuatroIguales : (int, int, int, int) -> bool
# tal que cuatroIguales(x,y,z,u) se verifica si los elementos x, y, z y
# u son iguales. Por ejemplo,
# cuatroIguales(5, 5, 5, 5) == True
# cuatroIguales(5, 5, 4, 5) == False
# ---------------------------------------------------------------------
def cuatroIguales(x: int, y: int, z: int, u: int) -> bool:
    return x == y == z == u

# ic(cuatroIguales(5, 5, 5, 5))
# ic(cuatroIguales(5, 5, 4, 5))
