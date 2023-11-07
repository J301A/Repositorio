#codigo creado por Jesus Estrada
import pygame # <- Nos ayudará a crear una interfaz gráfica
import time
import random

#MEJORAS EN "ESPERA" (O TALVEZ NUNCA)
# 1.- Sistema de "volver a jugar" una vez que acaba la partida
# 2.- Sistema de "dificultades" para el modo Jugador VS IA

#Inicializamos pygame
pygame.init()

#Variables para tamaño de pantalla
alto = 501
largo = 501
screen = pygame.display.set_mode((alto, largo))
backgroud_color = 52,52,52
screen.fill(backgroud_color)
celdas_x = 3
celdas_y = 3
celda_altura = alto/celdas_y
celda_anchura = largo/celdas_x

#Creamos una variable de control
running_menu = True
running_game = False
running_gameIA = False
turnos = 0
cuadrantes = [0,0,0,
              0,0,0,
              0,0,0]

#Imprimir el menu de inicio
def Menu_Inicio():
  base = (222,222,222)
  pygame.draw.line(screen, base, (0,375), (501,375), 1)
  pygame.draw.line(screen, base, (250,375), (250,501), 1)
  # (25 inicio + 75 letras + 25 final)x3 verticalmente
  # (113 incio) + (75 letras)x3 + (25 espaciado)x2 + (113 final) horizontalmente
  #TIC
  #T
  T1 = [(113,25),(188,25),(188,40),(158,40),(158,100),(143,100),(143,40),(113,40)]
  pygame.draw.polygon(screen, base, T1)
  #I
  I = [(213,25),(288,25),(288,40),(258,40),(258,85),(288,85),(288,100),(213,100),(213,85),(243,85),(243,40),(213,40)]
  pygame.draw.polygon(screen, base, I)
  #C
  pygame.draw.circle(screen, base, (359,62), 37.5, 15, False, True, True, False)
  C1 = [(359,25),(379,25),(379,39),(359,39)]
  C2 = [(359,99),(379,99),(379,85),(359,85)]
  pygame.draw.polygon(screen, base, C1)
  pygame.draw.polygon(screen, base, C2)
  #TAC
  #T
  T2 = [(113,150),(188,150),(188,165),(158,165),(158,225),(143,225),(143,165),(113,165)]
  pygame.draw.polygon(screen, base, T2)
  #A
  A1 = [(213,225),(228,150),(273,150),(288,225),(273,225),(258,165),(243,165),(228,225)]
  A2 = [(228,195),(273,195),(273,180),(228,180)]
  pygame.draw.polygon(screen, base, A1)
  pygame.draw.polygon(screen, base, A2)
  #C
  pygame.draw.circle(screen, base, (359,187), 37.5, 15, False, True, True, False)
  C3 = [(359,150),(379,150),(379,164),(359,164)]
  C4 = [(359,224),(379,224),(379,210),(359,210)]
  pygame.draw.polygon(screen, base, C3)
  pygame.draw.polygon(screen, base, C4)
  #TOE
  #T
  T3 = [(113,275),(188,275),(188,290),(158,290),(158,350),(143,350),(143,290),(113,290)]
  pygame.draw.polygon(screen, base, T3)
  #O
  pygame.draw.circle(screen, base, (250,312), 37.5, 15)
  #E
  E = [(322,275),(379,275),(379,290),(337,290),(337,305),(379,305),
       (379,320),(337,320),(337,335),(379,335),(379,350),(322,350)]
  pygame.draw.polygon(screen, base, E)
  #DIBUJO DE LOS MODOS DE JUEGO
  #1P -> (inicio 50) + (letras 75)x2 + (fin 50) = horizontalmente /// (inicio 25) + (letras 75) + (fin 26) = verticalmente
  #1
  N1 = [(95,475),(110,475),(110,400),(95,400),(80,415),(80,430),(95,415),(95,460)]
  pygame.draw.polygon(screen, base, N1)
  #P
  P1 = [(125,475),(140,475),(140,444),(155,444),(155,430),(140,430),(140,414),(155,414),(155,400),(125,400)]
  pygame.draw.polygon(screen, base, P1)
  pygame.draw.circle(screen, base, (155,422), 22.5, 15, True, False, False, True)
  #2P -> (inicio 50) + (letras 75)x2 + (fin 50) = horizontalmente /// (inicio 25) + (letras 75) + (fin 26) = verticalmente
  #2
  N2 = [(315,475),(360,475),(360,460),(330,460),(360,423),(345,423),(315,460)]
  pygame.draw.polygon(screen, base, N2)
  pygame.draw.circle(screen, base, (338,423), 23, 15, True, True, False, False)
  #P
  P2 = [(375,475),(390,475),(390,444),(405,444),(405,430),(390,430),(390,414),(405,414),(405,400),(375,400)]
  pygame.draw.polygon(screen, base, P2)
  pygame.draw.circle(screen, base, (405,422), 22.5, 15, True, False, False, True)
  return

