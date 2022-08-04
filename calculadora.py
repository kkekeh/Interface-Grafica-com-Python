import PySimpleGUI as sg

# Calculadora simples (sim, contém bugs).

theme_menu = ['Menu', ['LightGrey1', 'DarkGrey8', 'Random']]  # Cores do tema.
button_size = (6, 3)  # Tamanho do botão.
current_number = []  # Número atual.
operation = []  # Cálculo.


def create_window(theme):
    # TEMA
    sg.theme(theme)  
    sg.set_options(font='Franklin 14', button_element_size=(6, 3))

    # Layout do programa.
    layout = [
        [sg.Text(
            '0',
            font='Franklin 26',
            justification='right',
            expand_x=True,
            pad=(10, 20),
            right_click_menu=theme_menu, key='-TEXTO-'
            )
        ],  # Mensagem do resultado.

        # BOTÕES
        [
            sg.Button('Limpa', key='-LIMPA-', expand_x=True),
            sg.Button('Entra', key='-ENTRA-', expand_x=True)
        ],
        [
            sg.Button('7', size=button_size),
            sg.Button('8', size=button_size),
            sg.Button('9', size=button_size),
            sg.Button('/', size=button_size)
        ],
        [
            sg.Button('4', size=button_size),
            sg.Button('5', size=button_size),
            sg.Button('6', size=button_size),
            sg.Button('*', size=button_size)
        ],
        [
            sg.Button('1', size=button_size),
            sg.Button('2', size=button_size),
            sg.Button('3', size=button_size),
            sg.Button('-', size=button_size)
        ],
        [
            sg.Button('0', expand_x=True),
            sg.Button('.', size=button_size),
            sg.Button('+', size=button_size)
        ]
    ]

    return sg.Window('Calculadora', layout)


window = create_window(theme_menu[1][0])  # Tela (programa).

while True:
    event, values = window.read()  # Dados da janela.

    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_number.append(event)

        number_string = ''.join(current_number)
        
        window['-TEXTO-'].update(number_string)
    
    if event in ['+', '-', '*', '/']:
        operation.append(''.join(current_number))
        current_number.clear()
        operation.append(event)
        window['-TEXTO-'].update('')
    
    if event == '-ENTRA-':
        operation.append(''.join(current_number))

        result = eval(''.join(operation))

        window['-TEXTO-'].update(result)
        operation.clear()
    
    if event == '-LIMPA-':
        current_number.clear()
        operation.clear()
        window['-TEXTO-'].update('')

    # Muda o tema.
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    # Se o programa for fechado, encerra o loop.
    if event == sg.WIN_CLOSED:
        break

window.close()  # Fecha a janela.
