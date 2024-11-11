import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
from PIL import Image, ImageTk, ImageFilter
import os
import json
import pyzbar
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.button import Button
from pyzbar.pyzbar import decode
from PIL import Image as PILImage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import olefile

# Cargando las credenciales de Google Sheets
creds = None
creds_filename = '/Users/fernandapenaaraya/Downloads/service_account.json'
if os.path.exists(creds_filename):
    with open(creds_filename) as f:
        creds_data = json.load(f)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_data)

# Conectando a la hoja de Google # Configuración de las credenciales de Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    '/Users/fernandapenaaraya/Downloads/service_account.json', scope)
client = gspread.authorize(credentials)
sheet = client.open_by_url(
    'https://docs.google.com/spreadsheets/d/1F62X8Udm7Ypk0Ghyyytgw5HKLozgZfqaoKLYaKcnaRA/edit#gid=0').worksheet("Datos")

# Cargando el archivo kv para el diseño de la app
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    Button:
        text: 'Tomar foto'
        size_hint_y: None
        height: '48dp'
        on_release: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        # Tomar la foto y guardarla en un archivo temporal
        camera = self.ids['camera']
        img_filename = 'temp.jpg'
        camera.export_to_png(img_filename)

        # Leer el código de barras de la imagen
        img = PILImage.open(img_filename)
        barcode = decode(img)
        barcode_data = barcode[0].data.decode('utf-8') if barcode else ''

        # Agregar los datos a la hoja de Google Sheets
        if creds and barcode_data:
            data = ['campo1', 'campo2', 'campo3',
                    'campo4', 'campo5', 'campo6', 'campo7']
            data[0], data[1], data[2], data[3], data[4], data[5], data[6] = barcode_data.split(
                ',')
            sheet.append_row(data)


class MyApp(App):
    def build(self):
        return CameraClick()


if _name_ == '_main_':
    MyApp().run()
