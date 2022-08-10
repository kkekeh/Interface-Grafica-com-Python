import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

# Editor de imagens simples.

image_path = sg.popup_get_file('Abrir', no_window=True)  # O usuário faz a busca da imagem.
original = Image.open(image_path)


def update_image(original, blur, contraste, relevo, contorno, flip_x, flip_y):
    global image

    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contraste))
    bio = BytesIO()

    if relevo:
        image = image.filter(ImageFilter.EMBOSS())
    
    if contorno:
        image = image.filter(ImageFilter.CONTOUR())
    
    if flip_x:
        image = ImageOps.mirror(image)

    if flip_y:
        image = ImageOps.flip(image)

    image.save(bio, format='PNG')
    window['-IMAGEM-'].update(data=bio.getvalue())


control_col = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contraste', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-CONTRASTE-')]])],
    [sg.Checkbox('Relevo', key='-RELEVO-'), sg.Checkbox('Contorno', key='-CONTORNO-')],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip y', key='-FLIPY-')],
    [sg.Button('Salvar imagem', key='-SALVAR-')]])  # Coluna das configurações.
image_col = sg.Column([[sg.Image(image_path, key='-IMAGEM-')]])

# Layout do programa.
layout = [[control_col, image_col]]

window = sg.Window('Editor de Imagem', layout)  # Tela (programa).

while True:
    event, values = window.read(timeout=60)  # Dados da janela.

    update_image(
        original,
        values['-BLUR-'],
        values['-CONTRASTE-'],
        values['-RELEVO-'],
        values['-CONTORNO-'],
        values['-FLIPX-'],
        values['-FLIPY-'])

    if event == '-SAVE-':
        file_path = sg.popup_get_file('Salvar como', save_as=True, no_window=True) + '.png'
        
        image.save(file_path, 'PNG')

    # Se o programa for fechado, encerra o loop.
    if event == sg.WIN_CLOSED:
        break
        
window.close()  # Fecha a janela.