#Función la cual averigua el modo de juego al hacer click
def Quien_Juega(ubicacion):
  modo_de_juego = 0
  if ubicacion[0] < 251 and ubicacion[1] > 375:
    modo_de_juego = 1
  elif ubicacion[0] > 250 and ubicacion[1] > 375:
    modo_de_juego = 2
  return modo_de_juego

#Imprimir el tablero del tic tac toe
def Imprimir_Tablero():
  for x in range (0, celdas_x):
    for y in range (0, celdas_y):
      poly = [(x*celda_anchura      , y*celda_altura),
              ((x+1)*celda_anchura  , y*celda_altura),
              ((x+1)*celda_anchura  , (y+1)*celda_altura),
              (x*celda_anchura      , (y+1)*celda_anchura)]
      pygame.draw.polygon(screen, (222,222,222), poly, 1)
  return

#Función la cual averigua el cuadrante actual al hacer click
def Donde_estoy (ubicacion):
  # [x,y,z] -> x,y siendo las cordenadas y z siendo el numero del cuadrante
  cuadrante_actual = 0
  if ubicacion[0] > 333 and ubicacion[1] > 333:
    cuadrante_actual = [2,2,9]
  elif ubicacion[0] > 167 and ubicacion[1] > 333:
    cuadrante_actual = [1,2,8]
  elif ubicacion[0] > 0 and ubicacion[1] > 333:
    cuadrante_actual = [0,2,7]
  elif ubicacion[0] > 333 and ubicacion[1] > 167:
    cuadrante_actual = [2,1,6]
  elif ubicacion[0] > 167 and ubicacion[1] > 167:
    cuadrante_actual = [1,1,5]
  elif ubicacion[0] > 0 and ubicacion[1] > 167:
    cuadrante_actual = [0,1,4]
  elif ubicacion[0] > 333 and ubicacion[1] > 0:
    cuadrante_actual = [2,0,3]
  elif ubicacion[0] > 167 and ubicacion[1] > 0:
    cuadrante_actual = [1,0,2]
  elif ubicacion[0] > 0 and ubicacion[1] > 0:
    cuadrante_actual = [0,0,1]
  return cuadrante_actual

#Funcion la cual dibuja el simbolo para el Tic Tac Toe
def Dibujar_X (cuadrante_actual):
  x = cuadrante_actual[0]
  y = cuadrante_actual[1]
  pygame.draw.line(screen, (222,222,222), ((x*167)+42,(y*167)+42), ((x*167)+126,(y*167)+126), 1)
  pygame.draw.line(screen, (222,222,222), ((x*167)+126,(y*167)+42), ((x*167)+42,(y*167)+126), 1)
  pygame.display.flip()
  return

def Dibujar_O (cuadrante_actual):
  x = cuadrante_actual[0]
  y = cuadrante_actual[1]
  pygame.draw.circle(screen, (222,222,222), ((x*167)+84,(y*167)+84), 42, 1)
  pygame.display.flip()
  return

#Funcion la cual maneja el juego
def Juego ():
  cuadrante_actual = Donde_estoy(ubicacion_juego)
  control = 0
  if cuadrantes[cuadrante_actual[2]-1] == 0:
    if turnos % 2 == 0:
      Dibujar_X(cuadrante_actual)
      cuadrantes[cuadrante_actual[2]-1] = 1
      control = 1
    else:
      Dibujar_O(cuadrante_actual)
      cuadrantes[cuadrante_actual[2]-1] = 2
      control = 2
  return control

