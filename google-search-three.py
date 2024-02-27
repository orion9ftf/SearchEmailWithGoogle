import requests
from bs4 import BeautifulSoup
import time

def buscar_registros(email):
    resultados = []
    intentos_maximos = 5  # Número máximo de intentos
    intentos = 0
    
    while intentos < intentos_maximos:
        try:
            # Realizar una solicitud a Google con el email como consulta
            url = f"https://www.google.com/search?q={email}"
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)
            
            # Verificar si la solicitud fue exitosa
            if response.status_code == 200:
                # Parsear el contenido HTML
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Encontrar todos los enlaces en los resultados de búsqueda
                enlaces = soup.find_all('a')
                
                # Agregar los enlaces a la lista de resultados
                for enlace in enlaces:
                    resultados.append(enlace.get('href'))
                
                # Si no hay excepciones, salir del bucle
                break
        
        except Exception as e:
            print(f"Error al buscar: {e}")
            
            # Esperar antes de intentar nuevamente
            tiempo_espera = 10  # Tiempo de espera en segundos
            print(f"Esperando {tiempo_espera} segundos antes de intentar nuevamente...")
            time.sleep(tiempo_espera)
            
            # Incrementar el contador de intentos
            intentos += 1
            continue
    
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

