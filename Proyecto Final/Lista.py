
class Lista():

    def __init__(self):
        self.first = None 
        self.last = None 
        self.size = 0 

    #Método para verificar si la lista está vacía
    def empty(self):
        return self.first == None

    #Método para insertar elementos al final de la lista
    def insertar(self,data):
        newNode = Nodo(data)

        if self.empty():
            self.first = self.last = newNode
        else:
            self.last.siguiente = newNode
            self.last = newNode
            newNode.siguiente = None
        self.size += 1

    # Método mostrar los elementos de la lista
    def mostrar(self):
        actual = self.first

        while actual:
            print(actual.data)
            print("-" * 140)
            actual = actual.siguiente

class Nodo():
    def __init__(self, data, siguiente = None):
        self.data = data 
        self.siguiente = siguiente

    def __str__(self):
        return self.data

class Data():
    def __init__(self, concursante):
        self.concursante = concursante

    def __str__(self):
        return f'Datos concursante: {self.concursante}'
