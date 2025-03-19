def input_fruits():
    fruits = []
    
    while len(fruits) < 10:
        nombre = input(f"Ingrese el nombre de la fruta {len(fruits) + 1}: ").strip()
        
        while True:
            try:
                precio = float(input(f"Ingrese el precio de {nombre}: ").strip())
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                break
            except ValueError:
                print("⚠️ Error: Ingresa un precio válido (número positivo).")
        
        fruits.append({"nombre": nombre, "precio": precio})
        print("✅ Fruta agregada con éxito.\n")
    
    return fruits

def organice_fruits(fruits):
    return sorted(fruits, key=lambda fruit: fruit["precio"], reverse=True)

def mostrar_frutas(fruits):
    if not fruits:
        print("⚠️ No hay frutas registradas aún.")
        return
    
    print("\n🍍 Frutas ordenadas de mayor a menor precio: 🍓")
    for fruit in fruits:
        print(f"{fruit['nombre']}: ${fruit['precio']:.2f}")
    print()

def menu():
    fruits = []
    
    while True:
        print("\n📋 Menú:")
        print("1️⃣ Ingresar 10 frutas")
        print("2️⃣ Ordenar frutas de mayor a menor precio")
        print("3️⃣ Mostrar frutas ordenadas")
        print("4️⃣ Salir")
        
        option = input("🔹 Elige una opción: ").strip()
        
        if option == "1":
            fruits = input_fruits()
        elif option == "2":
            if not fruits:
                print("⚠️ Primero debes ingresar las frutas.")
            else:
                fruits = organice_fruits(fruits)
                print("✅ Frutas ordenadas con éxito.")
        elif option == "3":
            mostrar_frutas(fruits)
        elif option == "4":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida, intenta de nuevo.")

menu()