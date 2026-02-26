class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if not numeros:
            return 0

        ordenados = sorted(numeros)
        n = len(ordenados)
        medio = n // 2

        if n % 2 == 0:
            return (ordenados[medio - 1] + ordenados[medio]) / 2
        return float(ordenados[medio])
    
    def moda(self, numeros):
        if not numeros:
            return None

        frecuencia = {}
        for n in numeros:
            frecuencia[n] = frecuencia.get(n, 0) + 1

        max_frecuencia = max(frecuencia.values())

        for n in numeros:
            if frecuencia[n] == max_frecuencia:
                return n
    
    def desviacion_estandar(self, numeros):
        return self.varianza(numeros) ** 0.5
    
    def varianza(self, numeros):
        if not numeros:
            return 0

        media = self.promedio(numeros)
        suma = 0
        for n in numeros:
            suma += (n - media) ** 2

        return suma / len(numeros)
    
    def rango(self, numeros):
        if not numeros:
            return 0
        return max(numeros) - min(numeros)