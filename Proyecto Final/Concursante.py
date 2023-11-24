import random
from Persona import Persona

class Concursante(Persona):

    def __init__(self, id):
        
        super().__init__()
        self.id = id
        self.clasificacion = "No"
        self.estado = 'No clasificó a la ronda final'
        self.tiempoInicial = random.randint(25, 180)
        self.premioObtenido = int(0)
        self.ultimaPreguntaRespondida = 0
        self.comodinesUtilizados = []
        
    def __str__(self):
        if self.clasificacion == "Si":
            return f'{self.nombre} ID ({self.id}). Tiempo en responder pregunta inicial: {self.tiempoInicial} segundos. Premio obtenido: ${self.premioObtenido} pesos.\nUltima pregunta respondida: {self.ultimaPreguntaRespondida}. Comodines utilizados: {self.comodinesUtilizados}. {self.estado}'
        else:
            return f'{self.nombre} ID ({self.id}). Tiempo en responder pregunta inicial: {self.tiempoInicial} segundos. {self.estado}'
