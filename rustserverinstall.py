import os
import shutil
import zipfile
import urllib.request
import subprocess
import requests

import flet as ft
from flet import theme, ThemeMode

# Ventana
def main(page: ft.Page):

    #Titulo Pagina + opciones
    page.title = "Instalador de Rust Server"
    page.theme = theme.Theme(ft.colors.DEEP_ORANGE_ACCENT_200)
    page.dark_theme = theme.Theme(ft.colors.DEEP_ORANGE_ACCENT_200)
    page.theme_mode = "ligth"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    #page.splash = ft.ProgressBar()

    page.window_height = 500
    page.window_width = 640
    page.window_min_height = 500
    page.window_min_width = 640
    
    page.window_center()


   # page.bgcolor = ft.colors

    # Variables reutilizables

    # Rutas de carpetas
    carpeta_cero = os.getcwd()

    carpeta_principal = os.path.join(os.getcwd(), 'RUST SERVER')
    steamcmd_carpeta = os.path.join(carpeta_principal, 'STEAMCMD')
    carpeta_rust = os.path.join(carpeta_principal, 'SERVER')

    if carpeta_principal and steamcmd_carpeta:
        titulo_install = "Instalador de Rust Server"
    else:
        titulo_install = "Actualizador de Rust Server"

    opciones_sub = "¿ Qué desea hacer ?"


    # Funciones de los botones
    def steam(e):
        if steamcmd_carpeta:
            texto2.value = "Reinstalando SteamCMD"
            page.update()
        else:
            texto2.value = "Instalando SteamCMD"
            page.update()


        # Elimina el directorio `steamcmd_dir` si existe, ignorando cualquier error que pueda ocurrir.
        shutil.rmtree(steamcmd_carpeta, ignore_errors=True)

        # Crea el directorio `steamcmd_dir`.
        os.makedirs(steamcmd_carpeta)

        # Define una variable `url` que contiene la URL para descargar `steamcmd.zip`.
        url = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'

        # Descarga el archivo `steamcmd.zip` de la URL especificada y lo guarda en el directorio de trabajo actual.
        urllib.request.urlretrieve(url, 'steamcmd.zip')

        # Abre el archivo `steamcmd.zip` y extrae su contenido en el directorio `steamcmd_dir`.
        with zipfile.ZipFile('steamcmd.zip', 'r') as zip_ref:
            zip_ref.extractall(steamcmd_carpeta)

        # Elimina el archivo `steamcmd.zip`.
        os.remove('steamcmd.zip')

        # Cambia el directorio de trabajo actual a `steamcmd_dir`.
        os.chdir(steamcmd_carpeta)

        # Define una variable `cmd` que contiene el comando para ejecutar Steamcmd y cerrarlo después de completar todas las tareas pendientes.
        cmd = "START cmd /c steamcmd +quit && exit"

        # Ejecuta el comando especificado en `cmd` usando `subprocess.call()`.
        subprocess.call(cmd, shell=True)

        #process = subprocess.Popen(cmd, shell=True)
        #process.wait()

        if texto2.value == "Reinstalando SteamCMD":
            texto2.value = "Reinstalación completa"
            page.update()
        else:
            texto2.value = "Instalación completa"
            page.update()

        os.chdir(carpeta_cero)

    def rust(e):
       
        # Crea la carpeta si no existe
        os.makedirs(carpeta_rust, exist_ok=True)

        # Verifica si steamcmd está instalado
        if os.path.exists(os.path.join(steamcmd_carpeta, 'steamcmd.exe')):
            
             # Cambia el directorio de trabajo actual a `steamcmd_carpeta`.
            os.chdir(steamcmd_carpeta)

            # Define una variable `cmd` que contiene el comando para ejecutar Steamcmd y cerrarlo después de completar todas las tareas pendientes.
            cmd = f'START cmd /c steamcmd +login anonymous +force_install_dir "{carpeta_rust}" +app_update 258550 validate +quit && exit'

            # Ejecuta el comando especificado en `cmd` usando `subprocess.call()`.
            subprocess.call(cmd, shell=True)
       
        os.chdir(carpeta_cero)


    def oxide(e):
         # URL del sitio web de uMod para descargar la última versión de Oxide para Rust
        url = 'https://umod.org/games/rust/download'

        # Realiza una solicitud GET a la URL
        response = requests.get(url, stream=True)

        # Define la ruta del archivo .zip en la carpeta_principal
        ruta_zip = os.path.join(carpeta_principal, 'Oxide.Rust.zip')

        # Si la solicitud fue exitosa, procede a descargar el archivo
        if response.status_code == 200:
            with open(ruta_zip, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f) 

        # Abre el archivo 'Oxide.Rust.zip' y extrae su contenido en el directorio 'carpeta_rust'
        with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
            zip_ref.extractall(carpeta_rust)

        # Elimina el archivo temporal 'Oxide.Rust.zip'
        os.remove(ruta_zip)
        
        # Verifica si el directorio 'RustDedicated_Data' existe en el directorio 'carpeta_rust'
        if os.path.exists(os.path.join(carpeta_rust, 'RustDedicated_Data')):
            # Copia el contenido del directorio 'RustDedicated_Data' en el directorio raíz del servidor
            src_dir = os.path.join(carpeta_rust, 'RustDedicated_Data')
            dst_dir = os.path.join(carpeta_rust, 'RustDedicated_Data')
            for item in os.listdir(src_dir):
                src_item = os.path.join(src_dir, item)
                dst_item = os.path.join(dst_dir, item)
                if src_item != dst_item:  # Asegúrate de que el archivo de origen y el de destino no sean el mismo
                    if os.path.isdir(src_item):
                        shutil.copytree(src_item, dst_item, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src_item, dst_item)
            
            print('Instalación completada')
        else:
            print('Error: no se encontró el directorio RustDedicated_Data')

    def eliminar(e):
        if os.path.exists(carpeta_principal):
            shutil.rmtree(carpeta_principal)
            print("La carpeta ha sido eliminada.")
        else:
            print("La carpeta no existe.")

    def modo_oscuro(e):
        # Forma corta
        #page.theme_mode = "ligth" if page.theme_mode == "dark" else "dark"

        if page.theme_mode == "dark":
            page.theme_mode = "ligth"
            btn6.icon=ft.icons.DARK_MODE_ROUNDED
            btn6.tooltip="Modo oscuro"
        else:
            page.theme_mode = "dark"
            
            btn6.icon=ft.icons.LIGHT_MODE_ROUNDED
            btn6.tooltip="Modo claro"

        # No funciona bien, tienes que darle dos veces para que se ponga el modo oscuro la primera vez despues ya va bien.
        """
        if page.theme_mode == "ligth":
            page.theme_mode = "dark"
        else:
            page.theme_mode = "ligth"
        """
        
        page.update()


    # Lo que definimos con sus caracteristicas
    

    btn1 = ft.ElevatedButton("Steam", on_click=steam, width=140, scale=1.24)
    btn2 = ft.ElevatedButton("Rust", on_click=rust, width=140, scale=1.24)
    btn3 = ft.ElevatedButton("Oxide", on_click=oxide, width=140, scale=1.24)
    
    
    btn6 = ft.IconButton(
                    icon=ft.icons.DARK_MODE_ROUNDED,
                    icon_color=ft.colors.DEEP_ORANGE_500,
                    icon_size=40,
                    tooltip="Modo oscuro",
                    on_click=modo_oscuro,
                    )

    page.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.DELETE_FOREVER_ROUNDED,
            on_click=eliminar,
            bgcolor=ft.colors.DEEP_ORANGE_500,
            
        )

   
    titulo = ft.Text(
            f"{titulo_install}",
            size=46,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.ORANGE_800,
        )
    texto2=ft.Text(f"{opciones_sub}", size=26, weight=ft.FontWeight.W_800)
       
    
    

    # Lo que muestra

    page.add(
        ft.Column(controls=[
            titulo,texto2,
        ],
        horizontal_alignment="center",
        
        ),
        

        ft.Column(controls=[

            ft.Container(
                btn1,
                margin=6
        
            ),
            ft.Container(
                 btn2,
                margin=6
        
            ),
            ft.Container(
                btn3,
                margin=6
        
            ),
        ],
        horizontal_alignment="center",
        ),

        
        ft.Row(vertical_alignment="end",controls=[
            btn6,
        ]),
    )



# Fin de Ventana
ft.app(target=main)

# Comando mientras haces la applicacion
# flet run rustserverinstall.py