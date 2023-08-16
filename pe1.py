import json

def vali_numericas(x):
    bandera=True
    while bandera:
        try:
            int_x = int(x)
            if int_x >= 0:
                bandera=False
        except ValueError:
            print("Dato inválido")
        if bandera:
            x=input("Ingresalo de nuevo: ").strip() 
    return int_x
    
def vali_alfabeticas(y):
    bandera=True
    while bandera:
        try:
            if y.replace(" ",""):
                bandera=False
        except ValueError:
            print("Dato inválido")
        if bandera:
            y=input("Ingresalo de nuevo: ").strip() 
    return y



def cargar_datos():
    with open('PetShopping.json', 'r') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open('PetShopping.json', 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

def mostrar_mascotas(datos):
    for indice, mascota in enumerate(datos["pets"]):
        print(f"Índice: {indice}")
        print("Tipo:", mascota["tipo"])
        print("Raza:", mascota["raza"])
        print("Precio:", mascota["precio"])
        print("Servicios:", ", ".join(mascota["servicios"]))
        print()

def crear_mascota():
    tipo = vali_alfabeticas(input("Tipo de mascota: "))
    raza = vali_alfabeticas(input("Raza: "))
    talla = vali_alfabeticas(input("Talla: "))
    precio = vali_numericas(input("Precio: "))
    servicios = input("Servicios (separados por coma): ").split(", ")
    print(servicios)


    return {
        "tipo": tipo,
        "raza": raza,
        "talla": talla,
        "precio": precio,
        "servicios": servicios
    }

def mostrar_mascotas_por_tipo(datos, tipo):
    for mascota in datos["pets"]:
        if mascota["tipo"] == tipo:
            print("Raza:", mascota["raza"])
            print("Precio:", mascota["precio"])
            print("Servicios:", ", ".join(mascota["servicios"]))
            print()

def actualizar_mascota(datos, indice):
    mascota = datos["pets"][indice]
    print("Datos actuales:")
    print("Tipo:", mascota["tipo"])
    print("Raza:", mascota["raza"])
    print("Precio:", mascota["precio"])
    print("Servicios:", ", ".join(mascota["servicios"]))
    print()

    nuevos_datos = crear_mascota()
    datos["pets"][indice] = nuevos_datos

def eliminar_mascota(datos, indice):
    datos["pets"].pop(indice)

def main():
    datos = cargar_datos()

    while True:
        print("\n--- Menú ---")
        print("1. Mostrar todas las mascotas")
        print("2. Crear nueva mascota")
        print("3. Mostrar mascotas por tipo")
        print("4. Actualizar mascota por índice")
        print("5. Eliminar mascota por índice")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_mascotas(datos)
        elif opcion == "2":
            nueva_mascota = crear_mascota()
            datos["pets"].append(nueva_mascota)
            guardar_datos(datos)
        elif opcion == "3":
            tipo = vali_alfabeticas(input("Ingrese el tipo de mascota: "))
            mostrar_mascotas_por_tipo(datos, tipo)
        elif opcion == "4":
            indice = vali_numericas(input("Ingrese el índice de la mascota a actualizar: "))
            if 0 <= indice < len(datos["pets"]):
                actualizar_mascota(datos, indice)
                guardar_datos(datos)
            else:
                print("Índice inválido")
        elif opcion == "5":
            indice = vali_numericas(input("Ingrese el índice de la mascota a eliminar: "))
            if 0 <= indice < len(datos["pets"]):
                eliminar_mascota(datos, indice)
                guardar_datos(datos)
            else:
                print("Índice inválido")
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

main()
