import PySimpleGUI as sg
import sys
#modulo de configuracion de palabras

def ColorChooser(): #chequear si devuelve un color
	'''Muestra una carta de colores. Permite seleccionar un color
	y al presionar OK lo guarda.'''

	COLORS = ['cornflower blue', 'slate blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'dark turquoise', 'cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green','medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'blue violet', 'purple', 'medium purple',
          'thistle']




	sg.SetOptions(button_element_size=(8,2), element_padding=(0,0), auto_size_buttons=False, border_width=0)

	layout = [[sg.Text('Seleccione un color', text_color='black', font='Any 10')]]
	row = []
	# -- Create primary color viewer window --
	for rows in range(10):

		row = []
		for i in range(8):
			try:
				color = COLORS[rows+10*i]
				row.append(sg.Button(tooltip=color, button_color=('black', color), key=color))
			except:
				pass
		layout.append(row)
	#layout.append([sg.OK()])


	# for i, color in enumerate(COLORS):
	#     row.append(sg.Button(color, button_color=('black', color), key=color))
	#     if (i+1) % 12 == 0:
	#         layout.append(row)
	#         row = []

	window = sg.Window('Color Chooser', grab_anywhere=False, font=('any 9')).Layout(layout)

	# -- Event loop --
	if True:
		event, values = window.Read()
		if event is not None:
			sg.Popup('Color seleccionado correctamente.')
	window.Close()
	
	return event

#colores
def Color():
	'''Esta funcion permite elegir un color para los sustantivos,
	otro para los adjetivos, y otro para los verbos. Retorna un
	diccionario con dichas selecciones.'''
	
	#el diccionario colores tendra por defecto 3 colores que se modificaran por el usuario con el color chooser
	colours = {'Sustantivo': 'sea green', 'Adjetivo': 'sky blue', 'Verbo': 'coral'}
	#ventana con 3 botones, cada uno deberia abrir el color chooser una vez para seleccionar segun corresponda
	#el boton OK deberia presionarse al haber elegido los 3 colores
	layout =  [
    [sg.Text('Seleccione un color para cada tipo de palabra. Al finalizar presione "OK".')],
    [sg.Text('Color para sustantivos'), sg.Button('.')],
    [sg.Text('Color para adjetivos'), sg.Button('..')],
    [sg.Text('Color para verbos'), sg.Button('...')],
    [sg.Button('OK')]
	]

	window = sg.Window('Configuración').Layout(layout)
	
	while True:
		event, values = window.Read()
		if event is '.':
			selected_colour = ColorChooser()
			colours['Sustantivo'] = selected_colour
		if event is '..':
			selected_colour = ColorChooser()
			colours['Adjetivo'] = selected_colour
		if event is '...':
			selected_colour = ColorChooser()
			colours['Verbo'] = selected_colour
		if event is 'OK':
			break
	window.Close()
	
	return colours

#mayus minus
def CapsLock():
	'''Esta funcion genera una ventana que permite elegir si mostrar
	las letras en mayúscula o en minúscula. Retorna la opción seleccionada
	en formato String'''

	layout =  [
    [sg.Text('Seleccione cómo se mostrarán las letras:')],
    [sg.Radio('Mayúscula', "RADIO1", default=True),
    sg.Radio('Minúscula', "RADIO1")],
    [sg.Button('OK')]
	]
	
	window = sg.Window('Configuración').Layout(layout)
	
	if True:
		event, values = window.Read()

	if event == 'OK':
		if values[0]:
			caps = 'MAYUS'
		if values[1]:
			caps = 'MINUS'
	window.Close()
	return caps

#tipografia
def Typo():
	'''Esta funcion permite elegir la tipografía que será
	utilizada dentro de la sopa de letras. Retorna la opción
	seleccionada.'''
	
	#desconozco como obtener las fuentes del sistema operativo que se utilice, sea cual fuere
	#la lista que contiene fuente1 y fuente2 deberia contener las fuentes disponibles
	lista_fuentes = []
	layout = [[sg.InputCombo(lista_fuentes, default_value='Seleccionar')],
			  [sg.Button('OK')]
	]
	
	window = sg.Window('Configuración').Layout(layout)
	while True:
		event, values = window.Read()
	if event == 'OK':
		font = values

	return font

def Orientacion():
	'''Esta funcion permite elegir la orientación que tendrán
	las palabras dentro de la sopa de letras. Retorna la opción
	seleccionada.'''

	layout =  [
    [sg.Text('Seleccione cómo se mostrarán las letras:')],
    [sg.Radio('Horizontal', "RADIO1", default=True),
    sg.Radio('Vertical', "RADIO1")],
    [sg.Button('OK')]
	]
	
	window = sg.Window('Configuración').Layout(layout)
	while True:
		event, values = window.Read()
	if event == 'OK':
		orientation = values

	return orientation
	
#cant palabras
def Cant():
	'''Esta función permite indicar cuántas palabras serán
	ingresadas en la sopa de letras. Retorna la cantidad
	seleccionada en un diccionario.'''

	layout =  [
				[sg.Spin([i for i in range(1,6)], initial_value=1), sg.Text('Sustantivos')],
				[sg.Spin([i for i in range(1,6)], initial_value=1), sg.Text('Adjetivos')],
				[sg.Spin([i for i in range(1,6)], initial_value=1), sg.Text('Verbos')],
				[sg.Button('OK')]
				]
	window = sg.Window('Configuración').Layout(layout)
	while True:
		event, values = window.Read()
		#print(values)
		if event == 'OK':
			cantidad = values
	window.Close()

	return cantidad

#layout ventana
#config ventana
#layout = [
#          [sg.Button('Aplicar')],[sg.Button('Cerrar')]
#]
#window = sg.Window('Ventana de configuración').Layout(layout)

#while True:
#	event, values = window.Read()
#	print(values)
#	if event == 'OK':
#		print('OK')
#window.Close()
