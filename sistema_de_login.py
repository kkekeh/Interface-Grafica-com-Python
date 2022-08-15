import PySimpleGUI as sg

# Sistema simples de login.

# Dados do usuário.
data = {
    'usuario': 'Fulano',
    'senha': '1234'
}  

# Layout do programa.
layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='-USUARIO-')],
    [sg.Text('Senha')],
    [sg.Input(key='-SENHA-')],
    [sg.Button('login')],
    [sg.Text(key='-OUTPUT-')]
]

window = sg.Window('Login', layout)  # Tela (programa).

while True:
    event, values = window.read()  # Dados da janela.

    if event == 'login':
        user = values['-USUARIO-']
        password = values['-SENHA-']

        if user == data['usuario'] and password == data['senha']:
            window['-OUTPUT-'].update('Login efetuado com sucesso!')
        else:
            window['-OUTPUT-'].update('Usuário e/ou senha inválidos!')

    # Se o programa for fechado, encerra o loop.
    if event == sg.WIN_CLOSED:
        break

window.close()  # Fecha a janela.
