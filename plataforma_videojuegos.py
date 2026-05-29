from functools import wraps

comparaciones = 0 ## pieza para realizar el conteo de comparaciones, que puede ser utilziado varias veces

def registrar_operacion(func):
    @wraps(func) ## utilizamos un decorator solo para mostrar el incio y fin de ciertos procesos
    def wrapper(*args, **kwargs):
        print(f"\nINICIO")
        resultado = func(*args, **kwargs)
        print(f"FINAL")
        return resultado
    return wrapper

def capturar_videojuegos(): ## Para evitar poner a mano todo, llamamos una sola funcion de captura de juegos
    videojuegos = []

    for i in range(2):
        print(f"\nVideojuego {i+1}")

        nombre = input("Nombre: ")
        genero = input("Género: ")
        precio = float(input("Precio: "))
        activos = int(input("Jugadores activos: "))
        calificacion = float(input("Calificación: "))

        videojuegos.append({
            "nombre": nombre,
            "genero": genero,
            "precio": precio,
            "activos": activos,
            "calificacion": calificacion
        })

    return videojuegos

@registrar_operacion
def ordenar_por_popularidad(videojuegos):
    return sorted(videojuegos, key=lambda x: x["activos"], reverse=True) ## utilizamos la funcion sort ya que es propia de python y esta optimizada

@registrar_operacion
def ordenar_por_precio(videojuegos):
    return sorted(videojuegos, key=lambda x: x["precio"]) ## utilizamos la funcion sort ya que es propia de python y esta optimizada

@registrar_operacion
def busqueda_lineal(videojuegos, nombre): ##implementacion de busqueda lineal
    global comparaciones
    comparaciones = 0

    for juego in videojuegos:
        comparaciones += 1
        if juego["nombre"].lower() == nombre.lower():
            return juego

    return None

@registrar_operacion
def busqueda_binaria(videojuegos, nombre): ##implementacion busqueda binaria
    global comparaciones
    comparaciones = 0

    izquierda = 0
    derecha = len(videojuegos) - 1

    while izquierda <= derecha:
        comparaciones += 1

        medio = (izquierda + derecha) // 2
        actual = videojuegos[medio]["nombre"].lower()

        if actual == nombre.lower():
            return videojuegos[medio]

        if actual < nombre.lower():
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None

def videojuego_mas_popular(videojuegos):
    return max(videojuegos, key=lambda x: x["activos"]) ##utilizamos funcion de python max ya que esta optimizada

def promedio_calificaciones(videojuegos):
    return sum(map(lambda x: x["calificacion"], videojuegos)) / len(videojuegos) ## utilizamos sum con una lista que solo da la calificacion de la lista d evideojuegos

def crear_descuento(porcentaje): ##implementacion descuento
    def descuento(precio):
        return precio - (precio * porcentaje / 100)
    return descuento

def mostrar_catalogo(videojuegos, titulo):
    print(f"\n{titulo}")

    for juego in videojuegos:
        print(
            juego["nombre"],
            juego["genero"],
            juego["precio"],
            juego["activos"],
            juego["calificacion"]
        )
## implementacion final
videojuegos = capturar_videojuegos()

mostrar_catalogo(videojuegos, "CATÁLOGO ORIGINAL")

orden_popularidad = ordenar_por_popularidad(videojuegos)
mostrar_catalogo(orden_popularidad, "CATÁLOGO ORDENADO POR POPULARIDAD")

orden_precio = ordenar_por_precio(videojuegos)
mostrar_catalogo(orden_precio, "CATÁLOGO ORDENADO POR PRECIO")

nombre_buscar = input("\nNombre a buscar: ")

resultado_lineal = busqueda_lineal(videojuegos, nombre_buscar)

if resultado_lineal:
    print("\nBúsqueda lineal encontrada:", resultado_lineal)
else:
    print("\nNo encontrado en búsqueda lineal")

print("Comparaciones lineales:", comparaciones)

orden_nombre = sorted(videojuegos, key=lambda x: x["nombre"].lower())

resultado_binaria = busqueda_binaria(orden_nombre, nombre_buscar)

if resultado_binaria:
    print("\nBúsqueda binaria encontrada:", resultado_binaria)
else:
    print("\nNo encontrado en búsqueda binaria")

print("Comparaciones binarias:", comparaciones)

popular = videojuego_mas_popular(videojuegos)
print("\nVIDEOJUEGO MÁS POPULAR")
print(popular)

promedio = promedio_calificaciones(videojuegos)
print("\nPROMEDIO DE CALIFICACIONES:", promedio)

descuento20 = crear_descuento(20)

print("\nPRECIOS CON DESCUENTO DEL 20%")

for juego in videojuegos:
    print(
        juego["nombre"],
        "Precio original:",
        juego["precio"],
        "Precio descuento:",
        descuento20(juego["precio"])
    )