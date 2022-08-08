import PySimpleGUI as sg
from pathlib import Path

# Bloco de Anotações simples.

smileys = [
    'happy', [':)'],
    'sad', [':c'],
    'other', [':3']
]

smiley_events = smileys[1] + smileys[3] + smileys[5]

# Layout do menu.
menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', ['emoji', smileys]]
]

sg.theme('GrayGrayGray')

# Layout do programa.
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Sem título', key='-DOCNAME-')],
    [sg.Multiline(size=(40, 30), no_scrollbar=True, key='-TEXTBOX-')]
]

window = sg.Window('Bloco de notas', layout)  # Tela (programa).

while True:
    event, values = window.read()  # Dados da janela.

    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window=True)

        if file_path:
            file = Path(file_path)
            
            window['-DOCNAME-'].update(file_path.split('/')[-1])
            window['-TEXTBOX-'].update(file.read_text())
            
    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True) + '.txt'
        file = Path(file_path)
        
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n',' ').split()
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        
        sg.popup(f'words: {word_count}\ncharacters: {char_count}')

    if event in smiley_events:
        current_text = values['-TEXTBOX-']
        new_text = current_text + ' ' + event
        
        window['-TEXTBOX-'].update(new_text)

    # Se o programa for fechado, encerra o loop.
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()  # Fecha a janela.
