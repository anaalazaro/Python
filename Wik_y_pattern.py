from pattern.es import parse,tag,singularize,pluralize
from pattern.web import Wiktionary
import json

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
		palabra_tipo=["",""] #preguntar por esto	
		#print(palabra_tipo)
	return palabra_tipo


def validacion(teclado, diccionario):
	""" Esta funcion debe ser llamada dentro de un loop para ingresar todas las palabras. Puntualmente
	la funcion valida 1a palabra ingresada y la agrega a un diccionario de palabras validas """
	web = Wiktionary(language="es")
	articulo = web.search(teclado)#PALABRA
	cambio=False
	try:
		s = list(filter(lambda x: x.title=="Español", articulo.sections))
		etimologia = list(filter(lambda x: x.title=="Etimología", s[0].children))
		if etimologia ==[]:
			teclado=singularize(teclado)
			cambio=True 						#booleano que indica si la palabra cambió de plural a singular
			validado=False
			articulo = web.search(teclado)
		if articulo is not None:
			try:
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
						break
				if clasificacion in lista_adjetivos: 
					clasificacion="Adjetivo"
				elif clasificacion in lista_sustantivos:
					clasificacion="Sustantivo"
				elif clasificacion in lista_verbos:
					clasificacion="Verbo"
				validado=True      
			except IndexError:		#esto previene el error de que la pagina de wik no tenga etimologia (definicion)
				validado=False
				definicion="" # lo declaro para evitar un error posterior de referenciar una variable antes de que tenga un valor
				clasificacion=""						   
	except AttributeError:
		validado=False
		definicion="" # lo declaro para evitar un error posterior de referenciar una variable antes de que tenga un valor
		clasificacion=""	
	if cambio:
		teclado=pluralize(teclado)
								 
	indice=teclado
	diccionario[indice]={"Definición":definicion,"Tipo":clasificacion}#diccionario con la palabra , su deficinicion y su tipo.
	if validado:
		datos={"info_palabra":diccionario,"validez":True} #si se ingreso correctamente, se modifica la lista y diccionario
	else:
		datos={"info_palabra":diccionario,"validez":False} #si no se ingresó, solo "sirve" la validez
	return datos
#print(diccionario)

def comparando(pattern,wik):
	if pattern!=wik:
		aux="No Coinciden"
	elif (pattern=="" and wik==""):
		aux="No se encontro la palabra"
	else:
		aux="Las definiciones coinciden"	
	return aux


def no_coinciden(palabra,c_de_wik,c_de_pattern):
	""" Esta función ingresa las palabras cuyas definiciones no coinicden a un reporte """
	datos=[
		{"Palabra ":palabra,
		"Clasificacion de Wiktionary ":c_de_wik,
		"Clasificacion de Pattern ":c_de_pattern}]
	archivo = open("Reporte_No_Coinciden.txt", "a")
	json.dump(datos, archivo)
	archivo.close()

def no_existen(palabra):
	""" Esta función ingresa las palabras cuyas definiciones no existen a un reporte """
	datos={
		"Palabra ":palabra
	}
	archivo = open("Reporte_No_Existen.txt", "a")
	json.dump(datos, archivo)
	archivo.close()
