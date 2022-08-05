import PySimpleGUI as sg
from time import time

# Cronômetro básico.

start_time = 0
lap_amount = 1
active = False

sg.theme('Black')  # Tema do programa.


def create_window():
    # Layout do programa.
    layout = [
        [sg.Push(), sg.Image('cronometro/x.png', pad=0, enable_events=True, key='-CLOSE-')],
        [sg.VPush()],
        [sg.Text('', font='Franklin 50', key='-TIMER-')],
        [
            sg.Button('Start', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-STARTSTOP-'),
            sg.Button('Lap', button_color=('#FFFFFF', '#FF0000'), border_width=0, visible=False, key='-LAP-')
        ],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()]
    ]

    return sg.Window(
        'Cronômetro',
        layout,
        size=(300, 300),
        no_titlebar=True,
        element_justification='center')  # Tela (programa).


window = create_window()

while True:
    event, values = window.read(timeout=10)  # Dados da janela.

    if event == '-STARTSTOP-':
        # De ativo p/ parado.
        if active:
            active = False
            
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible=False)
        else:
            # De parado p/ resetar.
            if start_time > 0:
                window.close()

                window = create_window()
                start_time = 0
                lap_amount = 1
            # Do começo p/ ativar.
            else:
                start_time = time()
                active = True

                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible=True)
    
    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        
        lap_amount += 1

    if active:
        elapsed_time = round(time() - start_time, 1)
        
        window['-TIMER-'].update(elapsed_time)

    # Se clicar no "x", encerra o programa.
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break
        
window.close()  # Fecha a janela.
