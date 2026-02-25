class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        opciones = ["piedra", "papel", "tijera"]

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        if (
            (jugador1 == "piedra" and jugador2 == "tijera") or
            (jugador1 == "papel" and jugador2 == "piedra") or
            (jugador1 == "tijera" and jugador2 == "papel")
        ):
            return "jugador1"

        return "jugador2"
    
    def ta_te_ti_ganador(self, tablero):
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] != " ":
                return fila[0]

        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] != " ":
                return tablero[0][col]

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