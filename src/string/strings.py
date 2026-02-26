class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == self.invertir_cadena(texto)
    
    def invertir_cadena(self, texto):
        resultado = ""
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        return resultado
    
    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in texto:
            if letra in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
        for letra in texto:
            if letra.isalpha() and letra not in vocales:
                contador += 1
        return contador
    
    def es_anagrama(self, texto1, texto2):
        texto1 = texto1.lower().replace(" ", "")
        texto2 = texto2.lower().replace(" ", "")
        if len(texto1) != len(texto2):
            return False
        frecuencia = {}
        for letra in texto1:
            if letra in frecuencia:
                frecuencia[letra] += 1
            else:
                frecuencia[letra] = 1
        for letra in texto2:
            if letra not in frecuencia or frecuencia[letra] == 0:
                return False
            frecuencia[letra] -= 1
        return True
    
    def contar_palabras(self, texto):
        texto = texto.strip()
        if texto == "":
            return 0
        contador = 0
        en_palabra = False
        for caracter in texto:
            if caracter != " " and not en_palabra:
                en_palabra = True
                contador += 1
            elif caracter == " ":
                en_palabra = False
        return contador
    
    def palabras_mayus(self, texto):
        palabras = texto.split(" ")
        resultado = []
        for palabra in palabras:
            if len(palabra) > 0:
                resultado.append(palabra[0].upper() + palabra[1:])
            else:
                resultado.append(palabra)
        return " ".join(resultado)
    
    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio_anterior = False

        for caracter in texto:
            if caracter == " ":
                if not espacio_anterior:
                    resultado += caracter
            espacio_anterior = True
        else:
            resultado += caracter
            espacio_anterior = False

        return resultado
    
    def es_numero_entero(self, texto):
        if texto == "" or texto == "-":
            return False
        inicio = 1 if texto[0] == "-" else 0
        for i in range(inicio, len(texto)):
            if texto[i] < "0" or texto[i] > "9":
                return False
        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for caracter in texto:
            if caracter.isalpha():
                base = ord("A") if caracter.isupper() else ord("a")
                resultado += chr((ord(caracter) - base + desplazamiento) % 26 + base)
            else:
                resultado += caracter
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        if subcadena == "":
            return []

        posiciones = []
        largo = len(subcadena)
        for i in range(len(texto) - largo + 1):
            if texto[i:i + largo] == subcadena:
                posiciones.append(i)
        return posiciones