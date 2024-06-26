import funciones
import funciones_secundarias
'''
El proyecto se divide en 5 archivos:
(1) - registro.py -> inicia el código. 
(2) - funciones.py -> ejecuta las funciones principales del proyecto.
(3) - funcion_json.py -> se encarga de grabar y extraer la información del archivo JSON.
(4) - color.py -> se encarga de darle color al texto que se imprime en la consola.
(5) - datos.json -> Donde se almacenan los datos.
'''
def programa_registro():
    while True:
        funciones_secundarias.pantalla()
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
            funciones_secundarias.adios()
            break
        elif entrada_usuario == None:
            funciones_secundarias.salida()
        else:
            funciones_secundarias.error(entrada_usuario)
            funciones_secundarias.salida()
if __name__ == "__main__":
    programa_registro()
