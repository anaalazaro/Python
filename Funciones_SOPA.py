def insertar_palabra_horizontal (palabra,matriz,g):
	pos_maxima=17-len(palabra)
	pos=random.choice(range(0,pos_maxima))
	for i in palabra:
		matriz[1][pos+1]=i #el mas uno es para evitar corrimientos
		pos=pos+1
		g.DrawRectangle((pos * BOX_SIZE + 5, 1 * BOX_SIZE + 3), (pos * BOX_SIZE + BOX_SIZE + 5, 1 * BOX_SIZE + BOX_SIZE + 3), line_color='black',fill_color="white")
		location= (pos * BOX_SIZE + 18, 1 * BOX_SIZE + 17)
		g.DrawText(i,location , font='Courier 25')


def insertar_palabra_vertical (palabra,matriz,g):
	pos_maxima=17-len(palabra)
	pos=random.choice(range(0,pos_maxima))
	for i in palabra:
		matriz[pos+1][1]=i #el mas uno es para evitar corrimientos
		pos=pos+1
		g.DrawRectangle((1 * BOX_SIZE + 5, pos * BOX_SIZE + 3), (1 * BOX_SIZE + BOX_SIZE + 5, pos * BOX_SIZE + BOX_SIZE + 3), line_color='black',fill_color="white")
		location= (1 * BOX_SIZE + 18, pos * BOX_SIZE + 17)
		g.DrawText(i ,location , font='Courier 25')


def procesar_horizontal(matriz_letras,matriz_colores,orientacion,dic_colores):
	lista_aux=[]
	for row in range(16):
		palabra=""
		for col in range(16):
			color_actual=matriz_colores[row][col]
			letra_actual=matriz_letras[row][col]
			if color_actual in dic_colores.values():     # se debe pasar una dic con los tres colores
				claves=dic_colores.keys()
				for una_clave in claves:
					if dic_colores[una_clave]==color_actual:
						tipo_actual=una_clave
			color=dic_colores[tipo_actual]
			if color==color_actual:
				palabra=palabra+letra_actual	
			l=[palabra,tipo_actual]
			lista_aux.append(l)
	return lista_aux


def procesar_vertical(matriz_letras,matriz_colores,orientacion,dic_colores):
	lista_aux=[]
	for col in range(16):
		palabra=""
		for row in range(16):
			color_actual=matriz_colores[row][col]
			letra_actual=matriz_letras[row][col]
			if color_actual in dic_colores.values():     # se debe pasar una dic con los tres colores
				claves=dic_colores.keys()
				for una_clave in claves:
					if dic_colores[una_clave]==color_actual:
						tipo_actual=una_clave
			color=dic_colores[tipo_actual]
			if color==color_actual:
				palabra=palabra+letra_actual	
			l=[palabra,tipo_actual]
			lista_aux.append(l)
	return lista_aux
