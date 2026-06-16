from funciones import *
import questionary

limpiar_consola()
paises = cargar_csv("paises.csv")
while True:
    opcion = questionary.select(
    message= "=== GESTION DE PAISES ===",
    choices=["1. Agregar país", "2. Actualizar país", "3. Buscar país", "4. Filtrar países", "5. Ordenar países", "6. Estadísticas", "7. Guardar cambios", "0. Salir"]
).ask()
    if opcion == "1. Agregar país":
        limpiar_consola()
        agregar_pais(paises)
    elif opcion == "2. Actualizar país":
        limpiar_consola()        
        actualizar_pais(paises)
    elif opcion == "3. Buscar país":
        limpiar_consola()        
        buscar_pais(paises)
    elif opcion == "4. Filtrar países":
        limpiar_consola()        
        menu_filtros(paises)
    elif opcion == "5. Ordenar países":
        limpiar_consola()        
        menu_ordenamientos(paises)
    elif opcion == "6. Estadísticas":
        limpiar_consola()        
        mostrar_estadisticas(paises)
    elif opcion == "7. Guardar cambios":
        limpiar_consola()        
        guardar_csv("paises.csv", paises)
    elif opcion == "0. Salir":
        guardar_csv("paises.csv", paises)
        print("Cerrando programa...")
        break