class Variables:
    datos={}   
    lista_de_materias = [] 
    lista_llaves = []
    dict_llaves = {}
    correo = "^[a-zA-Z0-9_]+@unal\.edu\.co$"  
    código_re = "^[0-9]{1,10}$"  
    nombre_re = "^[a-zA-ZáéíóúñÑÁÉÍÓÚüÜ]+\s+[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$"
    materias_re = "[a-zA-Z0-9áéíóúÁÉÍÓÚüÜñÑ\s]+$"