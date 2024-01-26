import sqlite3

def buscar_cliente_con_cuotas(documento):
    # Conectar con la base de datos
    conexion = sqlite3.connect('BaseDatos.db')
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para seleccionar la información del cliente por su documento
    cursor.execute("SELECT * FROM Clientes WHERE Documento = ?", (documento,))
    cliente = cursor.fetchone()  # Obtener el primer cliente que coincida con el documento
    
    if cliente:
        # Obtener las cuotas del cliente
        cursor.execute("SELECT * FROM Cuotas WHERE id_cliente = ?", (cliente[0],))
        cuotas = cursor.fetchall()
    else:
        cuotas = []

    # Cerrar la conexión con la base de datos
    conexion.close()

    return cliente, cuotas

# Ejemplo de uso
documento_buscar = 45087673  # Documento del cliente que deseas buscar
cliente_encontrado, cuotas_cliente = buscar_cliente_con_cuotas(documento_buscar)

if cliente_encontrado:
    print("Cliente encontrado:")
    print("ID:", cliente_encontrado[0])
    print("Apellido:", cliente_encontrado[1])
    print("Nombre:", cliente_encontrado[2])
    print("Documento:", cliente_encontrado[3])
    print("Correo:", cliente_encontrado[4])
    print("Fecha de Nacimiento:", cliente_encontrado[5])
    print("Teléfono:", cliente_encontrado[6])

    if cuotas_cliente:
        print("\nCuotas del cliente:")
        for cuota in cuotas_cliente:
            print("ID de Cuota:", cuota[0])
            print("Haber:", cuota[1])
            print("Plan:", cuota[2])
            print("Profesor:", cuota[3])
            print("Fecha:", cuota[4])
            print("Vencimiento:", cuota[5])
            print("ID de Cliente:", cuota[6])
            print("ID de Programa:", cuota[7])
            print()  # Espacio entre cuotas
    else:
        print("\nEl cliente no tiene cuotas registradas.")
else:
    print("Cliente no encontrado.")
