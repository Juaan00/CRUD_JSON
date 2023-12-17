from subprocess import run 
from platform import system 
from color import Color

def funciones_secundarias():
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{'Modulo funciones secundarias, este archivo no se ejecutará directamente':>78}{'╬':>11}\n╬{'╬':>89}\n╬{'═'*88}╬")

def limpiar():  #función para limpiar la pantalla
    if system() == 'Linux' or system() == 'Darwin': #nombre que le da python a MacOS/UNIX
        return run('clear',shell=True)
    else:
        return run('cls',shell=True)
    
def error(variable):   #función para mostrar error de entrada
    '''
    Se muestra un mensaje de error en caso de que el usuario ingrese un dato incorrecto, 
    se divide en 3 tipos de datos: int, str y bool para mostrar el error correspondiente
    '''
    if type(variable) == int:   #si la variable es un entero
        return print(f"\n{Color.RED}<<Entrada incorrecta>> [{variable}] no es un dato valido.{Color.RESET}")
    elif type(variable) == str: #si la variable es un string
        return print(f"\n{Color.RED}<<Entrada incorrecta>> [{variable}] no es un dato valido.{Color.RESET}")
    elif not variable:  #cuando la variable da un ValueError
        return print(f"\n{Color.RED}<<Entrada incorrecta>> ingrese un dato valido.{Color.RESET}")

        
def salida():   #función para salir del programa
    if system() == 'Linux' or system() == 'Darwin': #opción para linux y MacOS
        return run('/bin/bash -c \'read -n 1 -s -r -p "\n<<<Presione una tecla para continuar>>>"\'', shell=True), print() 
    else:   #opción para windows
        return run('pause',shell=True)
        
def pantalla(): #función para mostrar la pantalla principal
    limpiar()
    lista=['(1): Crear registros','(2): Modificar registros','(3): Consultar registros', '(4): Eliminar registros', '(0): <Terminar>']
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Programa para el manejo de Estudiantes del Curso':>68}{Color.RESET}{'╬':>21}\n╬{'╬':>89}\n╬{'═'*88}╬")
    for i in lista:
        print(f"\n{'':>33}{i}")
    print(f"\n{Color.GREEN}{'-> Escoja una opción <-':^90}{Color.RESET}")

def adios():    #función para despedirse
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Programa Finalizado':>53}{Color.RESET}{'╬':>36}\n╬{'╬':>89}\n╬{'═'*88}╬")
    print(f"{Color.BOLD}{Color.RED}\n\n\n\n{'¡ADIOS!':^90}{Color.RESET}")
    salida()
    limpiar()

if __name__ == "__main__":
    funciones_secundarias()