ice_creams = []
id_counter = 1

def make_ice_cream():
    global id_counter
    name = input("Nombre del helado : ").strip()
    description = input("Descripcion del helado : ").strip()

    while True:
        try:
            price = float(input("Precio del helado : ").strip())
            if price < 0:
                raise ValueError("El precio no puede ser negativo")
            break
        except ValueError:
            print("Error: Ingresa un precio valido (numero positivo)")
    
    ice_cream = {
        "ID": id_counter,
        "Name": name,
        "Description": description,
        "Price": price
    }
    ice_creams.append(ice_cream.copy())
    print(f"\n✅ Helado '{name}' agregado con ID {id_counter}\n")
    id_counter += 1

def look_icecreams():
    if not ice_creams:
        print("No hay helados registrados aun")
    else:
        print("Lista de helados : ")
        for ice_cream in ice_creams:
            print(f"ID: {ice_cream['ID']} | Nombre: {ice_cream['Name']} | Descripción: {ice_cream['Description']} | Precio: ${ice_cream['Price']:.2f}")
        print()

def modify_ice_cream():
    look_icecreams()
    try:
        id_modify = int(input("Ingrese el ID del helado a modificar: "))
        for ice_cream in ice_creams:
            if ice_cream["ID"] == id_modify:
                ice_cream["Name"] = input("Nuevo nombre: ").strip() or ice_cream["Name"]
                ice_cream["Description"] = input("Nueva descripción: ").strip() or ice_cream["Description"]
                
                while True:
                    try:
                        price = input("Nuevo precio: ").strip()
                        if price:
                            ice_cream["Precio"] = float(price)
                            if ice_cream["Precio"] < 0:
                                raise ValueError("El precio no puede ser negativo.")
                        break
                    except ValueError:
                        print("Error: Ingresa un precio válido.")
                
                print(f"\n✅ Helado con ID {id_modify} modificado con éxito.\n")
                return
        print("\n⚠️ No se encontró un helado con ese ID.\n")
    except ValueError:
        print("\n⚠️ Error: Ingresa un ID válido.\n")

def delete_ice_cream():
    look_icecreams()
    try:
        id_delete = int(input("Ingrese el ID del helado a eliminar: "))
        for ice_cream in ice_creams:
            if ice_cream["ID"] == id_delete:
                ice_creams.remove(ice_cream)
                print(f"\n❌ Helado con ID {id_delete} eliminado.\n")
                return
        print("\n⚠️ No se encontró un helado con ese ID.\n")
    except ValueError:
        print("\n⚠️ Error: Ingresa un ID válido.\n")

def menu():
    while True:
        print("\n🍦 MENÚ DE GESTIÓN DE HELADOS 🍦")
        print("1️⃣ Crear un helado")
        print("2️⃣ Ver lista de helados")
        print("3️⃣ Modificar un helado")
        print("4️⃣ Eliminar un helado")
        print("5️⃣ Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            make_ice_cream()
        elif opcion == "2":
            look_icecreams()
        elif opcion == "3":
            modify_ice_cream()
        elif opcion == "4":
            delete_ice_cream()
        elif opcion == "5":
            print("\n👋 Saliendo del programa...\n")
            break
        else:
            print("\n⚠️ Opción no válida, intenta de nuevo.\n")
            
menu()
