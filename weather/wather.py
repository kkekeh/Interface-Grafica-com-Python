import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup as bs

# Programa que verifica condições meteorológicas.


# Retorna dados meteorológicos.
def get_weather_data(location):
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    url = f'https://www.google.com/search?q=weather+{location.replace(" ", "")}'
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    html = session.get(url)

    # Nova soup.
    soup = bs(html.text, 'html.parser')
    location = soup.find('div', attrs={'id': 'wob_loc'}).text
    time = soup.find('div', attrs={'id': 'wob_dts'}).text
    temp = soup.find('span', attrs={'id': 'wob_tm'}).text
    weather = soup.find('span', attrs={'id': 'wob_dc'}).text
    
    return location, time, temp, weather


sg.theme('Reddit')

symbol_col = sg.Column([[sg.Image(key='-IMAGE-', background_color='#FFFFFF')]])
info_col = sg.Column([
	[sg.Text('', font='Calibri 30', text_color='#FFFFFF', background_color='#FF0000',
            pad=0, visible=False, key='-LOCATION-')],
	[sg.Text('', font='Calibri 16', text_color='#FFFFFF', background_color='#000000',
            pad=0, visible=False, key='-TIME-')],
	[sg.Text('', font='Calibri 16', text_color='#000000', background_color='#FFFFFF',
            pad=(0, 10), justification='center', visible=False, key='-TEMP-')]
    ])

# Layout do programa.
layout = [
    [sg.Input(key='-INPUT-'), sg.Button('Pesquisar', button_color='#000000', border_width=0)],
    [symbol_col, info_col]
]

window = sg.Window('Weather', layout)  # Tela (programa).

while True:
    event, values = window.read()  # Dados da janela.

    if event == 'Pesquisar':
        location, time, temp, weather = get_weather_data(values['-INPUT-'])
        
        window['-LOCATION-'].update(location, visible=True)
        window['-TIME-'].update(time.split()[0].replace(',', ''), visible=True)
        window['-TEMP-'].update(f'{temp} \u2103 ({weather})', visible=True)

    # Sol
    if weather in ('Sol','Ensolarado','Limpo'):
        window['-IMAGE-'].update('weather/simbolos/sol.png')
	
    # Nublado
    if weather in ('Nublado', 'Parcialmente nublado'):
        window['-IMAGE-'].update('weather/simbolos/nublado.png')
    
    # Chuva
    if weather in ('Chuva', 'Pancadas de chuva', 'Pancadas esparsas de chuva'):
        window['-IMAGE-'].update('weather/simbolos/chuva.png')
    
    # Trovões
    if weather in ('Trovões', 'Chuvas com trovoadas', 'Tempestades isoladas com raios e trovões'):
        window['-IMAGE-'].update('weather/simbolos/trovoes.png')

    # Névoa
    if weather in ('Névoa', 'Nevoeiro'):
        window['-IMAGE-'].update('weather/simbolos/nevoa.png')
    
    # Neve
    if weather in ('Neve', 'Nevando'):
        window['-IMAGE-'].update('weather/simbolos/neve.png')
        
    # Se o programa for fechado, encerra o loop.
    if event == sg.WIN_CLOSED:
        break
        
window.close()  # Fecha a janela.
