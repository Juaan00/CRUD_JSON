# Proyecto_Final

El proyecto se divide en 4 archivos:

- registro.py → ejecuta el código y llama a las funciones del código.
- funciones.py → se encuentran las funciones del proyecto.
- función_json.py → se encarga de grabar, consultar y modificar el JSON.
- color.py → se encarga de darle color al texto que se imprime en la consola. (No es necesario para el programa).
- datos.json → almacena la base de datos de los estudiantes.


IMPORTANTE: 

Cuando descarguen el zip y editen el código, vuelvan a comprimir la carpeta antes de subir la nueva versión y subirla otra vez al drive.
Prácticamente, fusioné la versión 3 y 2, se me ocurrió dejar “registro.py” solamente con el <while True:>, también en “función_json.py” dejé únicamente las funciones de grabar, consultar y modificar. En el archivo “funciones.py” es donde se edita el diccionario que se extrae de JSON, me parece que queda más interesante ahí. Creo que se puede seguir optimizando. Pero igual es una propuesta que dejo.
Encontré información sobre el if__name__==”__main__”:  encontré lo siguiente: una construcción común en los scripts de Python. Aquí está lo que hace:
Cuando ejecutas un script de Python, Python asigna el nombre "__main__" al script. Esto significa que si ejecutas el script directamente, la condición if __name__ == "__main__": será verdadera.
Por otro lado, si importas el script como un módulo en otro script, Python asignará el nombre del archivo (sin la extensión .py) al script. En este caso, la condición if __name__ == "__main__": será falsa.
Por lo tanto, el código que se coloca dentro del bloque if __name__ == "__main__": sólo se ejecutará si el script se ejecuta directamente. Si el script se importa como un módulo, ese código no se ejecutará.
Esto es útil cuando quieres que un script se comporte de manera diferente dependiendo de si se ejecuta directamente o se importa como un módulo. Por ejemplo, puedes poner pruebas o código de demostración en el bloque if __name__ == "__main__": para que no se ejecute cuando el script se importa como un módulo.

Por lo que entiendo es para indicar que el archivo es un módulo, entonces dejé una función “main” aparte que cuando se ejecuta indica la naturaleza del archivo. Menos el de registro que es el que ejecuta todo.

Agregué el archivo “Color.py” de la carpeta de archivos de Programación.
Toca ver si el código se rige bajo los requisitos que dio el profesor.
Si tienen una propuesta de agregar o quitar, bien pueda. Mientras obedezcan los requisitos del proyecto. Pero crean la nueva versión y traten de documentar os cambios realizados.
Las funciones de limpiar la terminal y pausar hasta que <Presione cualquier tecla> funcionan bien en MacOS/LINUX. Por fa vean qué protocolos funcionan en Windows y los agregan.
Lo del ejecutable traigo la propuesta el miércoles, pero igual si encuentran documentación o descubren cómo se hace, pues bien.


