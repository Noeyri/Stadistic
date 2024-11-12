# Tabla de frecuencia:
# Datos cuantitativos continuos

#Para poder llamar funciones de otro archivo .py
from Estadistica_Funciones_Proyecto import buscar, redondear
#Para poder usar log(10) importamos math
from math import log10

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

li = first_number                   #limite inferior
ls = first_number + redondear(c)    #limite superior


print("")
print("Variable: obras:" + "  |   fi  |   hi   |  hi%  |   Xi")

contador = 0
while (contador <= k):
    fi_Entre_n = int(buscar(li, ls, datos))
    hi_Porcentual = int((fi_Entre_n / float(n) * 100))
    xi = (li + ls) / float(2)

# Solo para la marca de clase xi

#               limite inferior,  limite superior                       fi                               hi                                     hi%                                    xi
    print("   [" + str(li) + ";" + str(ls) + "]" + " ---->  |   " + str(fi_Entre_n) + "   |  " + str((fi_Entre_n/float(n))) + "   |  " + str(hi_Porcentual) + "%" + "  |  " + str((f"{xi:.2f}")))

    contador = contador + 1
    li = li + int(redondear(c))
    ls = ls + int(redondear(c))

print("")