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
grosor = 3
drawings = []

def camcolor_fondo(color):
    global current_background_color
    current_background_color = color
    surface.fill(current_background_color)
    pygame.display.flip()

def linea(star_x, start_y, end_x, end_y):
    pygame.draw.line(surface, current_color, (star_x, start_y), (end_x, end_y), grosor)
    pygame.display.flip()

    drawings.append(("line", star_x, start_y, end_x, end_y))

def cuadrado(x, y, z):
    k = z
    pygame.draw.rect(surface, current_color, pygame.Rect(x, y, z, k), grosor)
    pygame.display.flip()

    drawings.append(("square", x, y))

def rectangulo(x, y, ancho, alto):
    pygame.draw.rect(surface, current_color, pygame.Rect(x, y, ancho, alto), grosor)
    pygame.display.flip()

    drawings.append(("rectangle", x, y))

def circulo(x, y, radio):
    pygame.draw.circle(surface, current_color, (x,y), radio, grosor)
    pygame.display.flip()

    drawings.append(("circulo", x, y, radio))


def triangulo_equilatero(lado):
    x = int(input("Ingrese la coordenada x del vértice superior: "))
    y = int(input("Ingrese la coordenada y del vértice superior: "))

    # Calcular las coordenadas de los vértices del triángulo
    altura = (math.sqrt(3) / 2) * lado
    x2 = x - lado / 2
    x3 = x + lado / 2
    y2 = y + altura
    y3 = y + altura

    pygame.draw.polygon(surface, current_color, ((x, y), (x2, y2), (x3, y3)), grosor)
    pygame.display.flip()

    drawings.append(("trianguloequi",x, y, x2, y2, x3, y3))

def triangulo_rectangulo(lado1, lado2):
    x = int(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
    y = int(input("Ingrese la coordenada y del vértice inferior izquierdo: "))

    # Calcular las coordenadas de los vértices del triángulo
    x2 = x + lado1
    y2 = y
    x3 = x
    y3 = y - lado2

    pygame.draw.polygon(surface, current_color, ((x, y), (x2, y2), (x3, y3)), grosor)
    pygame.display.flip()

    drawings.append(("triangulorect", x, y, x2, y2, x3, y3))

def triangulo_escaleno(lado1, lado2):
    x = int(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
    y = int(input("Ingrese la coordenada y del vértice inferior izquierdo: "))

    x2 = x + lado1
    y2 = y
    x3 = x + lado2
    y3 = y - math.sqrt(lado1**2 - lado2**2)

    pygame.draw.polygon(surface, current_color, ((x, y), (x2, y2), (x3, y3)), grosor)
    pygame.display.flip()

    drawings.append(("trianguloescaleno", x, y, x2, y2, x3, y3))

def triangulo_isosceles(lado1, lado2):
    x = int(input("Ingrese la coordenada x del vértice superior: "))
    y = int(input("Ingrese la coordenada y del vértice superior: "))

    # Calcular las coordenadas de los vértices del triángulo
    x2 = x - lado1 / 2
    x3 = x + lado1 / 2
    y2 = y + lado2
    y3 = y + lado2

    # Dibujar el triángulo
    pygame.draw.polygon(surface, current_color, ((x, y), (x2, y2), (x3, y3)), grosor)
    pygame.display.flip()

    drawings.append(("trianguloiso", x, y, x2, y2, x3, y3))

def triangulo_obtusangulo(lado1, lado2):
    x = int(input("Ingrese la coordenada x del vértice inferior izquierdo: "))
    y = int(input("Ingrese la coordenada y del vértice inferior izquierdo: "))

    # Calcular las coordenadas de los vértices del triángulo
    x2 = x + lado1
    y2 = y
    x3 = x + (lado1 * (lado1**2 + lado2**2 - lado1**2)) / (2 * lado1 * lado2)
    y3 = y - math.sqrt(lado2**2 - ((lado1 * (lado1**2 + lado2**2 - lado1**2)) / (2 * lado1 * lado2))**2)

    # Dibujar el triángulo
    pygame.draw.polygon(surface, current_color, ((x, y), (x2, y2), (x3, y3)), grosor)
    pygame.display.flip()

    drawings.append(("trianguloobs", x, y, x2, y2, x3, y3))

def eliminar_ultimo_dibujo():
    if len(drawings) == 0:
        print("No hay dibujos para eliminar.")
    else:
        del drawings[-1]
        print("Se eliminó el último dibujo.")
    pygame.display.flip()




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
    print("eliminar_ultimo_dibujo")

def menu_colores():
    print("Colores disponible:")
    print("1. Rojo")
    print("2. Verde")
    print("3. Azul")
    print("4. Amarillo")
    print("5. negro")
    print("6. blanco")

def menu_triangulos():
    print("Seleccione un tipo de triángulo:")
    print("1. Triángulo Equilátero")
    print("2. Triángulo Rectángulo")
    print("3. Triángulo Escaleno")
    print("4. Triángulo Isósceles")
    print("5. Triángulo Obtusángulo")

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
        menu_triangulos()

        opcion = int(input("Ingrese el número de la opción deseada: "))

        if opcion == 1:
            lado = int(input("Ingrese la medida del lado del triángulo equilátero: "))
            triangulo_equilatero(lado)
        elif opcion == 2:
            lado1 = int(input("Ingrese la medida del primer lado del triángulo rectángulo: "))
            lado2 = int(input("Ingrese la medida del segundo lado del triángulo rectángulo: "))
            triangulo_rectangulo(lado1, lado2)
        elif opcion == 3:
            lado1 = int(input("Ingrese la medida del primer lado del triángulo escaleno: "))
            lado2 = int(input("Ingrese la medida del segundo lado del triángulo escaleno: "))
            triangulo_escaleno(lado1, lado2)
        elif opcion == 4:
            lado1 = int(input("Ingrese la medida del primer lado del triángulo isósceles: "))
            lado2 = int(input("Ingrese la medida del segundo lado del triángulo isósceles: "))
            triangulo_isosceles(lado1, lado2)
        elif opcion == 5:
            lado1 = int(input("Ingrese la medida del primer lado del triángulo obtusángulo: "))
            lado2 = int(input("Ingrese la medida del segundo lado del triángulo obtusángulo: "))
            triangulo_obtusangulo(lado1, lado2)
        else:
            print("Opción inválida.")

    if cmd == "color_lineas":
        menu_colores()

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
        menu_colores()


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
       grosor = thicknes
    if cmd == ("eliminar_ultimo_dibujo"):
        eliminar_ultimo_dibujo()
    else:
        print("Opción inválida.")