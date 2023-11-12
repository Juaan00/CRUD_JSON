import funciones    #se llaman al modulo funciones.py
'''
PROYECTO FINAL PROGRAMACIÓN DE COMPUTADORES, GRUPO 15
INTEGRANTES GRUPO [22]:
- Simón Velásquez Silva
- Julián David nieto Rodríguez
- Jorley Snehider Salas Rocha
- Juan Felipe Quiroga Medina

El proyecto se divide en 4 archivos:

(1) - registro.py -> inicia el código. 
(2) - funciones.py -> ejecuta las funciones principales del proyecto.
(3) - funcion_json.py -> se encarga de grabar y extraer la información del archivo JSON.
(4) - color.py -> se encarga de darle color al texto que se imprime en la consola. (No es necesario para el funcionamiento del programa)
(5) - datos.json -> Donde se almacenan los datos.

'''
while True:  #Se crea un ciclo infinito para que el programa se ejecute hasta que el usuario lo decida
    funciones.pantalla()
    try:
        entrada_usuario=int(input(f"\n{'(╯°□°）╯ ┻━┻ Escoja una opción:       ':>45}"))     #se pide la entrada al usuario 
        if entrada_usuario == 0:
            funciones.adios()
            break
        elif entrada_usuario == 1:
            funciones.opcion1()
        elif entrada_usuario == 2:
            funciones.opcion2()
        elif entrada_usuario == 3:
            funciones.opcion3()
        elif entrada_usuario == 4:
            funciones.opcion4()
        else:
            funciones.error_numerico(entrada_usuario)
    except ValueError:
        funciones.error_alfabetico()