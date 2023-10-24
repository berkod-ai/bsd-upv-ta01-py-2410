## Tarea 1:

def eje1():
    semaforo = input("Semáforo?: ")
    if semaforo == "Verde":
        print("Cruzar la calle")
    else:
        print("Esperar")


def eje2():
    compra = int(input("Cuanto es la compra?: "))
    if compra > 100:
        descuento = compra*0.9
        precio = compra - descuento
    else:
        precio = compra
    print(precio)


def eje3():
    year = int(input("Que año es?: "))
    if year <= 2055:
        print(f"Informes del Año {year}")



def eje4():
    mi_lista = ["Jose", "Andreu", "Berk", "Cris"]
    for nombre in mi_lista:
        print(nombre)


def eje5(n):
    #Fibonacci:
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


if __name__ == '__main__':
    #eje1()
    #eje2()
    #eje3()
    #eje4()
    print(eje5(8))