import funcion_json     #se llama al modulo funcion_json.py
from color import Color     #se llama al modulo color.py
from os import name, system     #se llama al modulo os
# from subprocess import call

'''
MODULO FUNCIONES
Todas las acciones principales del código serán llamadas de este archivo.
'''
datos={}
lista_de_materias = []

def main():  #función principal
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.CYAN}{Color.BOLD}{'Modulo funciones, este archivo no se ejecutará automaticamente':>78}{Color.RESET}{'╬':>11}\n╬{'╬':>89}\n╬{'═'*88}╬")

def limpiar():  #función para limpiar la pantalla
    '''
    Por medio del modulo os y subprocess de Python se invoca el comando de terminal 'clear' para Mac y 'cls' para Windows
    '''
    if name == 'posix': #nombre que le da python a MacOS
        # call('clear',shell=True) #opción #1 
        system('clear') #opción #2 
    else:
        # call('cls',shell=True)
        system('cls') 

def error_numerico(variable):   #función para mostrar error de entrada
    print(f"\n{Color.RED}<<Entrada incorrecta>> [{variable}] no es un dato valido.{Color.RESET}")
    salida()
    
def error_alfabetico():   #función para mostrar error de entrada
    print(f"\n{Color.RED}<<Entrada incorrecta>> Ingrese un valor numérico. {Color.RESET}")
    salida()
        
def salida():   #función para salir del programa
    if name == 'posix':
        bash = 'read -n 1 -s -r -p "\n<<<Presione una tecla para continuar>>>"' #no tengo ni puta idea por qué sirve esta mierda :U
        system(bash)
    else:
        print('\n<<<Presione una tecla para continuar>>>')
        system('pause')
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
                                ━━━━-╮
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
    
    
def organizar(dato):        #organiza los datos de manera que se vean mejor en pantalla
    for key,value in dato.items():
        print(f"\n{'_'*90}\n")
        print(f'Código: {key}')
        numero=key
        for key,value in dato[numero].items():
            if type(value) == list:
                print(f"{'':>30}{key}: ", end="")
                for i in value:
                    print(f"{i}",end=", ")
                print()  
            else:
                print(f"{'':>30}{key}: {value}")
    print(f"\n{'_'*90}\n")

def materias(lista_de_materias):    #función para ingresar las materias del estudiante
    lista_de_materias.clear()
    while True:
        materias=input('\nDigite las materias del estudiante:   ')
        c=input('\nDesea ingresar otras materias? Y/N   ')
        if c == 'Y' or c == 'y':
            lista_de_materias.append(materias)
            continue
        elif c =='N' or c == 'n':
            lista_de_materias.append(materias)
            break

def guardar_datos(modificar_datos,dato): #función para guardar los datos
    while True:
        try:
            opcion = input('\nDesea dejar guardar este nuevo dato? Y/N    ')
            if opcion == 'Y' or opcion == 'y':
                datos.pop(modificar_datos)
                datos.update(dato)
                funcion_json.modificar(datos)
                print('\n El dato fue modificado exitosamente')
                break
            else:
                error_alfabetico(opcion)
        except ValueError:
            error_alfabetico(opcion)

def opcion1():  #Añadir Registros
    limpiar()
    while True:
        print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Ingreso de Registro':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
        código=int(input('\nDigite el código del estudiante:    '))
        nombre=input('\nDigite el nombre del estudiante:    ')
        correo=input('\nDigite el correo institucional del estudiante:  ')
        materias(lista_de_materias)
        activo=input('\nEl estudiantes se encuentra activo? Y/N     ')
        bol=(activo=='Y')
        datos={código:{'Nombre':nombre,'Correo':correo,'Materias':lista_de_materias, 'Activo':bol}}
        organizar(datos)       
        c1=input('\nLos datos quedarán registrados de la siguiente manera, desea grabarlos así o modificarlos? Grabar(Y)/Devolver(N)     ')
        if c1 == 'Y':
            funcion_json.insertar(datos)
            print('\n Los datos han sido registrados de manera satisfactoria')    
            break
        elif c1 == 'N':
            continue
    salida()

