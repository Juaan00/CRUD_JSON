import funcion_json     #se llama al modulo funcion_json.py
from color import Color     #se llama al modulo color.py
from os import name     #se llama al modulo os para conocer el nombre del os que se está usando
from subprocess import call     #se llama al modulo subprocess, más rápido que os.system()
import re     #se llama al modulo re para usar expresiones regulares
'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                         __________MODULO FUNCIONES__________                           ╬
╬        Todas las acciones principales del código serán llamadas de este archivo.       ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''
datos={}    #diccionario para almacenar los datos del estudiante
lista_de_materias = []  #lista para almacenar las materias del estudiante
correo=re.compile("^[a-zA-Z0-9_]+@{1}+unal.edu.co{1}$")     #expresión regular con el fin de validar el correo institucional del estudiante

'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                    __________FUNCIONES SECUNDARIAS__________                           ╬
╬        Funciones que simplifican acciones repetitivas a lo largo del código            ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

def main():  #función principal
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.CYAN}{Color.BOLD}{'Modulo funciones, este archivo no se ejecutará directamente':>78}{Color.RESET}{'╬':>11}\n╬{'╬':>89}\n╬{'═'*88}╬")

def limpiar():  #función para limpiar la pantalla
    '''
    Por medio de la librería os, se limpia la pantalla de la consola, dependiendo del sistema operativo que se esté usando se ejecuta un comando diferente.
    '''
    if name == 'posix': #nombre que le da python a MacOS/UNIX
        call('clear',shell=True) #opción #1 
        # system('clear') #opción #2 
    else:
        call('cls',shell=True)
        # system('cls') 

def error(variable):   #función para mostrar error de entrada
    '''
    Se muestra un mensaje de error en caso de que el usuario ingrese un dato incorrecto, 
    se divide en 3 tipos de datos: int, str y bool para mostrar el error correspondiente
    '''
    if type(variable) == int:   #si la variable es un entero
        print(f"\n{Color.RED}<<Entrada incorrecta>> [{variable}] no es un dato valido.{Color.RESET}")
    elif type(variable) == str: #si la variable es un string
        print(f"\n{Color.RED}<<Entrada incorrecta>> [{variable}] no es un dato valido.{Color.RESET}")
    elif not variable:  #cuando la variable da un ValueError
        print(f"\n{Color.RED}<<Entrada incorrecta>> ingrese un dato valido.{Color.RESET}")
    salida()
        
def salida():   #función para salir del programa
    '''
    Esta función se encarga de pausar la pantalla y obliga al usuario a presionar una tecla para continuar
    '''
    if name == 'posix': #nombre que le da python a MacOS/UNIX
        call('/bin/bash -c \'read -n 1 -s -r -p "\n<<<Presione una tecla para continuar>>>"\'', shell=True) #no tengo ni puta idea por qué sirve esta mierda :U
        #call('/bin/zsh -c \'read "?\n<<<Presione una tecla para continuar>>>"\'', shell=True)  #opción para zsh pero no sirve
        '''
        comandos utilizados de la terminal bash:
        -c -> ejecuta el comando que se le pase como argumento
        read -> lee la entrada del usuario
        -n 1 -> read regresa después de leer n caracteres
        -s -> modo silencioso, no muestra la entrada del usuario
        -r -> no interpreta los caracteres de escape [\]
        -p -> muestra un mensaje al usuario
        '''
    else:   #opción para windows
        print('\n<<<Presione una tecla para continuar>>>')
        call('pause',shell=True)
    # salir=input('\nDesea volver al modulo principal? Y/N      ')
        
def pantalla(): #función para mostrar la pantalla principal
    limpiar()
    lista=['(1): Crear registros','(2): Modificar registros','(3): Consultar registros', '(4): Eliminar registros', '(0): <Terminar>']
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Programa para el manejo de Estudiantes del Curso':>68}{Color.RESET}{'╬':>21}\n╬{'╬':>89}\n╬{'═'*88}╬")
    for i in lista:
        print(f"\n{'':>30}{i}")
        
