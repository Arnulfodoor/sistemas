import json

def cargar_recetas():
    try:
        with open('recetas.json') as file:
            recetas = json.load(file)
        return recetas
    except FileNotFoundError:
        return []

def guardar_recetas(recetas):
    with open('recetas.json', 'w') as file:
        json.dump(recetas, file, indent=4)

def mostrar_recetas(recetas):
    if not recetas:
        print("No hay recetas disponibles.")
    else:
        print("Recetas disponibles:")
        for i, receta in enumerate(recetas, 1):
            print(f"{i}. {receta['nombre']}")

def mostrar_receta(recetas, indice):
    if 0 <= indice < len(recetas):
        receta = recetas[indice]
        print("--- Detalles de la Receta ---")
        print(f"Nombre: {receta['nombre']}")
        print("Ingredientes:")
        for ingrediente in receta['ingredientes']:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in receta['pasos']:
            print(f"- {paso}")
    else:
        print("Índice de receta inválido.")

def agregar_receta(recetas):
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por coma): ").split(",")
    pasos = input("Ingrese los pasos de la receta (separados por coma): ").split(",")
    receta = {
        "nombre": nombre,
        "ingredientes": ingredientes,
        "pasos": pasos
    }
    recetas.append(receta)
    guardar_recetas(recetas)
    print("Receta agregada exitosamente.")

def main():
    recetas = cargar_recetas()

    while True:
        print("\n--- Gestor de Recetas ---")
        print("1. Mostrar recetas disponibles")
        print("2. Mostrar detalles de una receta")
        print("3. Agregar nueva receta")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_recetas(recetas)
        elif opcion == "2":
            indice_str = input("Ingrese el numero de la receta: ")
            try:
                indice = int(indice_str) - 1
                mostrar_receta(recetas, indice)
            except ValueError:
                print("¡Ingrese un índice válido!")
        elif opcion == "3":
            agregar_receta(recetas)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == '__main__':
    main()
