def input_data():
    # Solicitar al usuario la cantidad de datos que quiere ingresar
    number_of_data = int(input("La cantidad de datos (n): "))

    # Inicializar una lista vacía para almacenar los numeros
    data = []

    # Usar un bucle para solicitar cada numero al usuario
    for i in range(number_of_data):
        # Pedir al usuario que ingrese un numero
        number = int(input(f"Ingrese el dato {i + 1}: "))
        # Agregar el número a la lista
        data.append(number)
    
    print("")
    # Mostrar la lista de números ingresados
    print("Los datos ingresados:", data)

    # Ordenar de menor a mayor
    data.sort()
    print("Ordered numbers (Menor a mayor):", data)
    return data