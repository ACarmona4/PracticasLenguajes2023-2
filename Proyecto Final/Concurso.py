from Lista import *
from Concursante import *
import random

class Concurso():
    
    def __init__(self):
        self.concursantes = Lista()
        self.dineroEntregado = 0
        
    #Método que crea los concursantes para la ronda de clasificación
    def registrarConcursantes(self):
        for i in range(1, 7):
            self.concursantes.insertar(Concursante(i))
            
    #Método que selcecciona los concursantes que pasan al concurso
    def rondaClasificatoria(self):
        mejorConcursante = self.concursantes.first
        mejorTiempo = mejorConcursante.data.tiempoInicial
        segundoConcursante = None
        segundoTiempo = float('inf') 

        actual = self.concursantes.first.siguiente
        while actual:
            if actual.data.tiempoInicial < mejorTiempo:
                segundoConcursante = mejorConcursante
                segundoTiempo = mejorTiempo
                mejorTiempo = actual.data.tiempoInicial
                mejorConcursante = actual
            elif actual.data.tiempoInicial < segundoTiempo:
                segundoTiempo = actual.data.tiempoInicial
                segundoConcursante = actual
            actual = actual.siguiente

        mejorConcursante.data.clasificacion = "Si"
        segundoConcursante.data.clasificacion = "Si"
        return mejorConcursante, segundoConcursante
    
    #Método que otorga el dinero si se retira
    def retirarse(self, concursante):
        preguntasRespondidas = concursante.data.ultimaPreguntaRespondida
        
        if preguntasRespondidas == 0:
            pass
        elif preguntasRespondidas == 1:
            concursante.data.premioObtenido = 100,000
        elif preguntasRespondidas == 2:
            concursante.data.premioObtenido = 200000
        elif preguntasRespondidas == 3:
            concursante.data.premioObtenido = 300000
        elif preguntasRespondidas == 4:
            concursante.data.premioObtenido = 500000
        elif preguntasRespondidas == 5:
            concursante.data.premioObtenido = 1000000
        elif preguntasRespondidas == 6:
            concursante.data.premioObtenido = 2000000
        elif preguntasRespondidas == 7:
            concursante.data.premioObtenido = 3000000
        elif preguntasRespondidas == 8:
            concursante.data.premioObtenido = 5000000
        elif preguntasRespondidas == 9:
            concursante.data.premioObtenido = 7000000
        elif preguntasRespondidas == 10:
            concursante.data.premioObtenido = 10000000
        elif preguntasRespondidas == 11:
            concursante.data.premioObtenido = 12000000
        elif preguntasRespondidas == 12:
            concursante.data.premioObtenido = 20000000
        elif preguntasRespondidas == 13:
            concursante.data.premioObtenido = 50000000
        elif preguntasRespondidas == 14:
            concursante.data.premioObtenido = 100000000
        elif preguntasRespondidas == 15:
            concursante.data.premioObtenido = 300000000
        
        if preguntasRespondidas < 15:
            concursante.data.estado = f'Se retiró en la pregunta {preguntasRespondidas+1}'
        else:
            concursante.data.estado = f'Respondió todas las preguntas correctamente!'
          
    #Método que otroga el dinero si falla la pregunta
    def pierde(self, concursante):
        preguntasRespondidas = (concursante.data.ultimaPreguntaRespondida)

        if preguntasRespondidas < 5:
            concursante.data.premioObtenido = 0
        elif preguntasRespondidas < 10:
            concursante.data.premioObtenido = 1000000
        elif preguntasRespondidas < 15:
            concursante.data.premioObtenido = 10000000
        elif preguntasRespondidas == 15:
            concursante.data.premioObtenido = 300000000
        else:
            pass
        
        if preguntasRespondidas < 15:
            concursante.data.estado = f'Falló en la pregunta {preguntasRespondidas+1}'
        else:
            concursante.data.estado = f'Respondió todas las preguntas correctamente!'
        
    #Método que simula el uso de comodines
    def usarComodin(self, concursante):
        listaComodines = ["50/50", "Llamada a un amigo", "Ayuda del publico"]
        comodinesUsados = 0
        
        if concursante.data.ultimaPreguntaRespondida < 3:
            concursante.data.comodinesUtilizados.append(random.choice(listaComodines))
        else:
            while comodinesUsados < 3:
                comodin = random.choice(listaComodines)
                if comodin not in concursante.data.comodinesUtilizados:
                    concursante.data.comodinesUtilizados.append(comodin)
                comodinesUsados += 1
                
    #Método que calcula el dinero entregado en el concurso  
    def premioTotal(self):
        actual = self.concursantes.first
        while actual:
            self.dineroEntregado += actual.data.premioObtenido
            actual = actual.siguiente
        
    #Método que simula la ronda de preguntas
    def rondaFinal(self):
        primerConcursante, segundoConcursante = self.rondaClasificatoria()
        primerConcursante.data.ultimaPreguntaRespondida = (random.randint(0, 15))
        segundoConcursante.data.ultimaPreguntaRespondida = (random.randint(0, 15))
        
        probabilidad = random.randint(1, 4)
        if probabilidad == 1:
            self.usarComodin(primerConcursante)
            self.retirarse(primerConcursante)
            self.usarComodin(segundoConcursante)
            self.pierde(segundoConcursante)
        elif probabilidad == 2:
            self.usarComodin(primerConcursante)
            self.pierde(primerConcursante)
            self.usarComodin(segundoConcursante)
            self.retirarse(segundoConcursante)
        elif probabilidad == 3:
            self.usarComodin(primerConcursante)
            self.retirarse(primerConcursante)
            self.usarComodin(segundoConcursante)
            self.retirarse(segundoConcursante)
        else:
            self.usarComodin(primerConcursante)
            self.pierde(primerConcursante)
            self.usarComodin(segundoConcursante)
            self.pierde(segundoConcursante)
            
        self.premioTotal()
        
    #Método que muestra la información del día
    def informacionDia(self, nombreDia):
        print("=" * 140)
        print(f"INFORMACIÓN DÍA {nombreDia}\nPARTICIPANTES:\n")
        self.concursantes.mostrar()
        print(f"\nEl total del dinero entregado en el día es: ${self.dineroEntregado} pesos\n")
    
    #Metódo que simula un día de emisión
    def emitirPrograma(self, dia):
        self.registrarConcursantes()
        self.rondaFinal()
        self.informacionDia(dia)

  


            
            
            



     