import json

# código={
#     '1':{
#         'Nombre': ['Yamile Perdomo'],
#         'Correo': ['yaper@unal.edu.co'],
#         'Materias': ['Introducción', 'Sistemico', 'Cálculo', 'Programación'],
#         }
#     }

# with open('estudiantes.json', 'w') as f:
#     json.dump(código, f)

linea='╬═╬'*25
titulo='Ingreso de Registro'
centrar=(int(len(linea))-int(len(titulo)))/2
centro=' '*int(centrar)

def opcion1():
    print(f'{linea}\n{centro}{titulo}\n{linea}')
    entrada_código=input('\nDigite el código del estudiante: ')
    entrada_nombre=input('\nDigite el nombre del estudiante: ')
    entrada_correo=input('\nDigite el correo institucional del estudiante: ')
    entrada_materias=input('\nDigite las materias del estudiante: ')


    salida=input('me devuelvo?')


opcion1()