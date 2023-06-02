import pygame
import math


# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255,23,100)
surface.fill(background_color)
#colores disponible
colores = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0),
    "negro": (0, 0, 0),
    "blanco": (254, 254, 254)
}

current_color = colores["rojo"]
current_background_color = background_color
current_line_thickness = 1

drawings = []

def camcolor_fondo(color):
    global current_background_color
    current_background_color = color
    surface.fill(current_background_color)
    pygame.display.flip()

def linea(star_x, start_y, end_x, end_y):
    pygame.draw.line(surface, current_color, (star_x, star_y), (end_x, end_y), current_line_thickness)
    pygame.display.flip()

    drawings.append(("line", star_x, start_y, end_x, end_y))

def cuadrado(x, y, z):
    k = z
    pygame.draw.rect(surface, current_color, pygame.Rect(x, y, z, k), current_line_thickness)
    pygame.display.flip()

    drawings.append(("square", x, y))


    # Agregar el dibujo a la lista
    drawings.append(("square", x, y))

def rectangulo(x, y, ancho, alto):
    pygame.draw.rect(surface, current_color, pygame.Rect(x, y, ancho, alto), current_line_thickness)
    pygame.display.flip()

    drawings.append(("rectangle", x, y))

def circulo(x, y, radio):
    pygame.draw.circle(surface, current_color, (x,y), radio, current_line_thickness)
    pygame.display.flip()

    drawings.append(("circulo", x, y, radio))

def triangulo(px_1, py_1, px_2, py_2, px_3, py_3):
    pygame.draw.polygon(surface, current_color, ((px_1,py_1), (px_2,py_2), (px_3,py_3)), current_line_thickness)
    pygame.display.flip()

    drawings.append(("triangulo", px_1, py_1, px_2, py_2, px_3, py_3))

def show_menu():
    print("Selecciona una opción:")
    print("cuadrado")
    print("rectángulo")
    print("circulo")
    print("linea")
    print("triangulo")
    print("color_lineas")
    print("color_fondo")
    print("grosor_lineas")

# Esperar a que el usuario cierre la ventana
while True:

    show_menu()

    cmd = input("cmd> ")
    if cmd == "exit":
        pygame.quit()

    if cmd == "cuadrado":
        x = int(input("coordenada en el eje x : "))
        y = int(input("coordenada en el eje y : "))
        z = int(input("Largo de los lados del cuadrado: "))
        cuadrado(x, y, z)

    if cmd == "rectangulo":
        x = int(input("coordenada en el eje x : "))
        y = int(input("coordenada en el eje y : "))
        ancho = int(input("Largo de ancho del rectangulo: "))
        alto = int(input("Largo de alto del rectangulo: "))
        rectangulo(x, y, ancho, alto)
        
    if cmd == "circulo":
        x = int(input("coordenada en el eje x: "))
        y = int(input("coordenada en el eje y : "))
        radio = int(input("Radio del circulo: "))
        circulo(x, y, radio)

    if cmd == "linea":      
        star_x = int(input("coordenada en el eje x punto A: "))
        start_y = int(input("coordenada en el eje y del punto A: "))
        end_x = int(input("coordenada en el eje x del punto B: "))
        end_y = int(input("coordenada en el eje y del punto B: "))
        linea(star_x, start_y, end_x, end_y)

    if cmd == "triangulo":      
        px_1 = int(input("coordenada en el eje x punto 1: "))
        py_1 = int(input("coordenada en el eje y punto 1: "))
        px_2 = int(input("coordenada en el eje x punto 2: "))
        py_2 = int(input("coordenada en el eje y punto 2: "))
        px_3 = int(input("coordenada en el eje x punto 3: "))
        py_3 = int(input("coordenada en el eje y punto 3: "))
        linea(px_1, py_1, px_2, py_2, px_3, py_3)

    if cmd == "color_lineas":
        print("Colores disponible para las lineas:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Azul")
        print("4. Amarillo")
        print("5. negro")
        print("6. blanco")

        color_option = input("Ingresa el numero del color que deseas para las lineas:")

        if color_option == "1":
            current_color = colores["rojo"]
        elif color_option == "2":
            current_color = colores["verde"]
        elif color_option == "3":
            current_color = colores["azul"]
        elif color_option == "4":
            current_color = colores["amarillo"]
        elif color_option == "5":
            current_color = colores["negro"]
        elif color_option == "6":
            current_color = colores["blanco"]

        else:
            print("Opción inválida. Se utilizará el color predeterminado.")
    
    if cmd == "color_fondo":
        print("Colores disponibles para el fondo:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Azul")
        print("4. Amarillo")
        print("5. Negro")
        print("6. Blanco")


        color_option = input("Ingresa el numero del color que deseas para el fondo:")

        if color_option == "1":
            camcolor_fondo(colores["rojo"])
        elif color_option == "2":
            camcolor_fondo(colores["verde"])   
        elif color_option == "3":
            camcolor_fondo(colores["azul"])
        elif color_option == "4":
            camcolor_fondo(colores["amarillo"])
        elif color_option == "5":
            camcolor_fondo(colores["negro"])
        elif color_option == "6":
            camcolor_fondo(colores["blanco"])
        else:
            print("Opción inválida")
    if cmd == "grosor_lineas":
       thickness = int(input("Grosor para las lineas: "))
       current_line_thickness = thicknes
    else:
        print("Opción inválida.")