from libros import Libro

mi_libro = Libro()
opcion = None
salida = False

while not salida:
    print("¿Qué quieres hacer?")
    print("1. Mostrar información del libro")
    print("2. Prestar el libro")
    print("3. Devolver el libro")
    print("4. Salir")

    opcion = input("Ingresa el número de la opción: ")

    if opcion == "1":
        mi_libro.mostrarInformacion("12345")
    elif opcion == "2":
        mi_libro.prestarLibro("12345")
    elif opcion == "3":
        mi_libro.devolverLibro("12345")
    elif opcion == "4":
        salida = True
        print("¡Hasta luego!")
    else:
        print("Opción no válida, por favor ingresa un número del 1 al 4.")
        