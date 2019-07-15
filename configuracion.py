import PySimpleGUI as sg
import funciones_CONFIG as fc
import Wik_y_pattern as wp
import funciones_AYUDA as fa

def Config():
    ''' Esta función abre la ventana general de configuración y en cada pestaña permite configurar cada característica
	de la sopa de letras. Al presionar "Aplicar", se guardan los cambios. Si una o más características no fueron configuradas
	por el usuario, adoptarán los valores por defecto dados por esta misma función. Retorna un diccionario con todas las selecciones.'''
    
    #Lista de fuentes disponibles para el programa:
    lista_fuentes = ["Arial", "Helvetica", "Times New Roman", "Courier", "Verdana", "Georgia",
    "Garamond", "Bookman", "Comic Sans MS", "Trebuchet MS", "Arial Black", "Impact"]

    #Layout de la Tab para configurar los colores:
    colores_layout = layout =  [
        [sg.Text('Seleccione un color para cada tipo de palabra. Al finalizar presione "OK".')],
        [sg.Text('Color para sustantivos', key='color_S'), sg.Button('.', button_color = ('black','cadet blue'))],
        [sg.Text('Color para adjetivos', key='color_A'), sg.Button('..', button_color = ('black','cadet blue'))],
        [sg.Text('Color para verbos', key='color_V'), sg.Button('...', button_color = ('black','cadet blue'))]
	    ]  

    #Layout del Frame para configurar la fuente:
    tipografia_fuente_layout = [      
                  [sg.Text('Seleccione una fuente para las letras:')],      
                  [sg.Combo(lista_fuentes, default_value='Helvetica', key='fuente')]      
               ]
    #Layout del Frame para configurar si las letras se mostrarán en mayúscula o minúscula:
    tipografia_mayus_minus_layout = [      
                  [sg.Text('Seleccione cómo se mostrarán las letras:')],
                  [sg.Radio('Mayúscula', "RADIO1", default=True, key='mayus'),
                   sg.Radio('Minúscula', "RADIO1", key='minus')]     
               ]

    #Layout de la Tab para configurar la tipografía:
    tipografia_layout = [      
          [sg.Frame('Fuente', tipografia_fuente_layout, font='Any 8', title_color='cadet blue')],
          [sg.Frame('Caps', tipografia_mayus_minus_layout, font='Any 8', title_color='cadet blue')]     
         ]

    #Layout de la Tab para configurar el tipo de ayuda a utilizar:
    ayuda_layout = [
			[sg.Radio('Sin ayuda', "RADIO2", size=(10,1), key='sin_ayuda', default=True), sg.Radio('Mostrar definiciones', "RADIO2", key='con_definiciones'), 
			 sg.Radio('Mostrar palabras', "RADIO2", key='con_palabras'), sg.Radio('Mostrar definiciones y palabras', "RADIO2", key='con_ayuda')]
         ]

    #Layout del Frame para configurar las palabras a hallar:
    contenido_palabras_layout = [
		  [sg.Input(default_text='Ingrese una palabra', key='in'), sg.Submit('Ingresar')],
		  [sg.Listbox(values=[], size=(30, 6), key='palabra_seleccionada')],
          [sg.Button('Eliminar', tooltip='Seleccione una palabra y oprima el botón para eliminarla')]
		 ]

    #Layout del Frame para configurar la cantidad de palabras a hallar:
    contenido_cantidad_palabras_layout = [
				[sg.Spin([i for i in range(0,6)], initial_value=1, key='cant_S'), sg.Text('Sustantivos')],
				[sg.Spin([i for i in range(0,6)], initial_value=1, key='cant_A'), sg.Text('Adjetivos')],
				[sg.Spin([i for i in range(0,6)], initial_value=1, key='cant_V'), sg.Text('Verbos')]
				]

    #Layout del Frame para configurar la orientación de las palabras a hallar:
    contenido_orientacion_layout = [
				[sg.Text('Seleccione cómo se mostrarán las letras:')],
				[sg.Radio('Horizontal', "RADIO3", default=True, key='horizontal'),
				sg.Radio('Vertical', "RADIO3", key='vertical')]
		 ]

    #Layout de la Tab para configurar el contenido de la sopa de letras:
    contenido_layout =  [      
          [sg.Frame('Palabras', contenido_palabras_layout, font='Any 8', title_color='cadet blue')],
          [sg.Frame('Cantidad', contenido_cantidad_palabras_layout, font='Any 8', title_color='cadet blue')],
          [sg.Frame('Orientación', contenido_orientacion_layout, font='Any 8', title_color='cadet blue')]      
         ]

    #Layout de la ventana de configuración:
    layout = [[sg.TabGroup([[sg.Tab('Colores', colores_layout), sg.Tab('Tipografía', tipografia_layout), 
           sg.Tab('Ayuda', ayuda_layout), sg.Tab('Contenido', contenido_layout)]])],
           [sg.Submit('Aplicar', tooltip='Al presionar este botón todos los cambios serán guardados')]
          ]    

    window = sg.Window('Configuración', layout, default_element_size=(24,1)).Finalize()

    #Establezco valores por defecto en caso de que el usuario no establezca sus propios valores:
    colours = {'Sustantivo': 'spring green', 'Adjetivo': 'sky blue', 'Verbo': 'coral'}
    tipografia = {'font': 'Helvetica', 'caps': 'mayuscula'}
    cant_palabras = {'cant_Sust': '0', 'cant_Adjt': '0', 'cant_Verb': '0'}
    lista_palabras = []
    diccionario_palabras = {}
    ayuda = {'sin_ayuda':True, 'definiciones':False, 'palabras':False, 'con_ayuda':False}
    datos_configurados = {'colores':colours, 'tipografia': tipografia, 'cant_palabras': cant_palabras, 'palabras': lista_palabras, 'diccionario': diccionario_palabras, 'orientacion': 'horizontal'}

    while True:
        event, values = window.Read()    
        print(event,values)    
        if event is None:    
            break
        #Los colores se pueden elegir múltiples veces, el último seleccionado es el que se guarda:
        if event is '.':
            colours['Sustantivo'] = fc.ColorChooser()
            colores_layout[1][1].Update(button_color=('black', colours['Sustantivo']))
        if event is '..':
            colours['Adjetivo'] = fc.ColorChooser()
            colores_layout[2][1].Update(button_color=('black', colours['Adjetivo']))
        if event is '...':
            colours['Verbo'] = fc.ColorChooser()
            colores_layout[3][1].Update(button_color=('black', colours['Verbo']))
        #Al ingresar una palabra se verifica que no haya sido ingresada previamente:
        if event is 'Ingresar':
            if values['in'] not in lista_palabras:
                validada = wp.validacion(values['in'], diccionario_palabras)['validez']
                #Una vez validada, se agrega a la lista de palabras:
                if validada:
                    lista_palabras.append(values['in'])
                    contenido_palabras_layout[1][0].Update(values=lista_palabras)
                else:
                    sg.Popup('La palabra no puede ingresarse.')
                palabra_pattern=wk.de_pattern(values["in"])
                comparado=wk.comparando(palabra_pattern,diccionario_palabras[values["in"]])
                if (comparado=="No coinciden"):
                    wk.no_coinciden(values["in"],diccionario_palabras[values["in"]]["Tipo"],palabra_pattern[1])
                elif comparado=="No se encontró la palabra":
                    wk.no_existen(values["in"])  
        #Si se oprime 'Eliminar' se elimina la palabra seleccionada:
        if event is 'Eliminar' and values['palabra_seleccionada'][0] in lista_palabras:
            lista_palabras.remove(values['palabra_seleccionada'][0])
            contenido_palabras_layout[1][0].Update(values=lista_palabras)
        
        #Si se oprime 'Aplicar', se efectuarán los cambios:
        if event is 'Aplicar':
		    #Guardo la configuración de tipografía en el diccionario:
            tipografia['font'] = values['fuente']
            if values['minus']:
                tipografia['caps'] = 'minuscula'
            else:
                tipografia['caps'] = 'mayuscula'
            #Guardo la configuración de cantidad de palabras en el diccionario:
            cant_palabras['cant_Sust'] = values['cant_S']
            cant_palabras['cant_Adjt'] = values['cant_A']
            cant_palabras['cant_Verb'] = values['cant_V']
            #Aquí guarda la configuración de Ayuda:
            
            ayuda = {'sin_ayuda': values['sin_ayuda'], 'definiciones': values['con_definiciones'], 'palabras': values['con_palabras'], 'con_ayuda': values['con_ayuda']}
            
            print(ayuda)
            #Guardo la orientación de las palabras en la sopa de letras:
            if values['vertical']:
                orientacion = 'vertical'
            else:
                orientacion = 'horizontal'
            #Finalmente, guardo todo lo anterior en un solo diccionario y lo retorno:
            datos_configurados = {'colores':colours, 'tipografia': tipografia, 'cant_palabras': cant_palabras, 'palabras': lista_palabras, 'diccionario': diccionario_palabras, 'orientacion': orientacion, 'ayuda': ayuda}
            print(datos_configurados)
            break     
    window.Close()
                
    return datos_configurados
