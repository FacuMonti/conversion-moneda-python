# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms

medidas_en_cms = input("Ingrese las medidas de la pieza del mueble en centímetros: ")

# Paso 2: Convertir las medidas de centimetros a pulgadas

medidas_en_pulgadas = float(medidas_en_cms) / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario

print(f"Las medidas de la pieza del mueble en pulgadas son: {medidas_en_pulgadas:.2f} pulgadas")