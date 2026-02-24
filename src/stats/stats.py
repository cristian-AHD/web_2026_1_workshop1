class Stats:
    def promedio(self, numeros):
        suma = 0
        for n in numeros:
            suma += n
        return suma / len(numeros)
    
    def mediana(self, numeros):
        ordenados = sorted(numeros)
        n = len(ordenados)
        medio = n // 2
        if n % 2 == 0:
            return (ordenados[medio - 1] + ordenados[medio]) / 2
        return float(ordenados[medio])
    
    def moda(self, numeros):
        frecuencia = {}
        for n in numeros:
            if n in frecuencia:
                frecuencia[n] += 1
            else:
                frecuencia[n] = 1
        moda = numeros[0]
        for n in frecuencia:
            if frecuencia[n] > frecuencia[moda]:
                moda = n
        return moda
    
    def desviacion_estandar(self, numeros):
        return self.varianza(numeros) ** 0.5
    
    def varianza(self, numeros):
        media = self.promedio(numeros)
        suma = 0
        for n in numeros:
            suma += (n - media) ** 2
        return suma / len(numeros)
    
    def rango(self, numeros):
        minimo = numeros[0]
        maximo = numeros[0]
        for n in numeros:
            if n < minimo:
                minimo = n
            if n > maximo:
                maximo = n
        return maximo - minimo