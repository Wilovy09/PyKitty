import os
import argparse

path = r'.config/kitty/' # Aqui pon la ruta de tu carpeta kitty
pathThemes = r'.config/kitty/themes/' # Aqui pon la ruta de tu carpeta themes

parser = argparse.ArgumentParser(description='App para cambiar el tema de Kitty Terminal')

parser.add_argument('--tema', '-t', help='Cambiar tema a (NOMBRE)')
parser.add_argument('--scan', '-s', help='Ver temas disponibles %(prog)s', action='store_true')

def cambiarTema(NOMBRE):
    print(f'\n>>Se establecio {NOMBRE} como tema principal\nReinicia la terminal para ver los cambios')
    
    os.chdir(path)
    
    main = open('kitty.conf', 'w')
    
    #AQUI MODIFICA TU ARCHIVO DE CONFIGURACION DE KITTY
    KittyConf = f"""
include ~/.config/HyprV/kitty/themes/{NOMBRE}.conf
font_family      jetbrains mono nerd font
font_size        12
bold_font        auto
italic_font      auto
bold_italic_font auto
mouse_hide_wait  2.0
cursor_shape     block
url_color        #0087bd
url_style        dotted
#Close the terminal without confirmation
confirm_os_window_close 0
background_opacity 0.90
"""
    main.write(KittyConf)
    main.close()

def verTemas():
    os.chdir(pathThemes)
    print(os.system('ls'))

if __name__ == '__main__':
    args = parser.parse_args()

    if args.tema:
        cambiarTema(args.tema)
    elif args.scan:
        verTemas()
    else:
        print('Opcion invalida! \nPrueba con -h para ver las opciones disponibles')