from pattern.es import parse,tag,singularize,pluralize
from pattern.web import Wiktionary

def de_pattern(teclado):
	palabra_tipo=tag(teclado,tokenize=True, encoding="utf-8")
	#print(palabra_tipo)
	if palabra_tipo[0][1]=="NN":
		palabra_tipo=[teclado,"Sustantivo"]
	elif palabra_tipo[0][1]=="VB":
		palabra_tipo=[teclado,"Verbo"]
	elif palabra_tipo[0][1]=="JJ":
		palabra_tipo=[teclado,"Adjetivo"]
	else:
		palabra_tipo=[teclado,"error"] #preguntar por esto	
		#print(palabra_tipo)
	return palabra_tipo


def validacion(teclado, diccionario):
	""" Esta funcion debe ser llamada dentro de un loop para ingresar todas las palabras. Puntualmente
	la funcion valida 1a palabra ingresada y la agrega a un diccionario de palabras validas """
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
								 
	#lista_de_palabras.append(teclado)
	indice=teclado
	diccionario[indice]={"Definición":definicion,"Tipo":clasificacion}#diccionario con la palabra , su deficinicion y su tipo.
	#diccionario.update(indice)
	if validado:
		datos={"info_palabra":diccionario,"validez":True} #si se ingreso correctamente, se modifica la lista y diccionario
	else:
		datos={"info_palabra":diccionario,"validez":False} #si no se ingresó, solo "sirve" la validez
	return datos
#print(diccionario)

def comparando(pattern,wik):
	if pattern[1]!=wik[1]:
		#reporte 1 pattern y wik no coinciden
		aux= "No Coinciden"
		return aux



#
#   para la implementacion hay que llamar a las funciones
#	de pattern y validacion, despues comparar con comparando
#	y finalmente realizar los reportes que faltan
#
