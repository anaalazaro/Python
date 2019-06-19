import PySimpleGUI as sg

def ColorChooser(): #chequear si devuelve un color
	'''Muestra una carta de colores luego de unos segundos.
    Una vez mostrada la ventana grande, se puede clickear en cualquier color
    y se generará otra ventana mostrando el texto en ese color sobre fondos
    blanco y negro'''



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
			print(values)
	window.Close()
	
	return event

colorcito=ColorChooser()
print(colorcito)

