import funcion_json     #se llama al modulo funcion_json.py
from color import Color     #se llama al modulo color.py
from subprocess import run     #se llama al modulo subprocess, más rápido que os.system()
from re import compile, match, search   #se llama al modulo re para validar los datos ingresadosq
from platform import system     #se llama al modulo platform para conocer el sistema operativo que se está usando

'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                         __________MODULO FUNCIONES__________                           ╬
╬        Todas las acciones principales del código serán llamadas de este archivo.       ╬
╬                             __________VARIABLES__________                              ╬
╬                Variables vacias que se utilizarán a lo largo del código.               ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

datos={}    #diccionario para almacenar los datos del estudiante
lista_de_materias = []  #lista para almacenar las materias del estudiante
correo = compile("^[a-zA-Z0-9_]+@unal\.edu\.co$")    #expresión regular con el fin de validar el correo institucional del estudiante
código_re = compile("^[0-9]{1,10}$")  #expresión regular con el fin de validar el código del estudiante
nombre_re = compile("^[a-zA-ZáéíóúñÑÁÉÍÓÚüÜ]+\s+[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$") #expresión regular con el fin de validar el nombre del estudiante
materias_re = compile("[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ\s]+$")

'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                    __________FUNCIONES SECUNDARIAS__________                           ╬
╬        Funciones que simplifican acciones repetitivas a lo largo del código            ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

def main():  #función principal
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{'Modulo funciones, este archivo no se ejecutará directamente':>78}{'╬':>11}\n╬{'╬':>89}\n╬{'═'*88}╬")


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
                       
def organizar(dato):        #organiza los datos de manera que se vean de manera ordenada
    espacio=(' '*15)
    for key,value in dato.items():
        print(f"\n{Color.BOLD}{'_'*90}{Color.RESET}\n")
        print(f"{Color.BOLD}Código:{Color.RESET} {value['Código']}\n")
        numero=key
        for key,value in dato[numero].items():
            if type(value) == list:
                print(f"{'':>5}{Color.BOLD}{key}:{Color.RESET} {value[0]}")
                for i in value[1:]:
                    print(f"{'':>5}{'':>10}{i}")  
            elif type(value) == int:
                pass
            else:
                print(f"{'':>5}{Color.BOLD}{key}:{Color.RESET}{'':>2} {value}")
    print(f"\n{Color.BOLD}{'_'*90}{Color.RESET}\n")

def input_alfabetico(): #función para ingresar datos alfabéticos
    '''
    INPUT DATOS ALFABÉTICOS
    '''
    while True:
        try:
            global palabra  #se declara la variable como global para que pueda ser usada en otras funciones
            palabra = None #se declara la variable como None para que no se repita el valor anterior
            palabra = input(f"\n{Color.GREEN}{'':>10}Ingrese el dato:{Color.RESET}    ")
            if palabra:
                break
        except KeyboardInterrupt:
            continue
        except TypeError:
            continue
        finally:    #se ejecuta siempre
            return palabra
      
def input_numerico():   #función para ingresar datos numéricos
    '''
    INPUT DATOS NUMÉRICOS
    '''
    while True:
        try:    #se intenta ejecutar el código
            global número   #se declara la variable como global para que pueda ser usada en otras funciones
            número = None   #se declara la variable como None para que no se repita el valor anterior
            número = int(input(f"\n{Color.GREEN}{'':>10}Ingrese el dato: {Color.RESET}   "))
            if número >= 0: #si el dato es numérico
                break
            else:   #si el dato es negativo
                error(número)
        except ValueError:
            error(número)
        except KeyboardInterrupt:
            error(número)
        except TypeError:
            error(número)
        finally:    #se ejecuta siempre
            return número

def Y_N():  #función para preguntar sí / no
    '''
    IMPUT DATOS BOOLEANOS
    '''
    while True:
        try:
            global escoger_Y_N  #se declara la variable como global para que pueda ser usada en otras funciones
            escoger_Y_N = None  #se declara la variable como None para que no se repita el valor anterior
            escoger_Y_N = input(f"\n{'':>10}{Color.GREEN}Escoja una opción:  Sí(Y)  /{Color.RED}  No(N) {Color.RESET}   ")
            if escoger_Y_N == 'Y' or escoger_Y_N == 'y' or escoger_Y_N == 'N' or escoger_Y_N == 'n':
                break
            else:
                error(escoger_Y_N)
        except ValueError:
            error(escoger_Y_N)
        except KeyboardInterrupt:
            error(escoger_Y_N)
        except TypeError:
            error(escoger_Y_N)
        finally:
            return escoger_Y_N

