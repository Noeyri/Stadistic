# Tabla de frecuencia:
# Datos cuantitativos continuos

from input import input_data
#Para poder llamar funciones de otro archivo .py
from utils import buscar, redondear
#Para poder usar log(10) importamos math
from math import log10

datos = input_data()
number_of_data = len(datos)

# Ordenar de mayor a menor
# datos.sort(reverse=True)
# print("Ordered numbers (Mayor a menor):", datos)
# print(datos.__len__()) para hallar la cantidad de datos
print(f"Numero Mayor: {max(datos)}")
print(f"Numero Menor: {min(datos)}")
print("TOTAL: n = ", number_of_data)

# PASO 1: Hallando el Rango (R)
r = max(datos) - min(datos)
print("R = ",r)

# PASO 2: Hallando el numero de intervalos (K)
k = 1 + 3.322 * log10(number_of_data)
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
    hi_Porcentual = int((fi_Entre_n / float(number_of_data) * 100))
    xi = (li + ls) / float(2)

# Solo para la marca de clase xi

#               limite inferior,  limite superior                       fi                               hi                                     hi%                                    xi
    print("   [" + str(li) + ";" + str(ls) + "]" + " ---->  |   " + str(fi_Entre_n) + "   |  " + str((fi_Entre_n/float(number_of_data))) + "   |  " + str(hi_Porcentual) + "%" + "  |  " + str((f"{xi:.2f}")))

    contador = contador + 1
    li = li + int(redondear(c))
    ls = ls + int(redondear(c))

print("")