# ===== CLASE COCHE =====
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, v):
        self.velocidad += v
        print(f"Aceleraste {v} km/h")

    def frenar(self, v):
        self.velocidad -= v
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Frenaste {v} km/h")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h")


# ===== CLASE CUENTA BANCARIA =====
class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Depósito realizado")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro realizado")
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}, Saldo: ${self.saldo}")


# ===== CLASE RECTÁNGULO =====
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        print(f"Ancho: {self.ancho}, Alto: {self.alto}")
        print(f"Área: {self.calcular_area()}")
        print(f"Perímetro: {self.calcular_perimetro()}")


# ===== MENÚ PRINCIPAL =====
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Probar Coche")
    print("2. Probar Cuenta Bancaria")
    print("3. Probar Rectángulo")
    print("ESC + Enter para salir")

    op = input("Opción: ")

    if op == "\x1b":
        print("Saliendo...")
        break

    # ===== COCHE =====
    elif op == "1":
        marca = input("Marca (ej: Toyota): ")
        modelo = input("Modelo (ej: Corolla): ")
        color = input("Color (ej: Rojo): ")

        coche = Coche(marca, modelo, color)

        coche.mostrar_info()
        v = int(input("Cuánto acelerar? (ej: 20): "))
        coche.acelerar(v)

        v = int(input("Cuánto frenar? (ej: 10): "))
        coche.frenar(v)

        coche.mostrar_info()

    # ===== CUENTA =====
    elif op == "2":
        nombre = input("Titular (ej: Juan): ")
        cuenta = CuentaBancaria(nombre)

        d = float(input("Depósito inicial (ej: 500): "))
        cuenta.depositar(d)

        r = float(input("Retiro (ej: 200): "))
        cuenta.retirar(r)

        cuenta.mostrar_saldo()

    # ===== RECTÁNGULO =====
    elif op == "3":
        a = float(input("Ancho (ej: 5): "))
        h = float(input("Alto (ej: 10): "))

        rect = Rectangulo(a, h)
        rect.mostrar_info()

    else:
        print("Opción inválida")
