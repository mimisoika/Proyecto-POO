import pygame
import sys

# Inicializar Pygame
pygame.init()

# Tamaño de la ventana
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

# Bucle principal
while True:
    #w
    surface.fill(background_color)
    
    # Actualizar la ventana
    pygame.display.flip()
    
    # Esperar a que el usuario ingrese un comando
    command = input("Ingrese un comando ('linea -h' o 'linea -v'): ")
    
    # Salir del programa si el usuario ingresa 'exit'
    if command == 'exit':
        pygame.quit()
        sys.exit()
    
    # Verificar el comando ingresado
    if command == 'linea -h':
        # Obtener las coordenadas y tamaño del rectángulo
        x = int(input("Ingrese la coordenada del eje x: "))
        y = int(input("Ingrese la coordenada del eje y: "))

        def linea_v():
            for i in range(0,100):
                surface.set_at((x + i, y), color)
            pygame.display.flip()
        
    elif command == 'linea -v':
        # Obtener las coordenadas y radio del círculo
        x = int(input("Ingrese la coordenada x del centro: "))
        y_start = int(input("Ingrese la coordenada y_start de la linea: "))
        y_end = int(input("Ingrese la coordenada y_end de la linea: "))

        def linea_v():
            for i in range(y_start,y_end + 1):
                surface.set_at((x, i), color)
            pygame.display.flip()