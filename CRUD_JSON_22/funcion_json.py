from json import load, dump     #Se importa la librería JSON
'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                   __________MODULO DE FUNCIONES JSON__________                         ╬
╬               Aquí se encargará de Insertar, Consultar y Modificar                     ╬
╬                       los datos que se almacenan en el JSON                            ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''
datos_estudiante={}
def main(): #Función principal
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{'Módulo de funciones JSON, este archivo no se ejecutará directamente':>78}{'╬':>11}\n╬{'╬':>89}\n╬{'═'*88}╬")

def insertar(datos):    #Función que inserta los datos en el JSON
    with open("datos.json", encoding='utf-8') as registro_previo:
        datos_estudiante = load(registro_previo)
        datos_estudiante.update(datos)
    with open("datos.json", "w", encoding='utf-8') as dato_agregado:
        dump(datos_estudiante, dato_agregado, indent=2, ensure_ascii=False)
        
def consultar(datos):   #Función que consulta los datos del JSON
    with open("datos.json", 'r', encoding='utf-8') as registro_previo:
        datos_estudiante = load(registro_previo)
        datos.update(datos_estudiante)

def modificar(datos_m):   #Función que modifica los datos del JSON
    with open("datos.json", 'w', encoding='utf-8') as registro_previo:
        dump(datos_m,registro_previo, indent=2, ensure_ascii=False)
        
if __name__ == "__main__":  #Se ejecuta la función principal
    main()
