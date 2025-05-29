from sympy import symbols, cos, sin, nsolve
from mpmath import radians
# Recibe v0, u, cte, c
# Calcula a, b, t 
v0 = float(input("Velocidad inicial de la patada (ms^-1) [0 < v0]? \n\t>>> "))
u = float(input("Velocidad del viento (ms^-1) [u < 0]? \n\t>>> "))
cte = float(input("Constante de arrastre del viento? [0 < 1]? \n\t>>> "))
c = float(input("Ángulo de dirección de viento [0-360]?\n\t>>> "))
a, b, t = symbols('a b t', real = True)
eq_x = - 22.5 + v0 * cos(radians(a)) * sin(radians(b)) * t + cte * u * t * sin(radians(c))
eq_y = - 0 + v0 * cos(radians(a)) * cos(radians(b)) * t + cte * u * t * cos(radians(c))
eq_z = - 5.97 + v0 * sin(radians(a)) * t - 0.5 * 9.81 * t ** 2
solution = nsolve((eq_x, eq_y, eq_z), (a, b, t), (1,1,1))
a_res, b_res, t_res = solution

if a_res > 360: 
    a_res = a_res % 360
if b_res > 360: 
    b_res = b_res % 360
print("\nEl ángulo de disparo a = %s°. \nEl ángulo de compensación lateral b = %s°." %(a_res, b_res))
print("El tiempo de la trayectoria es de %s segundos." %(t_res))