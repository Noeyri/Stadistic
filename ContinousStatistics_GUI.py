# Tabla de frecuencia:
# Datos cuantitativos continuos

#Para poder llamar funciones de otro archivo .py
from Estadistica_Funciones_Proyecto import buscar, redondear
#Para poder usar log(10) importamos math
from math import log10

#Para la interfaz grafica
import flet as ft

# Solicitar al usuario la cantidad de datos que quiere ingresar
n = int(input("La cantidad de datos (n): "))

# Inicializar una lista vacía para almacenar los numeros
datos = []

# Usar un bucle para solicitar cada numero al usuario
for i in range(n):
    # Pedir al usuario que ingrese un numero
    numero_ingresado = int(input(f"Ingrese el dato {i + 1}: "))
    # Agregar el número a la lista
    datos.append(numero_ingresado)

print("")
# Mostrar la lista de números ingresados
print("Los datos ingresados:", datos)
# Ordenar de menor a mayor
datos.sort()
print("Ordered numbers (Menor a mayor):", datos)
# Ordenar de mayor a menor
# datos.sort(reverse=True)
# print("Ordered numbers (Mayor a menor):", datos)
# print(datos.__len__()) para hallar la cantidad de datos
print(f"Numero Mayor: {max(datos)}")
print(f"Numero Menor: {min(datos)}")
print("TOTAL: n = ", n)

# PASO 1: Hallando el Rango (R)
r = max(datos) - min(datos)
print("R = ",r)

# PASO 2: Hallando el numero de intervalos (K)
k = 1+3.322*log10(n)
print("K = ", k)
print("Redondeado: ", redondear(k))

# PASO 3: Hallando amplitud del intervalo (C) o Ancho (A)
c = r/k
print("C = ", c)
print("Redondeado: ", redondear(c))


# Hallando el limite superior y limite inferior
first_number = min(datos)


def interfaz(page: ft.Page):
    # Inicializamos los límites dentro de la función
    li = first_number  # limite inferior
    ls = first_number + redondear(c)  # limite superior

    # Título de la página
    page.title = "Tabla de Frecuencia"

    # Definición de las columnas de la tabla
    columns = [
        ft.DataColumn(ft.Text("Intervalo")),
        ft.DataColumn(ft.Text("fi")),
        ft.DataColumn(ft.Text("hi")),
        ft.DataColumn(ft.Text("hi%")),
        ft.DataColumn(ft.Text("xi")),
    ]

    # Lista para almacenar las filas de la tabla
    rows = []

    # Bucle para generar las filas dinámicamente
    contador = 0
    while contador < int(redondear(k)):  # Aseguramos que k sea un número entero
        fi_entre_n = int(buscar(li, ls, datos))  # Valor para la columna "fi"
        hi = fi_entre_n / float(n)  # Valor para la columna "hi"
        hi_Porcentual = int(hi * 100)  # Valor para la columna "hi%"
        xi = (li + ls) / float(2)  # Valor para la columna "xi"

        # Agregar una fila con estos valores
        rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"[{li}; {ls}]")),  # Intervalo
                    ft.DataCell(ft.Text(str(fi_entre_n))),
                    ft.DataCell(ft.Text(f"{hi:.2f}")),
                    ft.DataCell(ft.Text(f"{hi_Porcentual}%")),
                    ft.DataCell(ft.Text(f"{xi:.2f}")),
                ]
            )
        )

        # Incrementar el límite inferior y superior para el siguiente intervalo
        li = li + int(redondear(c))
        ls = ls + int(redondear(c))

        # Incrementar el contador para la siguiente fila
        contador += 1

    # Crear la tabla con las columnas y filas
    table = ft.DataTable(columns=columns, rows=rows)

    # Agregar la tabla a la página
    page.add(table)

# Ejecutar la aplicación
ft.app(target=interfaz)