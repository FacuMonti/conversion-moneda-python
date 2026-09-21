# Paso 1: Definir el valor actual del Euro y Dolar al Peso Mexicano

tipo_cambio_eur_a_mxn = 23.70 # En un caso mas realista, este valor podría ser obtenido de una API de tipo de cambio en tiempo real O BDD
tipo_cambio_usd_a_mxn = 20.75 # En un caso mas realista, este valor podría ser obtenido de una API de tipo de cambio en tiempo real o BDD

# Paso 2: Solicitar al usuario el tipo de conversion (euro a mex o dolar a mex)

tipo_conversion = input("Ingrese 'EUR' para convertir Euros a Pesos Mexicanos o 'USD' para convertir Dólares a Pesos Mexicanos: ")

# Paso 3: Solicitar al usuario el monto a converitr

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversion utilizando el tipo de cambio correspondiente
# Paso 5: Mostrar el resultado de la conversion al usuario

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print(f"{monto_a_convertir} Euros equivalen a {resultado:.2f} Pesos Mexicanos.")
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print(f"{monto_a_convertir} Dólares equivalen a {resultado:.2f} Pesos Mexicanos.")
else:
    print("Tipo de conversión no válido. Por favor, ingrese 'EUR' o 'USD'.")
    