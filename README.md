# Contador de Duplicados

[![python3](https://img.shields.io/badge/Python-3.9.4-blue.svg)](https://www.python.org/)

<p align="center">
  <img src="./docs/img/keys.jpg" width="400" alt="Keys">
</p>


## Contenidos

- [¿Qué es _Contador de Duplicados_?](#about)
- [Introducción](#getting_started)
- [El desafío](#challenge)
- [Ejemplos](#examples)
- [Instalación](#installing)
- [uso](#usage)

## ¿Qué es _Contador de Duplicados_? <a name = "about"></a>

Desafío: ¿Cuántas veces has querido saber si los caracteres de un texto se repiten? ¡Ya llegó el contador de caracteres duplicados!

## Introducción <a name = "getting_started"></a>

El contador de caracteres duplicados es un algoritmo que permite encontrar cuántos caracteres se repiten una o más veces en una cadena de texto.

## Sobre el desafío <a name = "challenge"></a>

El reto es realizar un contador de caracteres duplicados en una cadena de texto, el reto dura una hora, puede usarse cualquier lenguaje.

- Debe escribirse una función que devuelva el número de caracteres duplicados.

- Para este caso **no se distingen mayúsculas de minúsculas**.

- **Regla de negocio**: Hay que suponer que la cadena de texto sólo contiene letras del alfabeto en mayúsculas y minúsculas, además de números enteros.

### Ejemplos del retorno de la función. <a name = "examples"></a>

- "abcde" devolvería 0 pues ningún carácter se repite más de una vez.
- "aabbcde" devolvería 2 pues 'a' y 'b' se repiten.
- "aabBcde" devolvería 2 pues 'a' aparece dos veces y 'b' dos veces ('b' y 'B').
- "invisibility" devolvería 1 pues 'i' aparece cinco veces.
- "aA11" devolvería 2 pues 'a' y '1' se repiten.
- "ABBA" devolvería 2 pues 'A' y 'B' ocurren dos veces.

### Requisitos Previos

Para ejecutar el algoritmo es necesario tener instalado **Python3**.

### Instalación <a name = "installing"></a>

Una vez instalado Python3, se clona el repo, se ingresa a la carpeta y se abre el script con Python3.

```
git clone https://github.com/Marfullsen/contador-de-duplicados.git
cd contador-de-duplicados
python main.py
```

## Uso <a name = "usage"></a>

El código iniciará con las pruebas del código para verificar que todo esté en órden, luego se podrán ingresar palabras infinitamente para ser analizadas.

```
Ingrese una cadena de texto: aabc
La cantidad de letras que en algún momento se repetiten es 1

Ingrese una cadena de texto: aAbc
La cantidad de letras que en algún momento se repetiten es 1

Ingrese una cadena de texto: aaaaAaaaaabc
La cantidad de letras que en algún momento se repetiten es 1

Ingrese una cadena de texto: aabbc
La cantidad de letras que en algún momento se repetiten es 2

Ingrese una cadena de texto: AabBc
La cantidad de letras que en algún momento se repetiten es 2

Ingrese una cadena de texto: aAaAaAabBbBBBbcCcCCCcccc
La cantidad de letras que en algún momento se repetiten es 3
```

## Créditos y referencias.
- Foto de llaves - <a href="https://unsplash.com/@fotonium?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Akhilesh Sharma</a> en el sitio <a href="https://unsplash.com/s/photos/duplicate?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  
- Imágen comprimida en el sitio [compressjpeg.com](https://compressjpeg.com/)