import funciones
'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬       __________PROYECTO FINAL PROGRAMACIÓN DE COMPUTADORES, GRUPO 15__________        ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬

INTEGRANTES GRUPO [22]:
- Simón Velásquez Silva
- Jorley Snehider Salas Rocha
- Juan Felipe Quiroga Medina

El proyecto se divide en 5 archivos:

(1) - registro.py -> inicia el código. 
(2) - funciones.py -> ejecuta las funciones principales del proyecto.
(3) - funcion_json.py -> se encarga de grabar y extraer la información del archivo JSON.
(4) - color.py -> se encarga de darle color al texto que se imprime en la consola. (No es necesario para el funcionamiento del programa)
(5) - datos.json -> Donde se almacenan los datos.
'''
def programa_registro():
    #funciones.cambiar_tamaño_terminal()    
    while True:
        funciones.pantalla()
        funciones.input_numerico()
        entrada_usuario=funciones.número
        if entrada_usuario == 1:
            funciones.opcion1()
        elif entrada_usuario == 2:
            funciones.opcion2()
        elif entrada_usuario == 3:
            funciones.opcion3()
        elif entrada_usuario == 4:
            funciones.opcion4()
        elif entrada_usuario == 0:
            funciones.adios()
            break
        else:
            funciones.error(entrada_usuario)
if __name__ == "__main__":
    programa_registro()
