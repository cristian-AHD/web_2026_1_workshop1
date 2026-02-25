class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    def fibonacci(self, n):
        
        if n < 0:
            return None
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def secuencia_fibonacci(self, n):
        secuencia = []
        a, b = 0, 1
        for _ in range(n):
            secuencia.append(a)
            a, b = b, a + b
        return secuencia
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos
    
    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                suma += i
                if i != n // i:
                    suma += n // i
        return suma == n
    
    def triangulo_pascal(self, filas):
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo
    
    def factorial(self, n):
        if n < 0:
            return None
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
    
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return (a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        suma = 0
        n = abs(n)
        while n > 0:
            suma += n % 10
            n //= 10
        return suma
    
    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        suma = 0
        for d in digitos:
            suma += int(d) ** potencia
        return suma == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_magica = sum(matriz[0])

        for fila in matriz:
            if sum(fila) != suma_magica:
                return False

        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_magica:
                return False

        if sum(matriz[i][i] for i in range(n)) != suma_magica:
            return False

        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_magica:
            return False

        return True