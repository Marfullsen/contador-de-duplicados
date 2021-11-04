''' Francisco Marfull, fr.marfull@duocuc.cl
# Contar el número de duplicados
#
# Escriba la función duplicateCount, que devuelva
# el numero (entero) de letras duplicadas.
#
# Condicion 1 del String de entrada: (distinct case-insensitive)
# No distinguen entre mayúsculas y minúsculas
#
# Regla de negocio
# Suponer que el String de entrada SOLO contiene alfabetos (mayúsculas y minúsculas) y dígitos numericos
#
# Ejemplos de retornos de la funcion
#
# "abcde" -> 0 # ningún carácter se repite más de una vez
# "aabbcde" -> 2 # 'a' y 'b'
# "aabBcde" -> 2 # 'a' aparece dos veces y 'b' dos veces (`b` y` B`)
# "indivisibility" -> 1 # 'i' aparece seis veces
# "aA11" -> 2 # 'a' y '1'
# "ABBA" -> 2 # 'A' y 'B' ocurren dos veces
'''
class CountingDuplicates():
    def duplicateCount(text):
        count = 0
        conjunto = set(text.lower())
        if len(conjunto) == len(text):
            return 0
        else:
            for letra in conjunto:
                lower_text = text.lower()
                lower_letra = letra.lower()
                if lower_text.count(lower_letra) > 1:
                    count += 1
            return count

def main():
    texto = ' '
    contarRepetidos = CountingDuplicates
    while texto:
        texto = input('Ingrese una cadena de texto: ')
        repetidos = contarRepetidos.duplicateCount(texto)
        print(f'La cantidad de letras que en algún momento se repetiten es {repetidos}')

def pruebas_unitarias():
    print('Iniciando pruebas unitarias...')
    contarRepetidos = CountingDuplicates
    
    ## Prueba unitaria 1.
    texto = "aabbcc"
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 3
        print('¡Prueba 1 aprobada!')
    except:
        print('Error en la prueba 1')
    
    ## Prueba unitaria 2
    texto = "abcde" # -> 0 # ningún carácter se repite más de una vez
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 0
        print('¡Prueba 2 aprobada!')
    except:
        print('Error en la prueba 2')
    
    ## Prueba unitaria 3
    texto = "aabbcde" # -> 2 # 'a' y 'b'
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 2
        print('¡Prueba 3 aprobada!')
    except:
        print('Error en la prueba 3')
    
    ## Prueba unitaria 4
    texto = "aabBcde" # -> 2 # 'a' aparece dos veces y 'b' dos veces (`b` y` B`)
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 2
        print('¡Prueba 4 aprobada!')
    except:
        print('Error en la prueba 4')
    
    ## Prueba unitaria 5
    texto = "indivisibility" # -> 1 # 'i' aparece seis veces
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 1
        print('¡Prueba 5 aprobada!')
    except:
        print('Error en la prueba 5')
    
    ## Prueba unitaria 6
    texto = "aA11" # -> 2 # 'a' y '1'
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 2
        print('¡Prueba 6 aprobada!')
    except:
        print('Error en la prueba 6')
    
    ## Prueba unitaria 7
    texto = "ABBA" # -> 2 # 'A' y 'B' ocurren dos veces
    try:
        repetidos = contarRepetidos.duplicateCount(texto)
        assert repetidos == 2
        print('¡Prueba 7 aprobada!')
    except:
        print('Error en la prueba 7')
    
    ## Si todo fue aprobado:
    print('¡Todas las pruebas unitarias fueron aprobadas!')

if __name__ == '__main__':
    pruebas_unitarias()
    print('\nIniciando programa normalmente...')
    main()
