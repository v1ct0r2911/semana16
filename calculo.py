
def calcular_raices(a, b, c):
    # Cuantas raices retorna una ecuacion cuadratica?
    x1 = (-b + ((b*b - 4 * a * c) ** 0.5)) / (2 * a)
    x2 = (-b - ((b*b - 4 * a * c) ** 0.5)) / (2 * a)
    # esto retorna una tupla
    return x1, x2


def guardar_archivo(raices):
  # recordemos que raices es una tupla, por ende al ser un tupla un elemento que contiene
  # uno o mas datos, yo puede usar los indices para poder acceder a cada dato

  # recuerden que los elementos de esta tupla son numeros y para poder guardarlos en un archivo
  # deben ser convertidos a string
    archivo = open("raices.txt", "w")
    archivo.write("Las raices son las siguientes:\n")
    archivo.write("x1 = " + str(raices[0]) + "\n")
    archivo.write("x2 = " + str(raices[1]) + "\n")
    archivo.close()


def leer_archivo():
    archivo = open("raices.txt", "r")
    print(archivo.read())