def JuegoIA ():
  cuadrante_actual = Donde_estoy(ubicacion_juego)
  control = 0
  if cuadrantes[cuadrante_actual[2]-1] == 0:
    Dibujar_X(cuadrante_actual)
    cuadrantes[cuadrante_actual[2]-1] = 1
    control = 1
  return control

def TurnoIA ():
  control = 0
  if turnos<1:
    valor = random.randint(0,8)
    while cuadrantes[valor] != 0:
      valor = random.randint(0,8)
    coordenadas = [int(valor%3),int(valor/3)]
    Dibujar_O(coordenadas)
    cuadrantes[valor] = 2
    control = 1
  else:
    if (cuadrantes[0] == 1 and cuadrantes[4] == 1) and cuadrantes[8] != 2:
      cuadrante_actual = [2,2]
      Dibujar_O(cuadrante_actual)
      cuadrantes[8] = 2
      control = 1
    elif (cuadrantes[4] == 1 and cuadrantes[8] == 1) and cuadrantes[0] != 2:
      cuadrante_actual = [0,0]
      Dibujar_O(cuadrante_actual)
      cuadrantes[0] = 2
      control = 1
    elif (cuadrantes[0] == 1 and cuadrantes[8] == 1) and cuadrantes[4] != 2:
      cuadrante_actual = [1,1]
      Dibujar_O(cuadrante_actual)
      cuadrantes[4] = 2
      control = 1
    elif (cuadrantes[2] == 1 and cuadrantes[4] == 1) and cuadrantes[6] != 2:
      cuadrante_actual = [0,2]
      Dibujar_O(cuadrante_actual)
      cuadrantes[6] = 2
      control = 1
    elif (cuadrantes[4] == 1 and cuadrantes[6] == 1) and cuadrantes[2] != 2:
      cuadrante_actual = [2,0]
      Dibujar_O(cuadrante_actual)
      cuadrantes[2] = 2
      control = 1
    elif (cuadrantes[2] == 1 and cuadrantes[6] == 1) and cuadrantes[4] != 2:
      cuadrante_actual = [1,1]
      Dibujar_O(cuadrante_actual)
      cuadrantes[4] = 2
      control = 1
    else:
      for n in range(0,3):
        if ((cuadrantes[3*n] == 1) and (cuadrantes[(3*n)+1] == 1)) and (cuadrantes[(3*n)+2] != 2):
          cuadrante_actual = [2,n]
          Dibujar_O(cuadrante_actual)
          cuadrantes[(3*n)+2] = 2
          control = 1
          break
        elif ((cuadrantes[(3*n)+1] == 1) and (cuadrantes[(3*n)+2] == 1)) and (cuadrantes[3*n] != 2):
          cuadrante_actual = [0,n]
          Dibujar_O(cuadrante_actual)
          cuadrantes[3*n] = 2
          control = 1
          break
        elif ((cuadrantes[3*n] == 1) and (cuadrantes[(3*n)+2] == 1)) and (cuadrantes[(3*n)+1] != 2):
          cuadrante_actual = [1,n]
          Dibujar_O(cuadrante_actual)
          cuadrantes[(3*n)+1] = 2
          control = 1
          break
        elif ((cuadrantes[n] == 1) and (cuadrantes[n+3] == 1)) and (cuadrantes[n+6] != 2):
          cuadrante_actual = [n,2]
          Dibujar_O(cuadrante_actual)
          cuadrantes[n+6] = 2
          control = 1
          break
        elif ((cuadrantes[n+3] == 1) and (cuadrantes[n+6] == 1)) and (cuadrantes[n] != 2):
          cuadrante_actual = [n,0]
          Dibujar_O(cuadrante_actual)
          cuadrantes[n] = 2
          control = 1
          break
        elif ((cuadrantes[n] == 1) and (cuadrantes[n+6] == 1)) and (cuadrantes[n+3] != 2):
          cuadrante_actual = [n,1]
          Dibujar_O(cuadrante_actual)
          cuadrantes[n+3] = 2
          control = 1
          break
  if control == 0:
    valor = random.randint(0,8)
    while cuadrantes[valor] != 0:
      valor = random.randint(0,8)
    coordenadas = [int(valor%3),int(valor/3)]
    Dibujar_O(coordenadas)
    cuadrantes[valor] = 2
  return

