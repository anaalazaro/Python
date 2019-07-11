import random
def insertar_palabra_horizontal (BOX_SIZE,palabra,matriz,g,filas_validas,fuente,colores):   #en filas validas se le debe mandar una lista con las filas que todavia no tienen una palabra insertada
	pos_maxima=17-len(palabra)   
	pos=random.choice(range(0,pos_maxima))
	fila=random.choice(filas_validas)
	filas_validas.remove(fila)
	for i in palabra:
		matriz[fila][pos+1]=i #el mas uno es para evitar corrimientos
		colores[pos+1][columna]="grey"
		pos=pos+1
		g.DrawRectangle((pos * BOX_SIZE + 5, fila * BOX_SIZE + 3), (pos * BOX_SIZE + BOX_SIZE + 5, fila * BOX_SIZE + BOX_SIZE + 3), line_color='black',fill_color="white")
		location= (pos * BOX_SIZE + 18, fila * BOX_SIZE + 17)
		g.DrawText(i,location , font=fuente)
	return filas_validas	


def insertar_palabra_vertical (BOX_SIZE,palabra,matriz,g,columnas_validas,fuente,colores):
	pos_maxima=17-len(palabra)
	pos=random.choice(range(0,pos_maxima))
	columna=random.choice(columnas_validas)
	columnas_validas.remove(columna)
	for i in palabra:
		matriz[pos+1][columna]=i #el mas uno es para evitar corrimientos
		colores[pos+1][columna]="grey"
		pos=pos+1
		g.DrawRectangle((columna * BOX_SIZE + 5, pos * BOX_SIZE + 3), (columna * BOX_SIZE + BOX_SIZE + 5, pos * BOX_SIZE + BOX_SIZE + 3), line_color='black',fill_color="white")
		location= (columna * BOX_SIZE + 18, pos * BOX_SIZE + 17)
		g.DrawText(i ,location , font=fuente)
	return columnas_validas


def procesar_horizontal(matriz_letras,matriz_colores,orientacion,dic_colores):
	lista_aux=[]
	tipo_actual_f=" "
	for row in range(16):
		try:
			palabra=""
			for col in range(16):
				color_actual=matriz_colores[row][col]
				letra_actual=matriz_letras[row][col]
				if color_actual in dic_colores.values():     # se debe pasar una dic con los tres colores
					claves=dic_colores.keys()
					for una_clave in claves:
						if dic_colores[una_clave]==color_actual:
							tipo_actual_f=una_clave
					color=dic_colores[tipo_actual_f]
					if color==color_actual:
						palabra=palabra+letra_actual	
			if palabra != "":
				l=[palabra,tipo_actual_f]
				lista_aux.append(l)
		except KeyError:
						a=1  #solucion temporal
	return lista_aux




def procesar_vertical(matriz_letras,matriz_colores,orientacion,dic_colores):
	lista_aux=[]
	tipo_actual_f=" "
	for col in range(16):
		try:
			palabra=""
			for row in range(16):
				color_actual=matriz_colores[row][col]
				letra_actual=matriz_letras[row][col]
				if color_actual in dic_colores.values():     # se debe pasar una dic con los tres colores
					claves=dic_colores.keys()
					for una_clave in claves:
						if dic_colores[una_clave]==color_actual:
							tipo_actual_f=una_clave
					color=dic_colores[tipo_actual_f]
					if color==color_actual:
						palabra=palabra+letra_actual	
			if palabra != "":
				l=[palabra,tipo_actual_f]
				lista_aux.append(l)
		except KeyError:
						a=1  #solucion temporal
	return lista_aux