def organizar_materias(lista_de_materias):   #función para organizar las materias de manera ordenada obedeciendo las margenes de la terminal
    print(f"\n{Color.BOLD}{'_'*90}{Color.RESET}\n")
    print(f"{'Materias registradas:':^90}")
    for i in lista_de_materias:
        print(f"{'':>5}{i}")
    print(f"\n{Color.BOLD}{'_'*90}{Color.RESET}\n")

def materias(lista_de_materias):    #función para ingresar las materias del estudiante
    opciones_1 = ['(1) - Ingresar materias', '(2) - Eliminar materia','(3) - Reingresar materias','(0) - Salir del modulo']
    if lista_de_materias == []:
        while True:
            limpiar()
            print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modulo Inscripción de Materias':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
            if lista_de_materias == []:
                print(f"\nEl estudiante no tiene materias registradas")
            else:
                organizar_materias(lista_de_materias)
            print(f'{Color.RESET}{Color.GREEN}\nDigite las materias del estudiante:{Color.RESET}')
            materias=None
            input_alfabetico()
            materias=palabra
            if match(materias_re, materias):
                lista_de_materias.append(materias)
                print("\n¿Desea incribir otras materias?")
                Y_N()
            else:
                error(materias)
                salida()
                continue
            if escoger_Y_N =='N' or escoger_Y_N == 'n':
                break
            elif escoger_Y_N == 'Y' or escoger_Y_N == 'y':
                continue

    elif lista_de_materias != []:
        while True:
            limpiar()
            print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modulo Inscripción de Materias':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
            organizar_materias(lista_de_materias)
            print(f"Escoja una opción:")
            for i in opciones_1:
                print(f"\n{'':>30}{i}")
            escoger = None
            input_numerico()
            escoger = número
            if escoger == 1:
                while True:
                    limpiar()
                    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modulo Inscripción de Materias':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                    organizar_materias(lista_de_materias)
                    print(f'{Color.RESET}{Color.GREEN}\nDigite las materias del estudiante:{Color.RESET}')
                    materias=None
                    input_alfabetico()
                    materias=palabra
                    if match(materias_re, materias):
                        lista_de_materias.append(materias)
                        print("\n¿Desea incribir otras materias?")
                        Y_N()
                        if escoger_Y_N =='N' or escoger_Y_N == 'n':
                            break
                        elif escoger_Y_N == 'Y' or escoger_Y_N == 'y':
                            continue
            elif escoger  == 2:
                while True:
                    limpiar()
                    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modulo Inscripción de Materias':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                    organizar_materias(lista_de_materias)
                    print(f'{Color.RESET}{Color.GREEN}\nDigite la materia que desea eliminar:{Color.RESET}')
                    eliminar_materia=None
                    input_alfabetico()
                    eliminar_materia=palabra
                    lista_de_materias.remove(eliminar_materia)
                    print(f"\nLa materia {palabra} fue eliminada exitosamente ¿Desea eliminar otra materia?")
                    Y_N()
                    if escoger_Y_N =='N' or escoger_Y_N == 'n':
                        break
                    elif escoger_Y_N == 'Y' or escoger_Y_N == 'y':
                        continue
            elif escoger == 3:
                lista_de_materias.clear()
                while True:
                    limpiar()
                    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modulo Inscripción de Materias':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                    if lista_de_materias == []:
                        print(f"\nEl estudiante no tiene materias registradas")
                    else:
                        organizar_materias(lista_de_materias)
                    print(f'{Color.RESET}{Color.GREEN}\nDigite las materias del estudiante:{Color.RESET}')
                    materias=None
                    input_alfabetico()
                    materias=palabra
                    if match(materias_re, materias):
                        lista_de_materias.append(materias)
                        print("\n¿Desea incribir otras materias?")
                        Y_N()
                        if escoger_Y_N =='N' or escoger_Y_N == 'n':
                            break
                        elif escoger_Y_N == 'Y' or escoger_Y_N == 'y':
                            continue
                        else:
                            error(materias)
                break
            elif escoger == 0:
                break
            else:
                error(escoger)
    return lista_de_materias

