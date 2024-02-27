from googlesearch import search

def buscar_registros(email):
    resultados = []
    try:
        # Realizar una búsqueda en Google con el email como consulta
        query = f'"{email}"'
        for resultado in search(query, num_results=10):  # Cambio aquí
            resultados.append(resultado)
    except Exception as e:
        print(f"Error al buscar: {e}")
    
    return resultados

if __name__ == "__main__":
    email = input("Ingrese su email: ")
    resultados = buscar_registros(email)
    
    if resultados:
        print("El email está registrado en los siguientes sitios web:")
        for resultado in resultados:
            print(resultado)
    else:
        print("No se encontraron resultados para el email proporcionado.")
