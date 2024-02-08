class Silla:
    color ="Cafe"
    altura = "1.25"
    peso = 1
    
    def __init__(self, color, material, patas):
        self.color = color
        self.material = material
        self.patas = patas
    
    def reclinar (self):
        return True
    
silla_Odontologo = Silla('Naranja','Aluminio',4)
#silla_Odontologo.color = 'Verde'

print(silla_Odontologo.reclinar())
print(silla_Odontologo.color)
print(silla_Odontologo.patas)
