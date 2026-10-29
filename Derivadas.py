import sympy as sp

x = sp.symbols('x')

#Ejercicio 1
f = x**5

f_derivada = sp.diff(f, x)

print("Ejercicio 1:")
print("Función f(x):", f)
print("Derivada f'(x):", f_derivada)
print("-" * 30) #Guiones para separar ejercicios

#Ejercicio 2
g = 4 * x**3

g_derivada = sp.diff(g, x)

print("Ejercicio 2:")
print("Función g(x):", g)
print("Derivada g'(x):", g_derivada)
print("-" * 30)

#Ejercicio 3
h = 2*x**4 - 6*x**2 + 7*x - 9

h_derivada = sp.diff(h, x)

print("Ejercicio 3:")
print("Función h(x):", h)
print("Derivada h'(x):", h_derivada)