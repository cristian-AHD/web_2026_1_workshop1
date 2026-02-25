class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        if jugador1 == jugador2:
            return "empate"

        gana_a = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        if gana_a[jugador1] == jugador2:
            return "jugador1"
        return "jugador2"
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return tablero[i][0]
            
        for i in range(3):
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return tablero[0][i]

        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return tablero[0][0]

        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return tablero[0][2]

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        import random
        combinacion = []
        for _ in range(longitud):
            combinacion.append(random.choice(colores_disponibles))
        return combinacion
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        for v in [desde_fila, desde_col, hasta_fila, hasta_col]:
            if v < 0 or v > 7:
                return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False

        return True