#Funcion que hace la logica del tic tac toe
def Codicion_Victoria():
  Victoria = 0
  #Para el caso de 3 en fila recta:
  for n in range(0,3):
    if ((cuadrantes[3*n] == 1) and (cuadrantes[(3*n)+1] == 1) and (cuadrantes[(3*n)+2] == 1)) or ((cuadrantes[n] == 1) and (cuadrantes[n+3] == 1) and (cuadrantes[n+6] == 1)):
      Victoria = 1
      break
    elif (cuadrantes[3*n] == 2 and cuadrantes[(3*n)+1] == 2 and cuadrantes[(3*n)+2] == 2) or (cuadrantes[n] == 2 and cuadrantes[n+3] == 2 and cuadrantes[n+6] == 2):
      Victoria = 2
      break
  #Para el caso de 3 en las diagonales:
  if (cuadrantes[0] == 1 and cuadrantes[4] == 1 and cuadrantes[8] == 1) or (cuadrantes[2] == 1 and cuadrantes[4] == 1 and cuadrantes[6] == 1):
    Victoria = 1
  elif (cuadrantes[0] == 2 and cuadrantes[4] == 2 and cuadrantes[8] == 2) or (cuadrantes[2] == 2 and cuadrantes[4] == 2 and cuadrantes[6] == 2):
    Victoria = 2
  return Victoria

#Pantallas de victoria
def Pantalla_Victoria(ganador):
  backgroud_color = 52,52,52
  screen.fill(backgroud_color)
  if ganador == 1:
    color_base = 0,0,222
    #DIBUJAR 1
    pygame.draw.line(screen, color_base, (264,311), (296,311), 1)
    pygame.draw.line(screen, color_base, (280,262), (280,311), 1)
    pygame.draw.line(screen, color_base, (280,262), (264,275), 1)
  elif ganador == 2:
    color_base = 222,0,0
    #DIBUJAR 2
    pygame.draw.line(screen, color_base, (264,311), (296,311), 1)
    pygame.draw.line(screen, color_base, (264,311), (291,289), 1)
    pygame.draw.circle(screen, color_base, (280,278), 16, 1, True, True, False, False)
    pygame.draw.arc(screen, color_base, (264,262,32,32), 5.49779, 6.26573, 1)
  else:
    color_base = 222,222,222
  
  #Impresion de VICTORIA P1 / P2
  #V [(incio 52) (letras 49)x7 (espaciado 9)x6 (final 52) -> 501]horizontal ||| [(incio 190) (letra 49) (espaciado 23) (letra 49) (final 190) -> 501]verticalmente 
  pygame.draw.line(screen, color_base, (52,190), (77,239), 1)
  pygame.draw.line(screen, color_base, (77,239),(101,190), 1)
  #I
  pygame.draw.line(screen, color_base, (113,190),(156,190), 1)
  pygame.draw.line(screen, color_base, (135,239),(135,190), 1)
  pygame.draw.line(screen, color_base, (113,239),(156,239), 1)
  #C
  pygame.draw.line(screen, color_base, (193,190),(212,190), 1)
  pygame.draw.circle(screen, color_base, (193,215), 24, 1, False, True, True, False)
  pygame.draw.line(screen, color_base, (193,239),(212,239), 1)
  #T
  pygame.draw.line(screen, color_base, (226,190),(275,190), 1)
  pygame.draw.line(screen, color_base, (251,239),(251,190), 1)
  #O
  pygame.draw.circle(screen, color_base, (310,215), 24, 1)
  #R
  pygame.draw.line(screen, color_base, (350,190), (350,239) ,1)
  pygame.draw.line(screen, color_base, (350,190), (370,190) ,1)
  pygame.draw.line(screen, color_base, (350,215), (370,215) ,1)
  pygame.draw.circle(screen, color_base, (371,203), 12, 1, True, False, False, True)
  pygame.draw.line(screen, color_base, (370,215), (382,239) ,1)
  #Y
  pygame.draw.line(screen, color_base, (400,190),(425,215), 1)
  pygame.draw.line(screen, color_base, (425,215),(425,239), 1)
  pygame.draw.line(screen, color_base, (425,215),(450,190), 1)
  #P [197 / 49 / 9 / 49 / 197 -> 501]
  pygame.draw.line(screen, color_base, (205,262), (205,311) ,1)
  pygame.draw.line(screen, color_base, (205,262), (225,262) ,1)
  pygame.draw.line(screen, color_base, (205,287), (225,287) ,1)
  pygame.draw.circle(screen, color_base, (226,275), 12, 1, True, False, False, True)

  pygame.display.flip()
  return