def opcion2():  #Modifica Registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Modificar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
    funcion_json.consultar(datos)
    modificar_datos=input('\nEscriba el código del Estudiante a quien le desea modificar el registro:     ')
    dato = dict({modificar_datos:datos[modificar_datos]})
    organizar(dato)
    opciones=['(1) - Código','(2) - Nombre', '(3) - Correo', '(4) - Materias', '(5) - Activo']
    print('\nModificar:')
    for u in opciones:
        print(f"\n{'':>30}{u}")
    escoger = int(input('\nPor favor, escoja la opción que desea modificar del registro.   '))
    while True:
        try:
            if 0 > escoger or escoger > 6:
                error_numerico(escoger)
            else:
                break
        except ValueError:
            error_alfabetico()
    if escoger == 1:
        nuevo_c = int(input('Digite el nuevo código del estudiante:     '))
        dato = dict({nuevo_c:datos[modificar_datos]})
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
    elif escoger == 5:
        activo=input('\nEl estudiantes se encuentra activo? Y/N     ')
        bol=(activo=='Y')
        dato[modificar_datos]['Activo'] = bol
        organizar(dato)
        guardar_datos(modificar_datos,dato)
    salida()

def opcion3():  #Consultar registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Registros de los Estudiantes':>55}{Color.RESET}{'╬':>34}\n╬{'╬':>89}\n╬{'═'*88}╬")
    funcion_json.consultar(datos)
    opciones_consulta=['(1) - Todos los registros','(2) - Un solo registro']
    print('\nConsultar:')
    for u in opciones_consulta:
        print(f"\n{'':>30}{u}")
    while True:
        try:
            cantidad_datos = int(input("\nEscoge una opción:       "))
            if cantidad_datos == 1:
                dato=datos
                organizar(dato)
                break
            elif cantidad_datos == 2:
                while True:
                    try:
                        num_dato_cons = input("\nQué registro desea consultar?: ")
                        if num_dato_cons:
                            dato=dict({num_dato_cons:datos[num_dato_cons]})
                            organizar(dato)
                            break
                        else:
                            error_numerico(num_dato_cons)
                    except KeyError:
                        error_alfabetico()
                break
            else:
                error_numerico(cantidad_datos)
        except ValueError:
            error_alfabetico()
    salida()

def opcion4():  #Eliminar registros
    limpiar()
    print(f"╬{'═'*88}╬\n╬{'╬':>89}\n{'╬'}{Color.BLUE}{Color.BOLD}{'Eliminar Registro':>50}{Color.RESET}{'╬':>39}\n╬{'╬':>89}\n╬{'═'*88}╬")
    eliminar_datos = int(input('\nDesea eliminar todos los archivos (1), o eliminar uno solo (2)?     '))
    if eliminar_datos == 1:
        funcion_json.consultar(datos)
        accion_e = input('Desea eliminar este dato? esta acción no se puede revertir. Y/N    ')
        if accion_e == 'Y' or accion_e == 'y':  
            datos.clear()
            funcion_json.modificar(datos)
            print('\nEl dato ha sido eliminado')
            salida()
        elif accion_e == 'N' or accion_e == 'n':
            salida()
    elif eliminar_datos == 2:
        funcion_json.consultar(datos)
        eliminar = input('\nEscriba el código del registro que desea eliminar:      ')
        dato = dict({eliminar:datos[eliminar]})
        organizar(dato)
        accion_e = input('Desea eliminar este dato? esta acción no se puede revertir. Y/N    ')
        if accion_e == 'Y' or accion_e == 'y':
            del(datos[eliminar])
            funcion_json.modificar(datos)
            print('\nEl dato ha sido eliminado')
            salida()
        elif accion_e == 'N' or accion_e == 'n':
            salida()

if __name__ == "__main__":  #indica que el modulo no se ejecutará automáticamente a menos que sea llamado <funciones.funcion_que_se_llama()>
    main()