from subprocess import call

color1='\033[0;32m'
color2='\033[0;97m'
bold='\033[1m'
normal='\033[5m'
linea="╬═╬"*25
nombre='Programa para el manejo de Estudiantes del Curso'
espacio=(int(len(linea))-int(len(nombre)))/2
centrar=' '*int(espacio)
lista={(1):'Crear registros',(2):'Modificar registros',(3):'Consultar registros', (4):'Eliminar registros', (0):'<Terminar>'}

def abrir():
    call(['python','opciones.py'])

if __name__ == "__main__":
    while True:
        print("\033c", end="")
        print(f'{linea}{color1}\n{bold}{centrar}{nombre}\n{color2}{linea}')
        for key,value in lista.items():
            espacio2=(int(len(linea))-3-int(len(value)))/2
            centrar2=' '*int(espacio2)
            print(f'\n {centrar2}{key}. {value}')
        try:
            entrada1=int(input(f'\n{color1} (╯°□°）╯ ┻━┻ Escoja una opción: {color2}'))
            if entrada1 == 0:
                print('''
    ═══════•◉•════════
        ▂▄▄▓▄▄▂
        ◢◤ █▀▀████▄▄▄▄◢◤
        █▄ █ █▄ ███▀▀▀▀▀▀▀╬
        ◥█████◤
        ═╩══╩═
        ╬═╬
        ╬═╬
        ╬═╬
        ╬═╬ Chau, desinstalen.
        ╬═╬ ●/
        ╬═╬/▌
        ╬═╬/ 
        ''')
                break
            elif (entrada1 == 1 or entrada1 == 2 or entrada1 == 3 or entrada1 == 4):
                abrir()
            else:
                print('entrada incorrecta')
        except ValueError:
            print('entrada incorrecta')
