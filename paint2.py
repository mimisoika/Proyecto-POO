import pygame
import sys
from pygame.locals import *

pygame.init()


# set up the window
width = 800 
height = 600

surface = pygame.display.set_mode((width, height))

background_color = (255,23,100)


amarillo = (252,255,23)
rojo = (255,23,23)
naranja = (255,130,23)
morado = (171,23,255)
azul = (23,249,255)

color = rojo

def linea_h():
    for i in range(0,100):
        surface.set_at((100 + i, 200), color)
    ## Mostrar la superficie en la pantalla
    pygame.display.flip()

def linea_v():
    for i in range(0,100):
        surface.set_at((200, 100 + i), color)
    pygame.display.flip()

def triangulo():
    linea_h()
    linea_v()
    # Dibujar la diagonal del triángulo
    for i in range(0, 100):
        surface.set_at((200 + i, 100 + i), color)
    pygame.display.flip()
    


myfile = open("comando.cmd", "r")
for cmd in myfile:
    cmd = cmd.strip()
    if cmd == "linea -h":
        linea_h()
    if cmd == "linea -v":
        linea_v()
    if cmd == "triangulo":
        triangulo()
    print(f"-{cmd}-")
myfile.close()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