def adios():    #función para despedirse
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Programa Finalizado':>53}{Color.RESET}{'╬':>36}\n╬{'╬':>89}\n╬{'═'*88}╬",
'''
                                ╭━━━━-╮
                                ╰┃ ┣▇━▇
                                 ┃ ┃  ╰━▅╮
                                 ╰┳╯ ╰━━┳╯ 
                                  ╰╮ ┳━━╯     
                                 ▕▔▋ ╰╮╭━╮ 
                                ╱▔╲▋╰━┻┻╮╲╱▔▔▔╲
                                ▏  ▔▔▔▔▔▔▔  O O┃        ADIOS!
                                ╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱
                                 ▏╳▕▇▇▕ ▏╳▕▇▇▕
                                 ╲▂╱╲▂╱ ╲▂╱╲▂╱
                            
''')
                        
                        #       ,_,                    ,_,
                        #      (O,O)                  (O,O) 
                        #      (   )                  (   )         opción 2 de adios
                        #   ----"-"---     ADIOS    ---"-"----
    
    
def organizar(dato):        #organiza los datos de manera que se vean de manera ordenada
    for key,value in dato.items():
        print(f"\n{'_'*90}\n")
        print(f'Registro: {key}')
        numero=key
        for key,value in dato[numero].items():
            if type(value) == list:
                print(f"{'':>15}{key}: ", end="")
                for i in value:
                    print(f"{i}",end=", ")
                print()  
            else:
                print(f"{'':>15}{key}: {value}")
    print(f"\n{'_'*90}\n")

def Y_N():  #función para preguntar sí / no
    '''
    Ya que se repite el código para guardar los datos modificados,
    se crea esta función para ahorrar espacio y tiempo.
    '''
    while True:
        try:
            global escoger_Y_N  #se declara la variable como global para que pueda ser usada en otras funciones
            escoger_Y_N = None  #se declara la variable como None para que no se repita el valor anterior
            escoger_Y_N = input('\nPor favor, escoja una opción: Sí(Y)/No(N)    ')
            if escoger_Y_N == 'Y' or escoger_Y_N == 'y' or escoger_Y_N == 'N' or escoger_Y_N == 'n':
                break
            else:
                error(escoger_Y_N)
        except ValueError:
            error(escoger_Y_N)
                
def materias(lista_de_materias):    #función para ingresar las materias del estudiante
    lista_de_materias.clear()
    while True:
        materias=input('\nDigite las materias del estudiante:   ')
        lista_de_materias.append(materias)
        print(f"\n Las materias registradas son: {lista_de_materias}.\n¿Desea incribir otras materias?")
        Y_N()
        if escoger_Y_N =='N' or escoger_Y_N == 'n':
            break

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
        funcion_json.modificar(datos)
        print('\n El dato fue modificado exitosamente')
    else:
        print('\n El dato no fue modificado')

'''
╬════════════════════════════════════════════════════════════════════════════════════════╬
╬                                                                                        ╬
╬                    __________FUNCIONES PRINCIPALES__________                           ╬
╬         Las cuatro funciones principales que definen la naturaleza del código          ╬
╬                                                                                        ╬
╬════════════════════════════════════════════════════════════════════════════════════════╬
'''

def opcion1():  #Añadir Registros
    limpiar()
    while True:
        funcion_json.consultar(datos)
        if len(datos) == 0:
            registro=1
        else:
            registro=len(datos)+1
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        código=int(input('\nDigite el código del estudiante:    '))
        nombre=input('\nDigite el nombre del estudiante:    ')
        while True:
            correo_i=input('\nDigite el correo institucional del estudiante:  ')
            if correo.match(correo_i):
                break
            else:
                print(f"\n{Color.RED}<<Entrada incorrecta>> [{correo_i}] no obedece el dominio @unal.edu.co.{Color.RESET}")
                error(correo)
        materias(lista_de_materias)
        print('\nEl estudiantes se encuentra activo?')
        Y_N()
        bol=(escoger_Y_N=='Y' or escoger_Y_N=='y')
        dato={registro:{'Código':código,'Nombre':nombre,'Correo':correo_i,'Materias':lista_de_materias,'Activo':bol}}
        organizar(dato)       
        print('\nLos datos quedarán registrados de la siguiente manera, ¿Desea grabarlos así?')
        Y_N()
        if escoger_Y_N == 'Y' or escoger_Y_N == 'y':
            datos.update(dato)
            funcion_json.insertar(datos)
            print('\n Los datos han sido registrados de manera satisfactoria')
            datos.clear()  
            break
        elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
            print('\n Los datos no han sido registrados')
    salida()

