import random
class Persona():
    def __init__(self):
        
        #Parametros para crear el concursante
        listaNombres = ["Juan", "Jose", "Daniel", "Alejandro", "Tomas", "Roberto", "Carlos", "Miguel", "David", "Ricardo", "Wilmer", "Agustin", "Mateo", "Pablo", "Andres", "German", "Mario", "Luis"]
        listaApellidos = ["Char", "Diaz", "Carmona", "Cardona", "Duque", "Rodriguez", "Lopez", "Restrepo", "Salinas", "Ospina", "Acevedo", "Roldan", "Cadavid", "Perez", "Sanchez", "Cifuentes", "Gutierrez" ]
        
        self.nombre = random.choice(listaNombres) + " " + random.choice(listaApellidos)
        self.edad = random.randint(18, 60)
