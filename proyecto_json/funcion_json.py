import json     #Se importa la librería JSON
'''
MODULO DE FUNCIONES JSON
Aquí se encargará de Insertar, Extraer y Modificar los datos que se almacenan en el JSON
'''
datos_estudiante={}
def main(): #Función principal
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{'Módulo de funciones JSON, este archivo no se ejecutará directamente':>78}{'╬':>11}\n╬{'╬':>89}\n╬{'═'*88}╬")

def insertar(datos):    #Función que inserta los datos en el JSON
    with open("datos.json", encoding='utf-8') as registro_previo:
        datos_estudiante = json.load(registro_previo)
        datos_estudiante.update(datos)
    with open("datos.json", "w", encoding='utf-8') as dato_agregado:
        json.dump(datos_estudiante, dato_agregado, indent=2)
        
def consultar(datos):   #Función que consulta los datos del JSON
    with open("datos.json", 'r', encoding='utf-8') as registro_previo:
        datos_estudiante = json.load(registro_previo)
        datos.update(datos_estudiante)

def modificar(datos):   #Función que modifica los datos del JSON
    with open("datos.json", 'w', encoding='utf-8') as registro_previo:
        json.dump(datos,registro_previo, indent=2)
        
if __name__ == "__main__":  #Se ejecuta la función principal
    main()