#Pantalla de empate
def Pantalla_Empate():
  backgroud_color = 52,52,52
  screen.fill(backgroud_color)
  color_base = (222,222,222)
  #Dibujar "Draw" [incio 139 - letras 49 x4 - espaciado 9 x3 - final 139] horizontal - - - [incio 226 - letra 49 - final 226] verticalmente
  #D
  D = [(164,226),(139,226),(139,275),(164,275)]
  pygame.draw.lines(screen, color_base, False, D, 1)
  pygame.draw.circle(screen, color_base, (164,251), 24.5, 1, True, False, False, True)
  #R
  R = [(228,226),(203,226),(203,251),(228,251),(203,251),(203,275)]
  pygame.draw.lines(screen, color_base, False, R, 1)
  pygame.draw.circle(screen, color_base, (228,239), 12.75, 1,True, False, False, True)
  pygame.draw.line(screen, color_base, (228,251), (235,275), 1)
  #A
  A = [(255,275),(279,226),(303,275)]
  pygame.draw.lines(screen, color_base, False, A, 1)
  pygame.draw.line(screen, color_base, (267,251), (291,251), 1)
  #W
  W = [(313,226),(329,275),(337,251),(345,275),(361,226)]
  pygame.draw.lines(screen, color_base, False, W, 1)
  pygame.display.flip()
  return

#INICIO DEL MAIN 
Menu_Inicio()
pygame.display.flip()
while running_menu:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running_menu = False
    elif event.type == pygame.MOUSEBUTTONUP:
      ubicacion_menu = pygame.mouse.get_pos()
      Jugador = Quien_Juega(ubicacion_menu)
      if Jugador == 1:
        running_gameIA = True
        running_menu = False
      elif Jugador == 2:
        running_game = True
        running_menu = False

screen.fill(backgroud_color)
Imprimir_Tablero()
pygame.display.flip()
time.sleep(2)
#Un bucle en función de nuestra variable de control
#MODO DE JUEGO 1vs1 (2 jugadores)
while running_game:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running_game = False
    elif event.type == pygame.MOUSEBUTTONUP:
      ubicacion_juego = pygame.mouse.get_pos()
      if Juego() != 0:
        Victoria = Codicion_Victoria()
        if Victoria != 0:
          Pantalla_Victoria(Victoria)
          time.sleep(3)
          running_game = False
        elif turnos>7:
          Pantalla_Empate()
          time.sleep(3)
          running_game = False
        else:
          turnos+=1
      

#MODO DE JUEGO 1vsIA (1 jugador)
while running_gameIA:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running_gameIA = False
    elif event.type == pygame.MOUSEBUTTONUP:
      ubicacion_juego = pygame.mouse.get_pos()
      if JuegoIA() != 0:
        Victoria = Codicion_Victoria()
        if Victoria != 0:
          Pantalla_Victoria(Victoria)
          time.sleep(3)
          running_gameIA = False
        elif turnos > 3:
          Pantalla_Empate()
          time.sleep(3)
          running_gameIA = False
        else:
          TurnoIA()
          turnos+=1
          Victoria = Codicion_Victoria()
          if Victoria != 0:
            Pantalla_Victoria(Victoria)
            time.sleep(3)
            running_gameIA = False