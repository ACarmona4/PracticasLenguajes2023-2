from Concurso import * 
    
#Método que simula la emisión de los 5 programas en la semana
def emitirProgramas():
    dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES"]
    totalAcumulado = 0
    totalParticipantes = 0
    
    for dia in dias:
        concurso = Concurso()
        concurso.emitirPrograma(dia)
        totalAcumulado += concurso.dineroEntregado
        totalParticipantes += concurso.concursantes.size
        
    print("=" * 140)
    print("INFORMACIÓN DE LA SEMANA:")
    print(f"\nEl total de participantes en la semana fue de: {totalParticipantes}")
    print(f"El total acumulado de la semana es: ${totalAcumulado} pesos\n")
    
if __name__ == '__main__':
    print("\nQUIEN QUIERE SER MILLONARIO - INFORME SEMANAL\n")
    emitirProgramas()
