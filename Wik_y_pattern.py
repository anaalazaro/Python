from wiktionaryparser import WiktionaryParser
from pattern.es import parse,tag,singularize,pluralize
from pattern.web import Wiktionary

def de_pattern(teclado):
	palabra_tipo=tag(teclado,tokenize=True, encoding="utf-8")
	print(palabra_tipo)
	if palabra_tipo[0][1]=="NN":
		palabra_tipo=[teclado,"Sustantivo"]
	elif palabra_tipo[0][1]=="VB":
		palabra_tipo=[teclado,"Verbo"]
	elif palabra_tipo[0][1]=="JJ":
		palabra_tipo=[teclado,"Adjetivo"]
	else:
		palabra_tipo=[teclado,"error"] #preguntar por esto	
		print(palabra_tipo)
	return palabra_tipo


def validacion(teclado,diccionario,lista_de_palabras):
	""" Esta funcion debe ser llamada dentro de un loop para ingresar todas las palabras. Puntualmente
	la funcion valida 1 palabra ingresada y la agrega a una lista de palabras validas y un diccionario 
	de palabras validas """
	web = Wiktionary(language="es")
	articulo = web.search(teclado)#PALABRA
	if articulo is None:
		teclado=singularize(teclado)
		cambio=False
		articulo = web.search(teclado)
	elif articulo is not None:
		cambio=True 						#booleano que indica si la palabra cambió de plural a singular
		s = list(filter(lambda x: x.title=="Español", articulo.sections))  
		etimologia = list(filter(lambda x: x.title=="Etimología", s[0].children))
		definicion=etimologia[0].content #DEFINICION  
		lista = ["Adjetivo","Verbo","Verbo intransitivo","Forma verbal","Verbo transitivo","Forma adjetiva","Sustantivo","Sustantivo masculino","Sustantivo femenino"]
		lista_verbos=["Verbo","Verbo intransitivo","Forma verbal","Verbo transitivo"]
		lista_sustantivos=["Sustantivo","Sustantivo masculino","Sustantivo femenino"]
		lista_adjetivos=["Adjetivo","Forma Adjetiva"]
		for tipo in lista:
			tipo_real = list(filter(lambda x: x.title==tipo, s[0].children))
			if tipo_real:
				clasificacion=tipo
		if clasificacion in lista_adjetivos: 
			clasificacion="Adjetivo"
		elif clasificacion in lista_sustantivos:
		    clasificacion="Sustantivo"
		elif clasificacion in lista_verbos:
		    clasificacion="Verbo"
		validado=True      
								   
	if cambio:
		pluralize(teclado)
								 

#if articulo is None:           #pregunto si no se encontro en wik
#	palabra_pattern=de_pattern(teclado)
#	indice_diccionario=palabra_pattern[0]
#	indice_diccionario={"Definición":definicion,"Tipo":palabra_pattern[1]}
#	diccionario.update(indice_diccionario)
#   lista_de_palabras.append(palabra_pattern[0])

#lo de arriba no esta implementado ya que por un error de pattern, clasifica a todas las palabras como NN es decir, sustantivos

	lista_de_palabras.append(teclado)
	indice_diccionario=teclado
	indice_diccionario={"Definición":definicion,"Tipo":clasificacion}
	diccionario.update(indice_diccionario)
	if validado:
		lo_que_devuelve={"lista":lista_de_palabras,"diccionario":diccionario,"validez":True} #si se ingreso correctamente, se modifica la lista y diccionario
	else:
		lo_que_devuelve={"lista":lista_de_palabras,"diccionario":diccionario,"validez":False} #si no se ingresó, solo "sirve" la validez
	return lo_que_devuelve
#print(diccionario)









#unificar los tipos dados por pattern y los tipos dados por wik y comparar
#de ahi salen los reportes
#
#guardar las palabras validad en una dicc
#hacer que sean por teclado
#
#exepciones
