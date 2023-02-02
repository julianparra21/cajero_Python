def depositar(saldo, monto):
    return saldo + monto


def retirar(saldo, monto):
    if saldo >= monto:
        return saldo - monto
    else:
        return "Saldo insuficiente"


def consultar_saldo(saldo):
    return saldo


saldo = 0
nombre = input("Ingrese su nombre: ")

opcion = 0
while opcion != 4:
    print("Bienvenido al cajero, ", nombre)
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        monto = int(input("Ingrese el monto a depositar: "))
        saldo = depositar(saldo, monto)
        print("Deposito realizado con éxito. Nuevo saldo: ", saldo)
    elif opcion == 2:
        monto = int(input("Ingrese el monto a retirar: "))
        saldo = retirar(saldo, monto)
        if isinstance(saldo, int):
            print("Retiro realizado con éxito. Nuevo saldo: ", saldo)
        else:
            print(saldo)
    elif opcion == 3:
        print("Su saldo es: ", consultar_saldo(saldo))
    elif opcion == 4:
        print("Gracias por utilizar nuestro cajero.")
    else:
        print("Opción inválida. Intente nuevamente.")
