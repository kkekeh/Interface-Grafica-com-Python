import PySimpleGUI as sg

# Programa para a conversão de valores.

# Layout do programa.
layout = [
    [
        sg.Input(key='-INPUT-'),  # Input do usuário.
        sg.Spin(['km/mi', 'kg/lb', 'seg/min'], key='-UNITS-'),  # Unidades de conversão.
        sg.Button('Converte', key='-CONVERTE-')  # Botão de conversão.
    ],
    [sg.Text(key='-OUTPUT-')]  # Mensagem do resultado.
]

window = sg.Window('Conversor', layout)  # Tela (programa).

while True:
    event, values = window.read()  # Dados da janela.
    
    if event == '-CONVERTE-':
        input_value = values['-INPUT-']
        
        if input_value.isnumeric():
            # Verifica as unidades e as converte corretamente.
            match values['-UNITS-']:
                # Quilômetro p/ milha.
                case 'km/mi':
                    output = round(float(input_value) * 0.621371, 2)
                    output_string = f'{input_value}km é {output}mi'
                # Quilo p/ libra.
                case 'kg/lb':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value}kg é {output}lb'
                # Segundo p/ minuto.
                case 'seg/min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} segundo(s) é {output} minuto(s)'
            
            window['-OUTPUT-'].update(output_string)  # Atualiza o resultado.
        else:
            window['-OUTPUT-'].update('ERRO! Informe apenas números...')
    
    # Se o programa for fechado, encerra o loop.
    if event == sg.WIN_CLOSED:
        break
        
window.close()  # Fecha a janela.
