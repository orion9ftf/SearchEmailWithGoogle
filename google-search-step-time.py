from googlesearch import search
import time

def buscar_registros(email):
    resultados = []
    intentos_maximos = 5  # Número máximo de intentos
    intentos = 0
    
    while intentos < intentos_maximos:
        try:
            # Realizar una búsqueda en Google con el email como consulta
            query = f'"{email}"'
            for resultado in search(query, num_results=10):
                resultados.append(resultado)
            
            # Si no hay excepciones, salir del bucle
            break
        
        except Exception as e:
            print(f"Error al buscar: {e}")
            
            # Si el error es 429 (Too Many Requests), esperar antes de intentar nuevamente
            if '429' in str(e):
                tiempo_espera = 10  # Tiempo de espera en segundos
                print(f"Esperando {tiempo_espera} segundos antes de intentar nuevamente...")
                time.sleep(tiempo_espera)
                
                # Incrementar el contador de intentos
                intentos += 1
                continue
            
            # Otro tipo de error, salir del bucle
            else:
                break
    
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
