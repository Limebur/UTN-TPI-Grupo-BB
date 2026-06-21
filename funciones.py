import csv
import os
import questionary

def continuar():
    input("Presione cualquier tecla para continuar")

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Ingrese un número positivo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número entero.")

def pedir_nombre(mensaje):
    while True:
        try:
            nombre= input(mensaje).title().strip() 
            if nombre == "":
                raise ValueError("Error: No se permiten espacios vacios")
            elif not nombre.replace(" ", "").isalpha():
                raise ValueError("Error: Debe ingresar solamente letras")
            return nombre
        except ValueError as e:
            print(e)

def cargar_csv(nombre_archivo):
    paises = []
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
    try:
        with open(ruta, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"]})    
    except FileNotFoundError:
        print("No se encontró el archivo.")
    except ValueError:
        print("Error: formato inválido en el CSV.")
    return paises

def guardar_csv(nombre_archivo, paises):
    ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
    print("Archivo guardado con exito")

def agregar_pais(paises):
    print("== AGREGAR PAÍS ==")
    while True:
        try:
            nombre = pedir_nombre("Nombre: ")
            for pais in paises:
                if pais["nombre"].lower() == nombre.lower():
                    raise ValueError("Ese país ya existe.")
            break
        except ValueError as e:
            print(e)
    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie: ")
    continente = pedir_nombre("Continente: ")
    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(pais)
    print("País agregado correctamente.")
    continuar()
    limpiar_consola()

def actualizar_pais(paises):
    print("== ACTUALIZAR PAÍS ==")
    while True:
        try:
            nombre = input("País a actualizar: ").lower()
            if nombre == "":
                raise ValueError("Error: No se aceptan espacios vacios")
            if not nombre.isalpha():
                raise ValueError("Error: Debe ingresar solamente letras")
            break
        except ValueError as e:
            print(e)
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            pais["poblacion"] = pedir_entero("Nueva población: ")
            pais["superficie"] = pedir_entero("Nueva superficie: ")
            print("País actualizado.")
            continuar()
            limpiar_consola()
            return
    print("País no encontrado.")
    continuar()
    limpiar_consola()

def buscar_pais(paises):
    print("== BUSCAR PAÍS ==")
    pais_buscar = pedir_nombre("Ingrese el nombre del pais que desea buscar (de forma exactaa o parcial): ")
    encontrados = False
    for pais in paises:
        if pais_buscar.lower() in pais["nombre"].lower():
            encontrados = True
            print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
    if not encontrados:
        print("País no encontrado")
        continuar()
        limpiar_consola()
    else:
        continuar()
        limpiar_consola()   

def filtrar_continente(paises):
    print("== FILTRAR CONTINENTE ==")
    encontrado= False
    continente = pedir_nombre("Ingrese el nombre del continente para ver sus paises: ")
    print(f"[Paises del continente {continente}]")
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]}")
            encontrado= True
    if not encontrado:
        print(f">> No se a encontrado ningun pais en el continente {continente}")
        continuar()
        limpiar_consola()
    else:
        continuar()
        limpiar_consola()   

def filtrar_poblacion(paises):
    print("== FILTRAR POBLACIÓN ==")
    minimo = pedir_entero("Mínimo: ")
    maximo = pedir_entero("Máximo: ")
    if minimo > maximo:
        print("El mínimo no puede ser mayor al máximo.")
        return
    encontrados = False
    print(f"[Paises filtrados por poblacion entre {minimo} y {maximo}]")
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
            encontrados = True
    if not encontrados:
        print("No se encontraron países en el rango de población establecido.")
        continuar()
        limpiar_consola()
    else:
        continuar()
        limpiar_consola()      

def filtrar_superficie(paises):
    print("== FILTRAR SUPERFICIE ==")
    minimo = pedir_entero("Mínimo: ")
    maximo = pedir_entero("Máximo: ")
    if minimo > maximo:
        print("El mínimo no puede ser mayor al máximo.")
        return
    encontrados = False
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
            encontrados = True
    if not encontrados:
        print("No se encontraron países en el rango de superficie establecido.")
        continuar()
        limpiar_consola()
    else:
        continuar()
        limpiar_consola()

def menu_filtros(paises):
    while True:
        opcion = questionary.select(
        message= "=== FILTROS ===",
        choices=["1. Continente", "2. Población", "3. Superficie", "0. Volver"]
    ).ask()

        if opcion == "1. Continente":
            filtrar_continente(paises)
        elif opcion == "2. Población":
            filtrar_poblacion(paises)
        elif opcion == "3. Superficie":
            filtrar_superficie(paises)
        elif opcion == "0. Volver":
            print("Volviendo al menú...")
            continuar()
            limpiar_consola()
            break

def ordenar_nombre(paises):
    ordenados = sorted(paises, key=lambda x: x["nombre"])
    for pais in ordenados:
        print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
    continuar()
    limpiar_consola()

def ordenar_poblacion(paises, descendente=False):
    ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=descendente)
    for pais in ordenados:
        print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
    continuar()
    limpiar_consola()

def ordenar_superficie(paises, descendente=False):
    ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=descendente)
    for pais in ordenados:
        print(f"- Pais: {pais["nombre"]} | Poblacion: {pais["poblacion"]} | Superficie: {pais["superficie"]} | Continente: {pais["continente"]}")
    continuar()
    limpiar_consola()

def menu_ordenamientos(paises):
    while True:
        opcion = questionary.select(
        message= "=== ORDENAMIENTOS ===",
        choices=["1. Nombre", "2. Población ascendente", "3. Población descendente", "4. Superficie ascendente", "5. Superficie descendente", "0. Volver"]
    ).ask()

        if opcion == "1. Nombre":
            ordenar_nombre(paises)
        elif opcion == "2. Población ascendente":
            ordenar_poblacion(paises)
        elif opcion == "3. Población descendente":
            ordenar_poblacion(paises, descendente=True)
        elif opcion == "4. Superficie ascendente":
            ordenar_superficie(paises)
        elif opcion == "5. Superficie descendente":
            ordenar_superficie(paises, descendente=True)
        elif opcion == "0. Volver":
            print("Volviendo al menú...")
            continuar()
            limpiar_consola()            
            break

def mostrar_estadisticas(paises):
    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = (sum(p["poblacion"] for p in paises) / len(paises))
    promedio_superficie = (sum(p["superficie"] for p in paises) / len(paises))
    continentes = {}
    for pais in paises:
        cont = pais["continente"]
        continentes[cont] = (continentes.get(cont, 0) + 1)
    print("== ESTADISTICAS ==")
    print("● Mayor población:", mayor["nombre"])
    print("● Menor población:", menor["nombre"])
    print("● Promedio población:", round(promedio_poblacion, 2))
    print("● Promedio superficie:", round(promedio_superficie, 2)    )
    print("● Países por continente:")
    for c, cantidad in continentes.items():
        print(f" - {c}: {cantidad}")
    continuar()
    limpiar_consola()