def opcion2():  #Modifica Registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
    funcion_json.consultar(datos)
    if not datos:   #si no hay datos registrados
        print('\nNo hay datos registrados')
    else:   #si hay datos registrados se imprimen en pantalla con un ciclo for anidado para recorrer el diccionario de datos y sus valores
        n_datos = len(datos)
        if n_datos == 1:
            print(f"\nHay {n_datos} registro en la base de datos de estudiantes")
        else:
            print(f"\nHay {n_datos} registros en la base de datos de estudiantes")
    while True:
        modificar_datos=input('\nEscriba el Registro del Estudiante a quien le desea modificar el registro:     ')
        if modificar_datos:
            break
        else:
            error(modificar_datos)
    dato = dict({modificar_datos:datos[modificar_datos]})
    organizar(dato)
    opciones=['(1) - Código','(2) - Nombre', '(3) - Correo', '(4) - Materias','(5) - Activo', '(0) - Volver al menú principal']
    print('\nModificar:')
    for u in opciones:
        print(f"\n{'':>30}{u}")
    while True:
        escoger = int(input('\nPor favor, escoja la opción que desea modificar del registro.   '))
        try:
            if escoger < 0 or escoger > 5:
                error(escoger)
            else:
                break
        except ValueError:
            error(escoger)
    if escoger == 1:
        nuevo_c = int(input('Digite el nuevo código del estudiante:     '))
        dato[modificar_datos]['Código'] = nuevo_c
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 2:
        nuevo_n = input('\nDigite el nuevo nombre del estudiante:     ')
        dato[modificar_datos]['Nombre'] = nuevo_n
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 3:
        nuevo_co = input ('\nDigite el nuevo correo del estudiante:     ')
        dato[modificar_datos]['Correo'] = nuevo_co
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 4:
        materias(lista_de_materias)
        dato[modificar_datos]['Materias'] = lista_de_materias
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 6:
        print('\nEl estudiantes se encuentra activo? Y/N     ')
        Y_N()
        bol=(escoger_Y_N=='Y' or escoger_Y_N=='y')
        dato[modificar_datos]['Activo'] = bol
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    elif escoger == 0:
        print('\nNo se modificó ningún dato')
    salida()

def opcion3():  #Consultar registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
    funcion_json.consultar(datos)
    opciones_consulta=['(1) - Todos los registros','(2) - Un solo registro']
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
            try:
                cantidad_datos = int(input("\nEscoge una opción:       "))
                if cantidad_datos == 1 or cantidad_datos == 2:
                    break
                else:
                    error(cantidad_datos)
            except ValueError:
                error(cantidad_datos)
        if cantidad_datos == 1:
            dato=datos
            organizar(dato)
        elif cantidad_datos == 2:
            while True:
                try:
                    num_dato_cons = input("\nQué registro desea consultar?: ")
                    if num_dato_cons:
                        dato=dict({num_dato_cons:datos[num_dato_cons]})
                        organizar(dato)
                        break
                    else:
                        error(num_dato_cons)
                except KeyError:
                    error(num_dato_cons)
    salida()

def opcion4():  #Eliminar registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Eliminar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
    eliminar_datos = int(input('\nDesea eliminar todos los archivos (1), o eliminar uno solo (2)?     '))
    if eliminar_datos == 1:
        funcion_json.consultar(datos)
        print('¿Desea eliminar toda la base de datos? esta acción no se puede revertir.')
        Y_N()
        if escoger_Y_N == 'Y' or escoger_Y_N == 'y':  
            datos.clear()
            funcion_json.modificar(datos)
            print('\nLa base de datos ha sido eliminado')
        elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
            print('\nLa base de datos no ha sido eliminado')    
        salida()
    elif eliminar_datos == 2:
        funcion_json.consultar(datos)
        eliminar = input('\nEscriba el número de registro que desea eliminar:      ')
        dato = dict({eliminar:datos[eliminar]})
        organizar(dato)
        print('Desea eliminar este dato? esta acción no se puede revertir.')
        Y_N()
        if escoger_Y_N == 'Y' or escoger_Y_N == 'y':
            del(datos[eliminar])
            funcion_json.modificar(datos)
            print('\nEl dato ha sido eliminado')
        elif escoger_Y_N == 'N' or escoger_Y_N == 'n':
            print('\nEl dato no ha sido eliminado')
        salida()

if __name__ == "__main__":  #indica que el modulo no se ejecutará automáticamente a menos que sea llamado <funciones.funcion_que_se_llama()>
    main()
