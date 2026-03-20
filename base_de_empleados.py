import json

empleados = []

def agregar_empleado(): #funcion para agregar un nuevo libro

    nombre = input("Nombre del empleado: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío")
        return

    for emp in empleados:
        if emp["nombre"] == nombre:
            print("Este empleado ya existe")
            return

    while True:
        try:
            edad = int(input("Edad del empleado: "))
            if edad <= 18:
                print("La edad debe ser mayor a 18 años")
            else:
                break
        except ValueError:
            print("Edad invalida")

    puesto = input("Area asignada: ")

    while True:
        try:
            salario = int(input("Salario designado: "))
            if salario <= 5999:
                print("El salario debe ser de minimo $6,000 Mxn")
            else:
                break
        except ValueError:
            print("Salario invalido")

    empleado = {
    "nombre" : nombre,
    "edad" : edad,
    "puesto" : puesto,
    "salario" : salario
    }

    empleados.append(empleado)
    guardar_empleados()
    print("empleado agregado")

def mostrar_empleados(): #funcion
    print("\nEmpleados:")
    if not empleados:
        print("No hay empleados registrados")
        return
    
    for i, empleado in enumerate(empleados, 1):
        print(f'{i}. {empleado["nombre"]} - {empleado["edad"]} - {empleado["puesto"]} - ${empleado["salario"]:,} MXN')

def actualizar_empleados():
    if not empleados:
        print("No hay empleados")
        return

    mostrar_empleados()
    try:
        indice = int(input("Numero del empleado a actualizar: ")) - 1
        empleado = empleados[indice]
        
        empleado["edad"] = int(input("Nueva edad: "))
        empleado["puesto"] = input("Nuevo puesto: ")

        while True:
            try:
                salario = int(input("Nuevo salario: "))
                if salario < 6000:
                    print("El salario minimo tiene que ser $6,000 MXN")
                else:
                    empleado["salario"] = salario
                    break
            except ValueError:
                print("Salario invalido")
        guardar_empleados()
        print("Empleado actualizado")
    except (ValueError, IndexError):
        print("Numero de empleado invalido")

def guardar_empleados():

    with open("empleados.json", "w") as archivo:
        json.dump(empleados, archivo, indent=4, ensure_ascii=False)

def cargar_empleados():

    global empleados
    try:
        with open("empleados.json", "r") as archivo:
            empleados = json.load(archivo)
    except FileNotFoundError:
        empleados= []

def eliminar_empleado():
    if not empleados:
        print("No hay empleados")
        return
    mostrar_empleados()
    try:
        indice = int(input("Numero del empleado a eliminar: ")) - 1
        empleado = empleados[indice]
 
        confirmar = input(f"Seguro que deseas eliminar a {empleado['nombre']}? (s/n): ")
        if confirmar.lower() == "s":
            empleados.pop(indice)
            guardar_empleados()
            print("Empleado eliminado")
        else:
            print("Operacion cancelada")
    except (ValueError, IndexError):
        print("Numero de empleado invalido")

def salir():

    print("Cerrando programa")
    exit()

def main():
    opciones = {
        "1" : agregar_empleado,
        "2" : mostrar_empleados,
        "3" : actualizar_empleados,
        "4" : eliminar_empleado,
        "5" : salir
    }
    while True:
        print("\n --- Empleados ---")
        print("1. agregar empleado")
        print("2. mostrar empleados")
        print("3. actualizar empleados")
        print("4. eliminar empleado")
        print("5. salir")
        opcion = input("Elige una opcion: ")
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("opcion invalida")

if __name__ == "__main__":
    cargar_empleados()
    main()