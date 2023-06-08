# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def numeroBinario(numero):
    '''
    Esta función recibe como argumento un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
    '''
    #Tu código aca:   
    import re
    if (numero < 0) or (type(numero) != int):
      return None
    numero1 = bin(numero)
    print(re.sub('0b', '', numero1))       
   #return 'Funcion incompleta'

def dividirMultiplicar(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar una lista con los siguientes parámetros:
   1.Los números que sean positivos y pares se deben dividir por 2, y el resultado expresado como entero (sin decimales, no redondeando, debe tomar sólo la parte entera de la división por 2).
   2.Los números negativos multiplicados por 2.
   3.Los que no cumplan los criterios anteriores deben quedar igual al valor original.
   4.Ordernar los números de mayor a menor.
   Ej: dividirMultiplicar([2,4,1,-3]): debe retornar: [2, 1, 1, -6]
   '''   
   #Tu código acá
   lista_final = []
   for i in lista:
      num = lista[i]
      if (num > 0) and (num % 2 == 0):
         lista_final.append(num // 2)
      elif num < 0:
         lista_final.append(2 * num)
      else:
         lista_final.append(num)
   lista_final.sort(reverse=True)
   return lista_final
      
   return 'Funcion incompleta'

def crearDiccionario(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar un diccionario con tres claves, "multiplos3", 'cuadrados", "menores_promedio".
   Para la clave "multiplos3", el valor debe ser una lista con los múltiplos de 3 de la lista original.
   Para la clave "cuadrados", el valor debe ser una lista con los valores de la lista original elevados al cuadrado.
   Para la clave "menores_promedio", el valor debe ser una lista con los valores menores al promedio de la lista original.
   EJ: crearDiccionario([3,6,7,12]): debe retornar: {'multiplos3': [3, 6, 12], 'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}
   '''
   #Tu código acá
   promedio = sum(lista) / len(lista)
   multiplos3 = []
   cuadrados = []
   menores_p = []
   for i in lista:
      if i % 3 == 0:
         multiplos3.append(i)
      cuadrados.append(i ** 2)
      if i < promedio: menores_p.append(i)
   claves = ['multiplos3', 'cuadrados', 'menores_promedio']
   diccionario = dict(zip(claves,[multiplos3, cuadrados, menores_p]))
   return diccionario
   

   return 'Funcion incompleta'

def trianguloRectangulo(a,b,c):
   '''
   La función debe recibir como argumentos el valor en cm de los lados de un triángulo (a y b son los catetos), y dado estos valores, retornar True si en efecto corresponden a un triángulo rectángulo, o False en caso contrario. Sólo se debe poder pasar valores enteros como argumentos de la función, caso contrario debe retornar nulo.
   EJ: trianguloRectangulo(3.5,3.5,2.4), debe retornar nulo
   EJ: trianguloRectangulo(3,3,3), debe retornar False
   EJ: trianguloRectangulo(3,4,5), debe retornar True
   '''
   #Tu código acá
   if (type(a) != int) or (type(b) != int) or (type(c) != int):
         return None
   elif c == (a ** 2 + b ** 2) ** 0.5:
         return True
   elif c != (a ** 2 + b ** 2) ** 0.5:
         return False
    
   #return 'Funcion incompleta'

def ciudadesPoblacion(diccionario):
   '''
   Dado el siguiente diccionario ciudades, la función debe retornar una lista de listas, donde cada elemento de la lista sea una lista con el par ['ciudad', población], pero sólo de las ciudades que comiencen con la letra 'B', y como último elemento de la lista el par ['promedio', promedio de población] con el promedio de población de las ciudades seleccionadas.
   Ej: Si se pidiera ciudades que comiencen con la letra 'S', debe devolver: [['São Paulo', 21048514], ['Santiago de Chile', 7112808],['promedio', 14080661.0]]

   ciudades = {
      'São Paulo': 21048514,
      'Buenos Aires': 14975587,
      'Río de Janeiro': 11902701,
      'Bogotá': 10777931,
      'Lima': 10479899,
      'Santiago de Chile': 7112808,
      'Belo Horizonte': 6006091,
      'Caracas': 5622798,
      'Brasília': 4291577
      }
      Pista: investigar método de string startswith()
   '''
   #Tu código acá
   nombres = list(diccionario.keys())
   poblaciones = list(diccionario.values())
   listafinal = []
   elemento = []
   poblacion_total = 0
   for i in nombres:
      if i.startswith('B'): 
         a = nombres[nombres.index(i)]
         b = poblaciones[nombres.index(i)]
         elemento.append([a,b])
         poblacion_total += b
   elemento.append(['Promedio:',poblacion_total / len(elemento)])
   return elemento
   return 'Funcion incompleta'

def ordenarPalabras(palabras):
   '''
   La función recibe como argumento una secuencia de palabras unidas por guiones, y debe retornar las mismas palabras, unidas por guiones, pero en orden alfabético. Si el argumento que se le pasa no es un string o no contiene guiones, debe retornar nulo.
   EJ: ordenarPalabras('saco-libro-casa') debe retornar 'casa-libro-saco'
   EJ: ordenarPalabras('Hola') debe retornar nulo
   Pista: investigar métodos de string
   '''
   #Tu código acá
   if type(palabras) != str or palabras.find('-') == -1 : return None
   a = palabras.rsplit('-')
   r = len(a) - 1
   cadena1 = ''
   for t in range(r,-1,-1):
      if t == 0: cadena1 += a[t]
      else : cadena1 += a[t] + '-'
   return(cadena1)
   return 'Funcion incompleta'

def stringEspejo(texto):
    '''
    La función recibe como argumento una cadena de texto y retorna la cadena invertida, pero sólo si tiene más de tres caracteres, sino debe retornar nulo.
    EJ: stringEspejo('Hola Mundo') debe retornar 'odnuM aloH'
    EJ: stringEspejo('Hoy') debe retornar nulo
    '''
    #Tu código acá
    if len(texto) <= 3 : return None
    a = list(texto)
    l = len(texto)
    t_espejado = ''
    for i in range(l-1,-1,-1):
        t_espejado += a[i]
    return t_espejado
    return 'Funcion incompleta'
