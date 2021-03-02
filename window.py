import PySimpleGUI as gui
from generator import Generator


gui.theme('DarkAmber')

#Vars
str_length = ""
no_of_codes = ""
url_base = ""
chosen_path = ""



layout = [  [gui.Text('QR-kód generálás')],
            [gui.Text('Karakterlánc hossza:'), gui.InputText()],
            [gui.Text('QR kódok száma:'), gui.InputText()],
            [gui.Text('Alap URL:'), gui.InputText()],
            [gui.Text('Képek mentése:  '), gui.Text('Válaszd ki, hova szeretnéd menteni!', key="PATH", text_color="white"), gui.Button('Módosítás')],
            [gui.Text('Eddig minden rendben!', text_color="green", key="WARNING")],
            [gui.Button('Ok'), gui.Button('Mégsem')]]

window = gui.Window('QR Generátor', layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Mégsem':
        break
    if event == 'Módosítás':
        chosen_path = gui.popup_get_folder("Válassz mappát!", "Mentési hely változtatása", keep_on_top=True)
        window['PATH'].update(chosen_path)
    if event == "Ok":
        url_is_string = isinstance(values[2], str)
        #Check if numbers are numbers, strings are strings, and none of the values are empty
        #Then assign values
        if values[0].isdigit and values[1].isdigit() and url_is_string:
            string_length = values[0]
            no_of_codes = values[1]
            url_base = values[2]
            #chosen_path

            print(type(string_length), type(no_of_codes), type(url_base))

            gen = Generator(no_of_codes)
            gen.generate_qr(string_length, no_of_codes, url_base, chosen_path)

            window["WARNING"].update("A kódok készen vannak!", text_color="darkgreen")
        else:
            window["WARNING"].update("Helytelen értékek!", text_color="red")
    