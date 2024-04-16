from math import cos, sin, radians, sqrt

def menu():
  while True:
    print("1 - Velocidades nas direções î e j")
    print("2 - Altura máxima")
    print("3 - Tempo no ar")
    print("4 - Alcance maximo horizontal")
    print("5 - Posição x e y no instante")
    print("6 - Velocidade x e y no instante e módulo")
    print("7 - Velocidades ao atingir o chão")
    print("0- Sair\n")
    opcao = int(input("Digite a opção desejada: "))
    print()
    if opcao == 1:
      velocidades()
      print()
      print(f"Velocidade î: {v0x} m/s")
      print(f"Velocidade j: {v0y} m/s\n")
    elif opcao == 2:
      altura_max()
      print()
      print(f"Altura máxima: {h} m\n")
    elif opcao == 3:
      tempo_no_ar()
      print()
      print(f"Tempo no ar: {t_ar} s\n")
    elif opcao == 4:
      alcance_horiontal()
      print()
      print(f"Alcance horizontal: {x_max} m\n")
    elif opcao == 5:
      posicaoXYi()
      print()
      print(f"Posição x no instante: {x} m")
      print(f"Posição y no instante: {y} m\n")
    elif opcao == 6:
      velocidadesXYi()
      print()
      print(f"Velocidade x no instante: {vx} m/s")
      print(f"Velocidade y no instante: {vy} m/s")
      print(f"Módulo da velocidade: {modulo} m/s\n")
    elif opcao == 7:
      velocidadeF()
      print()
      print(f"Velocidade x final: {vx_final} m/s")
      print(f"Velocidade y final: {vy_final} m/s")
      print(f"Módulo da velocidade final: {modulo_final} m/s\n")
    elif opcao == 0:
      print("Saindo...")
      break
            
g = 9.8

def velocidades():
  global v0x, v0y
# Velocidades iniciais nas direções î e j
  v0 = float(input("Velocidade inicial: "))
  print("Deseja converter medida? (s/n) ")
  resp = input()
  if resp == "s":
    v0 = converteVel_inicial(v0)
  angulo = float(input("Ângulo de lançamento: "))
  v0x = v0 * cos(radians(angulo))
  v0y = v0 * sin(radians(angulo))

def altura_max():
  global h 
  # Altura máxima
  velocidades()
  h_inicial = float(input("Altura a partir do solo: "))
  h = (v0y ** 2 + 2 * g * (h_inicial / 100)) / (2 * g)


def tempo_no_ar():
  global t_ar
  # Tempo no ar
  altura_max()
  t_sub = v0y / g
  t_queda = sqrt(2 * h / g)
  t_ar = t_sub + t_queda

def alcance_horiontal():
  global x_max
  # Alcance máximo horizontal
  tempo_no_ar()
  x_max = v0x * t_ar

def posicaoXYi():
  global x, y, td, h_inicial
  # Posições x e y em determinado instante
  alcance_horiontal()
  td = float(input("Instante: "))
  h_inicial = float(input("Altura a partir do solo: "))
  x = v0x * td
  y = (h_inicial/100) + (v0y * td) - (g * (td**2)) / 2

def velocidadesXYi():
  global modulo, vx, vy
  # Velocidades x e y e módulo em determinado instante
  posicaoXYi()
  vx = x / td
  vy = v0y - g * td
  modulo = sqrt(vx**2 + vy**2)

def velocidadeF():
  global vx_final, vy_final, modulo_final
  # Velocidades ao atingir o chão
  velocidadesXYi()
  vx_final = v0x
  y_final = h_inicial + v0y * t_ar - (g * t_ar**2) / 2
  vy_final = 2 * (((y_final - h_inicial) / t_ar) - v0y / 2)
  modulo_final = sqrt(vx_final**2 + vy_final**2)

def converteVel_inicial(v0):
  resp = 0
  print("Selecione a unidade da velocidade inicial: ") 
  print("1 - m/s")
  print("2 - km/h")
  resp = int(input())
  if resp == 1:
    v0 = v0 * 36
  elif resp == 2:
    v0 = v0 / 36
  return v0  
  
menu()

