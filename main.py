from math import *

y0 = float(input("Posição inicial: "))
h_inicial = float(input("Altura a partir do solo: "))
v0 = float(input("Velocidade inicial: "))
angulo = float(input("Ângulo de lançamento: "))
td = float(input("Instante: "))

g = 9.8

# Velocidades iniciais nas direções î e j
v0x_rad = v0 * cos(radians(angulo))
v0y_rad = v0 * sin(radians(angulo))

v0x = v0 * v0x_rad
v0y = v0 * v0y_rad

# Altura máxima
h = (v0y ** 2 + 2 * g * h_inicial) / (2 * g)

# Tempo no ar
t_sub = v0y / g
t_queda = sqrt(2 * h / g)
t_ar = t_sub + t_queda

# Alcance máximo horizontal
x_max = v0x * t_ar

# Posições x e y em determinado instante
x = v0x * td
y = h_inicial + v0y * td - (g * td**2) / 2

# Velocidades x e y e módulo em determinado instante
vx = x / td
vy = 2 * (y - h_inicial) / td - (v0y / 2)
modulo = sqrt(vx**2 + vy**2)

# Velocidades ao atingir o chão
vx_final = v0x
y_final = h_inicial + v0y * t_ar - (g * t_ar**2) / 2
vy_final = 2 * (y_final - h_inicial) / t_ar - (v0y / 2)
modulo_final = sqrt(vx_final**2 + vy_final**2)