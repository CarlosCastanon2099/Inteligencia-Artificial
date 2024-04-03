class Celula:
    def __init__(self, color):
        self.color = color
        #self.estado = estado 
        
    def esCelulaViva(self):
        return self.color == "ROJOFUERTE" or self.color == "AZULCLARITO"
    

"""    
🦠 Clase Celula Azul 🔵
Atributos: 
    - Ataque
    - Defensa
"""
class CelulaAzul(Celula):
    def __init__(self):
        super().__init__("Azul") 
        self.gen_ataque = False
        self.gen_defensa = False

    def adquirirGenAtaque(self):
        self.gen_ataque = True

    def adquirirGenDefensa(self):
        self.gen_defensa = True

# Celula(AZUL) == CelulaAzul() ,_ ,_
celulanormal = Celula("Azul")
print (type(celulanormal))
print (type(celularara))
