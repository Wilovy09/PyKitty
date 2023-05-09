import os
import argparse

ruta_archivo = '/home/wilovy/.config/HyprV/kitty/kitty.conf' # Aqui pon la ruta de tu archivo kitty.conf
pathThemes = r'.config/kitty/themes/' # Aqui pon la ruta de tu carpeta themes

parser = argparse.ArgumentParser(description='App para cambiar el tema de Kitty Terminal')
parser.add_argument('--tema', '-t', help='Cambiar tema a (NOMBRE)')
parser.add_argument('--scan', '-s', help='Ver temas disponibles %(prog)s', action='store_true')

def cambiarTema(NOMBRE):
    print(f'\n>>Se establecio {NOMBRE} como tema principal\nReinicia la terminal para ver los cambios')
    with open(ruta_archivo) as file_object:
        lista = file_object.readlines()
        if 'include' in lista[0]:
            lineaTheme = lista[0].split('/')
            lineaTheme[-1] = NOMBRE + '.conf'
            lineaTheme = '/'.join(lineaTheme)
            lista[0] = lineaTheme
            lista = '\n'.join(lista)
            with open(ruta_archivo, 'w') as file_object:
                file_object.writelines(lista)
        else:
            print('\nNo hay ninguna linea de tema establecido\nO la linea "include" no es la primera linea del archivo')

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