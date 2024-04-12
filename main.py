from math import cos, sin, radians, sqrt

def menu():
  global y0, h_inicial, v0, angulo, td

  while True:
    print("1 - Velocidades iniciais nas direções î e j")
    print("2 - Altura máxima")
    print("3 - Tempo no ar")
    print("4 - Alcance máximo horizontal")
    print("5 - Posições x e y em determinado instante")
    print("6 - Velocidades x e y e módulo em determinado instante")
    print("7 - Velocidades ao atingir o chão")
    print("0 - Sair\n")
    
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
      velocidadesîj()
      print(" ")
      print(f"Velocidade inicial em î: {v0x} m/s")
      print(f"Velocidade inicial em j: {v0y} m/s\n")
    elif opcao == 2:
      altura_max()
      print(" ")
      print(f"Altura máxima: {h} m\n")
    elif opcao == 3:
      tempo_subida()
      print(" ")
      print(f"Tempo no ar: {t_ar} s\n")
    elif opcao == 4:
      alcanceMax_h()
      print("")
      print(f"Alcance máximo horizontal: {x_max} m\n")
    elif opcao == 5:
      posicaoXYi()
      print("")
      print(f"Posição x em determinado instante: {x} m")
      print(f"Posição y em determinado instante: {y} m\n")
    elif opcao == 6:
      velocidadeXYi()
      print("")
      print(f"Velocidade x em determinado instante: {vx} m/s")
      print(f"Velocidade y em determinado instante: {vy} m/s")
      print(f"Módulo da velocidade em determinado instante: {modulo} m/s\n")
    elif opcao == 7:
      velocidadeXYf()
      print("")
      print(f"Velocidade x final: {vx_final} m/s")
      print(f"Velocidade y final: {vy_final} m/s")
      print(f"Módulo da velocidade final: {modulo_final} m/s\n")
    elif opcao == 0:
      print("Saindo...")
      break
    else:
      print("Opção invalida")
    
g = 9.8

def velocidadesîj():
  global v0y, v0x
  print(" ")
  v0 = float(input("Velocidade inicial: "))
  angulo = float(input("Ângulo de lançamento: "))
  # Velocidades iniciais nas direções î e j
  v0x_rad = v0 * cos(radians(angulo))
  v0y_rad = v0 * sin(radians(angulo))

  v0x = v0 * v0x_rad
  v0y = v0 * v0y_rad

  return v0y, v0x
def altura_max():
  global h
  velocidadesîj()
  h_inicial = float(input("Altura a partir do solo: "))
  # Altura máxima
  h = (v0y ** 2 + 2 * g * h_inicial) / (2 * g)

  return h
def tempo_subida():
  global t_sub, t_queda, t_ar
  altura_max()
  # Tempo no ar
  t_sub = v0y / g
  t_queda = sqrt(2 * h / g)
  t_ar = t_sub + t_queda

  return t_ar
def alcanceMax_h():
  global x_max
  tempo_subida()
  # Alcance máximo horizontal
  x_max = v0x * t_ar

  return x_max
def posicaoXYi(): 
  global x, y, td, h_inicial
  alcanceMax_h()
  td = float(input("Instante: "))
  h_inicial = float(input("Altura a partir do solo: "))
  # Posições x e y em determinado instante
  x = v0x * td
  y = h_inicial + v0y * td - (g * td**2) / 2

  return x, y
def velocidadeXYi():
  global vx, vy, modulo
  posicaoXYi()
  # Velocidades x e y e módulo em determinado instante
  vx = x / td
  vy = 2 * (y - h_inicial) / td - (v0y / 2)
  modulo = sqrt(vx**2 + vy**2)

def velocidadeXYf():
  global vx_final, y_final, vy_final, modulo_final
  velocidadeXYi()
  # Velocidades ao atingir o chão
  vx_final = v0x
  y_final = h_inicial + v0y * t_ar - (g * t_ar**2) / 2
  vy_final = 2 * (y_final - h_inicial) / t_ar - (v0y / 2)
  modulo_final = sqrt(vx_final**2 + vy_final**2)

menu()