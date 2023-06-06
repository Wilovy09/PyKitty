# PyKitty

PyKitty es un script en python que te permite cambiar valores esteticos de tu terminal Kitty con una interfaz CLI.

## Configuracion

Para configurar, por el momento no es tan automatico como sera en un futuro

Primero deberas buscar la carpeta donde se guarda Kitty, usualmente es en:

```bash
.config/kitty
```

Una vez ubicada la carpeta deberas de ponerlo dentro del archivo `pykitty.py`

De esta forma:

```py
ruta_archivo = '/home/wilovy/.config/HyprV/kitty/kitty.conf' # Aqui pon la ruta de tu archivo kitty.conf
pathThemes = '.config/kitty/themes/' # Aqui pon la ruta de tu carpeta themes
pathFonts = '/usr/share/fonts/TTF/' # Aqui pon la ruta de tu carpeta TTF
```

En nuestro archivo `kitty.conf` debemos tener en este orden las siguientes lineas

```conf
include ~/.config/HyprV/kitty/themes/Hurtado.conf
font_family      jetbrains mono nerd font
font_size        12
```

De esta forma quedaria nuestro `kitty.conf`:

```conf
include ~/.config/HyprV/kitty/themes/Hurtado.conf
font_family      jetbrainsmono nerd font
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
```

## Comandos

|Completo   |Abreviacion |Funcion                                                        |
|-----------|------------|---------------------------------------------------------------|
|--help     |-h          |Muestra esta tabla en la temrminal                             |
|--tema     |-t          |Cambia el tema al que escribamos a su lado                     |
|--scan     |-s          |Nos muestra todos los temas que tengamos en la carpeta `themes`|
|--tamano   |-f          |Cambiar el tamano de la fuente                                 |
|--setFont  |-r          |Cambiar el tipo de fuente                                      |
|--scanFonts|-e          |Ver fuentes disponibles en la carpeta `/fonts/TTF/`            |

## Uso

Para cambiar valores deberemos usar el sig comando, solo cambiando el prefijo que deseamos modificar

```bash
python pykitty.py -t 3024_Day
python pykitty.py -r Montserrat-Medium
python pykitty.py -f 12

# Si nos da algun error de permisos podemos usar `sudo`
sudo python pykitty.py -t 3024_Day
sudo python pykitty.py -r Montserrat-Medium
sudo python pykitty.py -f 12
```
