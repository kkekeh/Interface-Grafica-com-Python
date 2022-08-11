import PySimpleGUI as sg
import base64
from PIL import Image
from io import BytesIO
from pygame import mixer, time

mixer.init()  # Inicializa o mixer.
clock = time.Clock()

#

path = sg.popup_get_file('Abrir', no_window=True)  # O usuário faz a busca do som.
song_name = path.split('/')[-1].split('.')[0]  # Pega apenas o nome do som (string).
song = mixer.Sound(path)

song_length = int(song.get_length())  # Pega o tempo do som (segundos).
time_since_start = 0
pause_amount = 0
playing = False


def base64_image_import(path):
    image = Image.open(path)
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    b64 = base64.b64encode(buffer.getvalue())

    return b64


sg.theme('Reddit')

play_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text(song_name, font='Arial 20'), sg.Push()],
    [   
        sg.Push(),
        sg.Button(
            image_data=base64_image_import('music_player/play.png'),
            button_color='white',
            border_width=0,
            key='-PLAY-'
            ),
        sg.Text(' '),
        sg.Button(
            image_data=base64_image_import('music_player/pause.png'),
            button_color='white',
            border_width=0,
            key='-PAUSE-'
            ),
        sg.Push()
    ],
    [sg.Progress(song_length, size=(20, 20), key='-PROGRESSO-')],
    [sg.VPush()]
]
volume_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Slider(range=(0, 100), default_value=50, orientation='h', key='-VOLUME-'), sg.Push()],
    [sg.VPush()]
]

# Layout do programa.
layout = [
    [sg.TabGroup([[sg.Tab('Play', play_layout), sg.Tab('Volume', volume_layout)]])]
]

window = sg.Window('Music Player', layout)  # Tela (programa).

while True:
    event, values = window.read(timeout=60)  # Dados da janela.

    if playing:
        time_since_start = time.get_ticks()
        
        window['-PROGRESSO-'].update((time_since_start - pause_amount) / 1000)

    if event == '-PLAY-':
        playing = True
        pause_amount += time.get_ticks() - time_since_start
        
        if not mixer.get_busy():
            song.play()
        else:
            mixer.unpause()
    
    if event == '-PAUSE-':
        mixer.pause()

        playing = False

    song.set_volume(values['-VOLUME-'] / 100)

    # Se o programa for fechado, encerra o loop.
    if event == sg.WIN_CLOSED:
        break
        
window.close()  # Fecha a janela.
