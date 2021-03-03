import PySimpleGUI as gui
from generator import Generator


gui.theme('DarkAmber')

#Simple Vars
str_length = ""
no_of_codes = ""
url_base = ""
chosen_path = ""

#Arrays
data_for_export = [None] * 39

#["Azonosító", "Típus", "Cikkszám", "Név", "Közzétéve", "Kiemelt?", "Látható a katalógusban", "Rövid leírás", "Leírás", "Akciós ár kezdődátuma", "Akciós ár végdátuma", "Adó státusz", "Adózási osztály", "Raktáron?", "Készlet", "Alacsony készlet mennyiség", "Függő rendelés engedélyezése?", "Egyedileg értékesíthető?", "Tömeg (kg)", "Hosszúság (cm)", "Szélesség (cm)", "Magasság (cm)", "Engedélyezzük az értékelést?", "Vásárlási megjegyzés", "Akciós ár", "Normál ár", "Kategória", "Címkék", "Szállítási osztály", "Képek", "Letöltési korlát", "Letöltés lejárati napok", "Szülő", "Csoportosított termék", "Upsell", "Keresztértékesítés", "Külső URL", "Gomb Szövege", "Pozíció"]


#Spinners

#Közzétéve: 1,      Privát: 0,      Piszkozat: -1,
kozzeteve_spinner = gui.Spin(values=('1', '0', '-1'), initial_value='1', size=(10, 1))

#Rejtett - "hidden",        Látható - "visible"     Katalógus - "catalog"     Keresés - "search"
lathato_katalogusban_spinner = gui.Spin(values=('hidden', 'visible', 'catalog', 'search'), initial_value='hidden', size=(10, 1))


########################################################################################################################################
##  Code Start ##
########################################################################################################################################


##Columns
base_ui_column = [  [gui.Text('Karakterlánc hossza:', size=(20,1)), gui.InputText()],
            [gui.Text('QR kódok száma:', size=(20,1)), gui.InputText()],
            [gui.Text('Alap URL:', size=(20,1)), gui.InputText()],
            [gui.Text('Képek mentése:  ', size=(20,1)), gui.Text('Válaszd ki, hova szeretnéd menteni!', key="PATH", text_color="white"), gui.Button('Módosítás')],
            [gui.Text('Eddig minden rendben!', text_color="green", key="WARNING", size=(20,1))],
            [gui.Button('Ok', size=(20,1)), gui.Button('Mégsem')],
]

tovabbi_beallitasok_column1 = [ [gui.Text('Típus', size=(20,1)), gui.InputText(default_text="simple, virtual", tooltip="3 opció van: \n1. simple \n2.variation \n3. virtual \nAlap QR kódhoz 'simple, virtual' kell. \nUgyan ebben a formátumban lehet többet, más variációt egybetenni.")],
            [gui.Text('Közzétéve', size=(20,1)), kozzeteve_spinner],
            [gui.Text('Látható katalógusban?', size=(20,1)), lathato_katalogusban_spinner],
            [gui.Text('Rövid leírás', size=(20,1)), gui.InputText()],
            [gui.Text('Leírás', size=(20,1)), gui.InputText()],
            [gui.Text('Kategória', size=(20,1)), gui.InputText(default_text="qractivate", tooltip="Fontos, hogy pontosan add meg a kategória nevét! \nAlap kategória(általában jó lesz): qractivate")],
            [gui.Text('Címkék', size=(20,1)), gui.InputText(tooltip="Fontos, hogy pontosan add meg a címke/címkék nevét! \nHa több kategóriát adsz meg, válaszd el vesszővel, szőközök nélkül! \nPéldául: nyakörv")],
            [gui.Text('Normál ár', size=(20,1)), gui.InputText(tooltip="Add meg a termék árát!")]
]

layout = [  [gui.Column(base_ui_column)],
            [gui.Column(tovabbi_beallitasok_column1)],
]

window = gui.Window('QR kódgenerálás', layout)

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
            """tipus = values[3]
            kozzeteve = values[4]
            lathato_katalogusban = values[5]
            rovid_leiras = values[6]"""
            

            print(type(string_length), type(no_of_codes), type(url_base))

            gen = Generator(no_of_codes)
            gen.generate_qr(string_length, no_of_codes, url_base, chosen_path, values)

            window["WARNING"].update("A kódok készen vannak!", text_color="green")
            print(values)
        else:
            window["WARNING"].update("Helytelen értékek!", text_color="red")
            
    

    

    