def guardar_datos(modificar_datos,dato): #función para guardar los datos modificados
    '''
    Ya que se repite el código para guardar los datos modificados,
    se crea esta función para ahorrar espacio y tiempo.
    '''
    print('\nLos datos quedarán registrados de la siguiente manera, ¿Desea grabarlos así?')
    Y_N()
    if escoger_Y_N == 'Y' or escoger_Y_N == 'y':
        datos.pop(modificar_datos)
        datos.update(dato)
        datos_m=dict(sorted(datos.items()))
        funcion_json.modificar(datos_m)
        print('\n El dato fue modificado exitosamente')
        datos.clear()
    else:
        print('\n El dato no fue modificado')

'''
 ╬════════════════════════════════════════════════════════════════════════════════════════╬
 ╬                                                                                        ╬
 ╬                    __________FUNCIONES PRINCIPALES__________                           ╬
 ╬         Las cuatro funciones principales que definen la naturaleza del código          ╬
 ╬                                                                                        ╬
 ╬════════════════════════════════════════════════════════════════════════════════════════╬
 ╬                                                                                        ╬
 ╬                   __________OPCIÓN #1 AÑADIR REGISTROS__________                       ╬
 ╬                                                                                        ╬
 ╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

def opcion1():  #Añadir Registros
    dato={}
    funcion_json.consultar(datos)
    r = len(datos)
    global registro
    registro = None
    if r == 0:
        registro="0001"
    else:
        registro="0"*(4-len(str(r+1)))+str(r+1)
    while True:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        print(f"{' '*20}Registro de estudiante # {registro}")
        print(f'{Color.GREEN}\nIngrese el código del estudiante:{Color.RESET}')
        código=None
        input_numerico()
        código=número
        if match(código_re,str(código)):
            break
        else:
            print(f"\n{Color.RED} Ingrese un código valido, no puede ser mayor a {Color.SUBRAY}10 digitos.{Color.RESET}")
            salida()
    while True:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        dato.update({registro:{
            'Código':código,
            'Nombre':"N/A",
            'Correo':"N/A",
            'Activo':"N/A",
            'Materias':"N/A"}})
        organizar(dato)
        print(f'{Color.GREEN}\nIngrese el nombre del estudiante:{Color.RESET}')
        nombre=None
        input_alfabetico()
        nombre=palabra
        if match(nombre_re,nombre):
            break
        else:
            print(f"\n{Color.RED}<<Entrada incorrecta>> [{nombre}] debe tener mínimo un nombre y aprellino.{Color.RESET}")
            salida()
    while True:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        dato[registro]['Nombre'] = nombre
        organizar(dato)
        print(f'{Color.GREEN}\nIngrese el correo del estudiante:{Color.RESET}')
        correo_i=None
        input_alfabetico()
        correo_i=palabra
        if match(correo,correo_i):
            dato[registro]['Correo'] = correo_i
            organizar(dato)
            break
        else:
            print(f"\n{Color.RED}<<Entrada incorrecta>> [{correo_i}] no obedece el dominio @unal.edu.co.{Color.RESET}")
            salida()
    while True:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        print(f'{Color.GREEN}\n¿El estudiantes se encuentra activo?{Color.RESET}')
        Y_N()
        if escoger_Y_N == 'Y' or escoger_Y_N == 'y':
            dato[registro]['Activo'] = True
            break
        elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
            dato[registro]['Activo'] = False
            break
        else:
            salida()
    lista_de_materias.clear()
    materias(lista_de_materias)
    dato[registro]['Materias'] = lista_de_materias
    while True:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)       
        print('\nLos datos quedarán registrados de la siguiente manera, ¿Desea grabarlos así?')
        Y_N()
        if escoger_Y_N == 'Y' or escoger_Y_N == 'y':
            datos.update(dato)
            funcion_json.insertar(datos)
            print('\n Los datos han sido registrados de manera satisfactoria')
            datos.clear()
            salida()  
            break
        elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
            print('\n Los datos no fueron registrados')
            salida()
            break
        else:
            salida()
'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                 __________OPCIÓN #2 MODIFICAR REGISTROS__________                      ╬
╬    (1) - Código     (2) - Nombre    (3) - Correo   (4) - Materias   (5) - Activo       ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

def opcion2():  #Modifica Registros
    funcion_json.consultar(datos)
    if not datos:   #si no hay datos registrados
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        print('\nNo hay datos registrados')
    else:   #si hay datos registrados se imprimen en pantalla con un ciclo for anidado para recorrer el diccionario de datos y sus valores
        n_datos = len(datos)
        while True:
            limpiar()
            print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
            print(f"\nHay {n_datos} registro en la base de datos de estudiantes:")
            c_o2_escoger= ["(1) - Código", "(2) - Nombre"]
            print(f"Desea buscar por:")
            for i in c_o2_escoger:
                print(f"\n{'':>30}{i}")
            c_o2 = None
            input_numerico()
            c_o2 = número
            if c_o2 == 1 or c_o2 == 2:
                break
            else:
                error(c_o2)
                salida()
    while True:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        if c_o2 == 1:
            for key,value in datos.items():
                print(f"{Color.GREEN}Registro{Color.RESET} - {key} {'-'*5} {Color.GREEN}Código{Color.RESET} - {value['Código']}")
        elif c_o2 == 2:
            for key,value in datos.items():
                print(f"{Color.GREEN}Registro{Color.RESET} - {key} {'-'*5} {Color.GREEN}Nombre{Color.RESET} - {value['Nombre']}")
        print('\nIngrese el número de registro que desea modificar:')
        modificar_datos=None
        input_numerico()
        modificar_datos="0"*(4-len(str(número)))+str(número)
        if modificar_datos in datos.keys():
            break
        else:
            error(modificar_datos)
            salida()
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
    dato = dict({modificar_datos:datos[modificar_datos]})
    organizar(dato)
    opciones=['(1) - Código','(2) - Nombre', '(3) - Correo', '(4) - Materias','(5) - Activo', '(0) - Volver al menú principal']
    print('\nModificar:')
    for u in opciones:
        print(f"\n{'':>30}{u}")
    while True:
        print('\nEscoja una opción:')
        escoger = None
        input_numerico()
        escoger = número
        if escoger < 0 or escoger > 5:
                error(escoger)
        else:
            break
    if escoger == 1:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        print('\nIngrese el nuevo código del estudiante:')
        while True:
            nuevo_c = None
            input_numerico()
            nuevo_c = número
            if match(código_re,str(nuevo_c)):
                dato[modificar_datos]['Código'] = nuevo_c
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
                organizar(dato)
                guardar_datos(modificar_datos,dato)
                break
            else:
                print(f"\n{Color.RED}<<Entrada incorrecta>> [{nuevo_c}] no es un código válido, no puede pasar de 10 digitos.{Color.RESET}")
    elif escoger == 2:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        print('\nDigite el nuevo nombre del estudiante:')
        while True:
            nuevo_n=None
            input_alfabetico()
            nuevo_n = palabra 
            if match(nombre_re,nuevo_n):
                dato[modificar_datos]['Nombre'] = nuevo_n
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
                organizar(dato)
                guardar_datos(modificar_datos,dato)
                break
            else:
                print(f"\n{Color.RED}<<Entrada incorrecta>> [{nuevo_n}] debe tener mínimo un nombre y aprellino.{Color.RESET}")
    elif escoger == 3:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        print('\nDigite el nuevo correo del estudiante:     ')
        nuevo_co=None
        while True:
            nuevo_co=None
            input_alfabetico()
            nuevo_co=palabra
            if correo.match(nuevo_co):
                dato[modificar_datos]['Correo'] = nuevo_co
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
                organizar(dato)
                guardar_datos(modificar_datos,dato)
                break
            else:
                print(f"\n{Color.RED}<<Entrada incorrecta>> [{nuevo_co}] no obedece el dominio @unal.edu.co.{Color.RESET}")
                error(nuevo_co)
    elif escoger == 4:
        lista_de_materias.clear()
        for i in dato[modificar_datos]['Materias']:
            lista_de_materias.append(i)
        materias(lista_de_materias)
        dato[modificar_datos]['Materias'] = lista_de_materias
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 5:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        print('\nEl estudiantes se encuentra activo? Y/N     ')
        Y_N()
        bol=(escoger_Y_N=='Y' or escoger_Y_N=='y')
        dato[modificar_datos]['Activo'] = bol
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 0:
        print('\nNo se modificó ningún dato')
    salida()
'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                 __________OPCIÓN #3 CONSULTAR REGISTROS__________                      ╬
╬       (1) - Todos los registros    (2) - Un solo registro      (3) - Filtrar           ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

def opcion3():  #Consultar registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
    funcion_json.consultar(datos)
    opciones_consulta=['(1) - Todos los registros','(2) - Un solo registro','(3) - Filtrar', '(0) - Volver al menú principal']
    if not datos:   #si no hay datos registrados
        print('\nNo hay datos registrados')
    else:   #si hay datos registrados se imprimen en pantalla con un ciclo for anidado para recorrer el diccionario de datos y sus valores
        n_datos = len(datos)
        if n_datos == 1:
            print(f"\nHay {n_datos} registro en la base de datos de estudiantes")
        else:
            print(f"\nHay {n_datos} registros en la base de datos de estudiantes")
        print('\nConsultar:')
        for u in opciones_consulta:
            print(f"\n{'':>30}{u}")
        while True:
                print("\nEscoge una opción:") 
                cantidad_datos = None
                input_numerico()
                cantidad_datos = número
                if cantidad_datos == 1 or cantidad_datos == 2 or cantidad_datos == 3 or cantidad_datos == 0:
                    break
                else:
                    error(cantidad_datos)
        if cantidad_datos == 1:
            limpiar()
            print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
            dato=datos
            organizar(dato)
        elif cantidad_datos == 2:
            limpiar()
            print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
            if n_datos == 1:
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                dato=datos
                organizar(dato)
            else:
                print(f"\nHay {n_datos} registro en la base de datos de estudiantes:")
                c_o2_escoger= ["(1) - Código", "(2) - Nombre"]
                print(f"Desea buscar por:")
                for i in c_o2_escoger:
                    print(f"\n{'':>30}{i}")
                while True:
                    c_o2 = None
                    input_numerico()
                    c_o2 = número
                    if c_o2 == 1 or c_o2 == 2:
                        break
                    else:
                        error(c_o2)
                if c_o2 == 1:
                    for key,value in datos.items():
                        print(f"{Color.GREEN}Registro{Color.RESET} - {key} {'-'*5} {Color.GREEN}Código{Color.RESET} - {value['Código']}")
                elif c_o2 == 2:
                    for key,value in datos.items():
                        print(f"{Color.GREEN}Registro{Color.RESET} - {key} {'-'*5} {Color.GREEN}Nombre{Color.RESET} - {value['Nombre']}")
            while True:
                print("\nQué registro desea consultar?: ") 
                num_dato_cons=None
                input_numerico()
                num_dato_cons="0"*(4-len(str(número)))+str(número)
                if num_dato_cons in datos.keys():  #si el dato ingresado está en el diccionario de datos
                    limpiar()
                    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                    dato=dict({num_dato_cons:datos[num_dato_cons]}) #se crea un diccionario con el dato ingresado
                    organizar(dato) #se imprime el dato
                    break
                else:
                    error(num_dato_cons)
        elif cantidad_datos == 3:
            opciones_filtro=['(1) - Materias', '(2) - Activo', '(0) - Volver al menú principal']
            limpiar()
            print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
            for i in opciones_filtro:
                print(f"\n{'':>30}{i}")
            while True:
                filtro_cons = None
                input_numerico()
                filtro_cons = número
                if filtro_cons == 1 or filtro_cons == 2 or filtro_cons == 0:
                    break
                else:
                    error(filtro_cons)
            if filtro_cons == 2:
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                print(f"\n¿Desea consultar los estudiantes (1) - Activos o (2) - Inactivos?")
                while True:
                    activos = None
                    input_numerico()
                    activos = número
                    if activos == 1 or activos == 2:
                        break
                    else:
                        error(activos)
                lista_llaves = []
                dict_llaves = {}
                if activos == 1:
                    f=True
                    for key, values in datos.items():
                        m=search(str(f), str(values['Activo']))
                        if m:
                            lista_llaves.append(key)
                        else:
                            pass
                    for i in lista_llaves:
                        dict_llaves.update({i:datos[i]})
                    organizar(dict_llaves)
                if activos == 2:
                    f=False
                    for key, values in datos.items():
                        m=search(str(f), str(values['Activo']))
                        if m:
                            lista_llaves.append(key)
                        else:
                            pass
                    for i in lista_llaves:
                        dict_llaves.update({i:datos[i]})
                    organizar(dict_llaves)
            elif filtro_cons == 1:
                lista_materias_filtro = []
                for key, values in datos.items():
                    for i in values['Materias']:
                        if i not in lista_materias_filtro:
                            lista_materias_filtro.append(i)
                            lista_materias_filtro.sort()
                        else:
                            pass
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                print(f"\n De la lista, escoja la materia que desea consultar: ")
                organizar_materias(lista_materias_filtro)
                while True:
                    input1 = None
                    input_alfabetico()
                    input1 = palabra
                    if input1 in lista_materias_filtro:
                        jj=input1
                        break
                    else:
                        print('La materia no se encuentra registrada, intente de nuevo')
                        continue
                lista_llaves = []
                dict_llaves = {}
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
                for key, values in datos.items():
                    m=search(str(jj), str(values['Materias']))
                    if m:
                        lista_llaves.append(key)
                    else:
                        pass
                for i in lista_llaves:
                    dict_llaves.update({i:datos[i]})
                organizar(dict_llaves)
        elif cantidad_datos == 0:
            print('\nNo se consultó ningún dato')
    salida()
'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                 __________OPCIÓN #4 ELIMINAR REGISTROS__________                       ╬
╬            (1) - Todos los registros        (2) - Un solo registro                     ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''
def opcion4():  #Eliminar registros
    limpiar()
    opciones_4=['(1) - Todos los registros','(2) - Un solo registro','(0) - Volver al menú principal']
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Eliminar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
    print('\nDesea eliminar:')
    for i in opciones_4:
        print(f"\n{'':>30}{i}")
    while True:
        eliminar_datos = None
        input_numerico()
        eliminar_datos = número
        if eliminar_datos == 1 or eliminar_datos == 2 or eliminar_datos == 0:
            break
        else:
            error(eliminar_datos)
    if eliminar_datos == 1:
        funcion_json.consultar(datos)
        print(f'\n{Color.RED}¿Desea eliminar toda la base de datos? esta acción no se puede revertir.{Color.RESET}')
        Y_N()
        if escoger_Y_N == 'Y' or escoger_Y_N == 'y':  
            datos.clear()
            funcion_json.modificar(datos)
            print('\nLa base de datos ha sido eliminada')
        elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
            print('\nLa base de datos no ha sido eliminada')    
        salida()
    elif eliminar_datos == 2:
        limpiar()
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Eliminar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
        funcion_json.consultar(datos)
        print(f"\nHay {Color.RED}{len(datos.keys())}{Color.RESET} registrados en la base de datos.")
        c_o2_escoger= ["(1) - Código", "(2) - Nombre"]
        print(f"Desea buscar por:")
        for i in c_o2_escoger:
            print(f"\n{'':>30}{i}")
        while True:
            c_o2 = None
            input_numerico()
            c_o2 = número
            if c_o2 == 1 or c_o2 == 2:
                break
            else:
                error(c_o2)
        if c_o2 == 1:
            for key,value in datos.items():
                print(f"{Color.GREEN}Registro{Color.RESET} - {key}{'':>10}{Color.GREEN}Código{Color.RESET} - {value['Código']}")
        elif c_o2 == 2:
            for key,value in datos.items():
                print(f"{Color.GREEN}Registro{Color.RESET} - {key}{'':>10}{Color.GREEN}Nombre{Color.RESET} - {value['Nombre']}")
        print('\nIngrese el número de registro que desea eliminar:')
        while True:
            eliminar=None
            input_numerico()
            eliminar="0"*(4-len(str(número)))+str(número)
            if eliminar in datos.keys():
                limpiar()
                print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Eliminar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
                dato = dict({eliminar:datos[eliminar]})
                organizar(dato)
                print(f'\n{Color.RED}Desea eliminar este dato? esta acción no se puede revertir.{Color.RESET}')
                Y_N()
                if escoger_Y_N == 'Y' or escoger_Y_N == 'y':
                    del(datos[eliminar])
                    nuevos_ordenados = {}
                    r=1 #contador para reordenar los datos
                    for key,values in datos.items():    #se recorren los datos
                        nuevos_ordenados.update({('0'*(4-len(str(r)))+str(r)):values})  #se reordenan los datos
                        r=r+1   #se aumenta el contador
                    funcion_json.modificar(nuevos_ordenados)
                    nuevos_ordenados.clear()
                    datos.clear()
                    print('\nEl dato ha sido eliminado')
                    salida()
                    break
                elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
                    print('\nEl dato no ha sido eliminado')
                    salida()
                    break
            else:
                error(eliminar)
    elif eliminar_datos == 0:
        print('\nNo se eliminó ningún dato')
        salida()

if __name__ == "__main__":  #indica que el modulo no se ejecutará automáticamente a menos que sea llamado <funciones.funcion_que_se_llama()>
    main()  #se llama la función main()