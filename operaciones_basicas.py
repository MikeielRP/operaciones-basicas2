"Operaciones basicas"
class OperacionesBasicas:
    "Class"
    def __init__(self ):
        self.resultado=0

    def sumar(self, a , b):
        """Esta función suma dos números"""
        self.resultado=a+b

    def restar( self,a,b):
        """Esta función resta dos números"""
        self.resultado=a-b

    def obtener_resultado(self):
        """Esta funcion obtiene el resultado"""
        return self.resultado


class CalculadoraPromedio:
    """Clasess"""
    def __init__( self, valores ):
        """Constructore"""
        self.valores=valores

    def calcular_promedio(self):
        """Calcula el promedio"""
        suma=0
        for valor in self.valores:
            suma+=valor
        promedio=suma/len(self.valores)
        return promedio

    def resultado (self):
        """Calcula el promedio"""
        r="Resultado"
        return r


# Variables globales
NUMEROS =[1,2,3,4,5]
NUM1 =10
NUM2=20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1,NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1,NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedios=calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedios}")
