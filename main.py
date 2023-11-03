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


def eje6():
    for num in range(1, 20):
        if num % 2 != 0:
            print(num)


def eje7():
    num_list = [1, 6, -4, -19, 57, -98]
    for neg in num_list:
        if neg < 0:
            print(neg)


def eje8():
    peso = float(input("Peso(en kg): "))
    estatura = float(input("Estatura(en metros): "))

    imc = peso / (estatura **2)

    print("Tu índice de masa corporal (IMC) es:", imc)


def eje9():

    # Solicitar la cantidad a invertir, el interés anual y el número de años
    cantidad_invertida = float(input("Ingresa la cantidad a invertir: "))
    tasa_interes_anual = float(input("Ingresa la tasa de interés anual (en porcentaje): "))
    years = int(input("Ingresa el número de años de la inversión: "))

    # Calcular el capital obtenido
    tasa_interes_decimal = tasa_interes_anual / 100  # Convertir el interés a decimal
    capital_obtenido = cantidad_invertida * (1 + tasa_interes_decimal) ** years

    # Redondear el capital obtenido a dos decimales
    capital_obtenido = round(capital_obtenido, 2)

    # Mostrar el capital obtenido
    print("El capital obtenido después de", years, "años es:", capital_obtenido)


if __name__ == '__main__':
    #eje1()
    #eje2()
    #eje3()
    #eje4()
    #print(eje5(8))
    #eje6()
    #eje7()
    #eje8()
    eje9()