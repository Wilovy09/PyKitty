# Autor: Wilovy
# Fecha: 2021-10-10
# Descripcion: Script para cambiar aspectos de tu terminal Kitty
import os, argparse

ruta_archivo = r'/home/wilovy/.config/HyprV/kitty/kitty.conf' # Aqui pon la ruta de tu archivo kitty.conf
pathThemes = r'/home/wilovy/.config/HyprV/kitty/themes/' # Aqui pon la ruta de tu carpeta themes
pathFonts = r'/usr/share/fonts/TTF/' # Aqui pon la ruta de tu carpeta TTF

parser = argparse.ArgumentParser(description='App para cambiar el tema de Kitty Terminal')
parser.add_argument('--tema', '-t', help='Cambiar tema')
parser.add_argument('--scan', '-s', help='Ver temas disponibles', action='store_true')

parser.add_argument('--tamano', '-f', help='Cambiar el tamano de la fuente')

parser.add_argument('--setFont', '-r', help='Cambiar tipo de letra')
parser.add_argument('--scanFonts', '-e', help='Ver fuentes TTF disponibles', action='store_true')

def cambiarTema(NOMBRE):
    with open(ruta_archivo) as file_object:
        lista = file_object.readlines()
        if 'include' in lista[0]:
            lineaTheme = lista[0].split('/')
            lineaTheme[-1] = NOMBRE + '.conf'
            lineaTheme = '/'.join(lineaTheme)
            lista[0] = f'{lineaTheme}\n'
            lista = ''.join(lista)
            with open(ruta_archivo, 'w') as file_object:
                file_object.writelines(lista)
        else:
            print('\nNo hay ninguna linea de tema establecido\nO la linea "include" no es la primera linea del archivo')

def cambianTamano(TAMANO):
    with open(ruta_archivo) as file_object:
        lista = file_object.readlines()
        if 'font_size' in lista[2]:
            lineaSize = lista[2].split(' ')
            lineaSize[-1] = TAMANO
            lineaSize = ' '.join(lineaSize)
            lista[2] = f'{lineaSize}\n'
            lista = ''.join(lista)
            with open(ruta_archivo, 'w') as file_object:
                file_object.writelines(lista)
        else:
            print('\nNo hay ninguna linea de tamano establecido\nO la linea "font_size" no es la tercera linea del archivo')

def cambianFONT(NOMBRETTF):
    with open(ruta_archivo) as file_object:
        lista = file_object.readlines()
        if 'font_family' in lista[1]:
            lineaSize = lista[1].split(' ')
            del lineaSize[6:]
            lineaSize[5] = ' ' + NOMBRETTF
            lineaSize = ' '.join(lineaSize)
            lista[1] = f'{lineaSize}\n'
            lista = ''.join(lista)
            with open(ruta_archivo, 'w') as file_object:
                file_object.writelines(lista)
        else:
            print('\nNo hay ninguna linea de font_family establecido\nO la linea "font_family" no es la segunda linea del archivo')

def verFonts():
    os.chdir(pathFonts)
    print(os.system('ls'))

def verTemas():
    os.chdir(pathThemes)
    print(os.system('ls'))

if __name__ == '__main__':
    args = parser.parse_args()

    if args.tema:
        cambiarTema(args.tema)
    elif args.tamano:
        cambianTamano(args.tamano)
    elif args.setFont:
        cambianFONT(args.setFont)
    elif args.scanFonts:
        verFonts()
    elif args.scan:
        verTemas()
    else:
        print('Opcion invalida! \nPrueba con -h para ver las opciones disponibles')
