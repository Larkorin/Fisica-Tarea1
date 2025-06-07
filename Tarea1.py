import math

def obtener_vector_por_componentes():
    x = float(input("Ingrese el componente en X: "))
    y = float(input("Ingrese el componente en Y: "))
    return x, y

def obtener_vector_por_magnitud_direccion():
    magnitud = float(input("Ingrese la magnitud del vector: "))
    angulo_grados = float(input("Ingrese la direccion(grados): "))
    angulo_radianes = math.radians(angulo_grados)
    x = magnitud * math.cos(angulo_radianes)
    y = magnitud * math.sin(angulo_radianes)
    return x, y


total_vectores = int(input("¿Cuántos vectores desea sumar?: "))
suma_x = 0
suma_y = 0

for i in range(total_vectores):
    print(f"\nVector #{i+1}")
    
    while True:
        metodo = input("Quiere ingresar por 'componentes' o 'magnitud y direccion'? (c/m): ")

        if metodo == 'c':
            x, y = obtener_vector_por_componentes()
            break
        elif metodo == 'm':
            x, y = obtener_vector_por_magnitud_direccion()
            break
        else:
            print("Opción no válida. Por favor ingrese 'c' o 'm'.")

    suma_x += x
    suma_y += y

print("\nResultado de la suma de vectores:")
print(f"Componente en X: {suma_x:.2f}m")
print(f"Componente en Y: {suma_y:.2f}m")

