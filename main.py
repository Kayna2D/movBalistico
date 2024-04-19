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
    v0 = converteVelInicial(v0)
  angulo = float(input("Ângulo de lançamento: "))
  v0x = v0 * cos(radians(angulo))
  v0y = v0 * sin(radians(angulo))

def altura_max():
  global h 
  # Altura máxima
  velocidades()
  h_inicial = float(input("Altura a partir do solo: "))
  print("Deseja converter medida? (s/n) ")
  resp = input()
  if resp == "s":
    h_inicial = converteH(h_inicial)

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

def converteVelInicial(v0):
  entrada = 0
  saida = 0
  print("Medidas de velocidade:") 
  print("1 - m/s")
  print("2 - km/h")
  print("3 - cm/s")
  entrada = int(input("Digite a opção de entrada: "))
  saida = int(input("Digite a opção de saida: "))
  if entrada == 1:
    if saida == 2:
      v0 = v0 * 3.6
    elif saida == 3:
      v0 = v0 * 100
  elif entrada == 2:
    if saida == 1:
      v0 = v0 / 3.6
    elif saida == 3:
      v0 = v0 * 27.778
  elif entrada == 3:
    if saida == 1:
      v0 = v0 / 100
    elif saida == 2:
      v0 = v0 / 27.778
  return v0  

def converteH(h):
  entrada = 0
  saida = 0
  print("Medidas de comprimento:") 
  print("1 - m")
  print("2 - km")
  print("3 - cm")
  entrada = int(input("Digite a opção de entrada: "))
  saida = int(input("Digite a opção de saida: "))
  if entrada == 1:
    if saida == 2:
      h = h / 1000
    elif saida == 3:
      h = h * 100
  elif entrada == 2:
    if saida == 1:
      h = h * 1000
    elif saida == 3:
      h = h * 100000
  elif entrada == 3:
    if saida == 1:
      h = h / 100
    elif saida == 2:
      h = h / 100000
  return h  


print("Gostaria de usar todas as funcoes ou uma especifica?")
opcao = input(str("Digite 't' para todas ou 'e' para uma especifica: "))
if opcao == "e":
  menu()
else:
  g = 9.8
  v0 = float(input("Velocidade inicial: "))
  print("Deseja converter medida? (s/n) ")
  resp = input()
  if resp == "s":
    v0 = converteVelInicial(v0)
  angulo = float(input("Ângulo de lançamento: "))
  td = float(input("Instante: "))
  h_inicial = float(input("Altura a partir do solo: "))
  print("Deseja converter medida? (s/n) ")
  resp = input()
  if resp == "s":
    h_inicial = converteH(h_inicial)
  
  # Velocidades iniciais nas direções î e j
  v0x = v0 * cos(radians(angulo))
  v0y = v0 * sin(radians(angulo))
  
  # Altura máxima
  h = (v0y ** 2 + 2 * g * (h_inicial)) / (2 * g)
  
  # Tempo no ar
  t_sub = v0y / g
  t_queda = sqrt(2 * h / g)
  t_ar = t_sub + t_queda
  
  # Alcance máximo horizontal
  x_max = v0x * t_ar
  
  # Posições x e y em determinado instante
  x = v0x * td
  y = (h_inicial) + (v0y * td) - (g * (td**2)) / 2
  
  # Velocidades x e y e módulo em determinado instante
  vx = x / td
  vy = v0y - g * td
  modulo = sqrt(vx**2 + vy**2)
  
  # Velocidades ao atingir o chão
  vx_final = v0x
  y_final = h_inicial + v0y * t_ar - (g * t_ar**2) / 2
  vy_final = 2 * (((y_final - h_inicial) / t_ar) - v0y / 2)
  modulo_final = sqrt(vx_final**2 + vy_final**2)
  
  print()
  
  print("----------------------------------")
  print()
  print("Dados:")
  print("Velocidade î: ", v0x)
  print("Velocidade j: ", v0y)
  print("Altura máxima: ", h)
  print("Tempo no ar: ", t_ar)
  print("Alcance horizontal: ", x_max)
  print("Posição x no instante: ", x)
  print("Posição y no instante: ", y)
  print("Velocidade x no instante: ", vx)
  print("Velocidade y no instante: ", vy)
  print("Módulo da velocidade no instante: ", modulo)
  print("Velocidade x final: ", vx_final)
  print("Velocidade y final: ", vy_final)
  print("Módulo da velocidade final: ", modulo_final)
  print("Velocidade x na altura máxima: ", vx)
  print("Velocidade y na altura máxima: 0")
  print("Módulo da velocidade na altura máxima: ", vx)