class Matrix:
    """
    Clase con métodos para operaciones sobre matrices.
    Incluye operaciones aritméticas, propiedades y transformaciones matriciales.
    """

    def suma_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices tienen dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            resultado.append(fila)
        return resultado

    def resta_matrices(self, A, B):
        if len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Las matrices tienen dimensiones incompatibles")
        resultado = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] - B[i][j])
            resultado.append(fila)
        return resultado

    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("Las dimensiones son incompatibles para multiplicación")
        m, n, p = len(A), len(A[0]), len(B[0])
        resultado = []
        for i in range(m):
            fila = []
            for j in range(p):
                suma = 0
                for k in range(n):
                    suma += A[i][k] * B[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado

    def multiplicar_escalar(self, matriz, escalar):
        resultado = []
        for fila in matriz:
            nueva_fila = []
            for elemento in fila:
                nueva_fila.append(elemento * escalar)
            resultado.append(nueva_fila)
        return resultado

    def transpuesta(self, matriz):
        if matriz == []:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []
        for j in range(columnas):
            fila = []
        for i in range(filas):
            fila.append(matriz[i][j])
        resultado.append(fila)
        return resultado

    def es_cuadrada(self, matriz):
        if matriz == []:
            return False
        return len(matriz) == len(matriz[0])

    def es_simetrica(self, matriz):
        if not self.es_cuadrada(matriz):
            return False
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if matriz[i][j] != matriz[j][i]:
                    return False
        return True

    def traza(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][i]
        return suma

    def determinante_2x2(self, matriz):
        if len(matriz) != 2 or len(matriz[0]) != 2:
            raise ValueError("La matriz no es 2x2")
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    def determinante_3x3(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("La matriz no es 3x3")

        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]

        return (
            a * (e * i - f * h)
            - b * (d * i - f * g)
            + c * (d * h - e * g)
        )

    def identidad(self, n):
        resultado = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(1 if i == j else 0)
            resultado.append(fila)
        return resultado

    def diagonal(self, matriz):
        if not self.es_cuadrada(matriz):
            raise ValueError("La matriz no es cuadrada")
        return [matriz[i][i] for i in range(len(matriz))]

    def es_diagonal(self, matriz):
        n = len(matriz)
        for i in range(n):
            for j in range(n):
                if i != j and matriz[i][j] != 0:
                    return False
        return True

    def rotar_90(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0])
        resultado = []
        for j in range(columnas):
            fila = []
            for i in range(filas - 1, -1, -1):
                fila.append(matriz[i][j])
            resultado.append(fila)
        return resultado

    def buscar_en_matriz(self, matriz, valor):
        posiciones = []
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == valor:
                    posiciones.append((i, j))
        return posiciones
