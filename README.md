# PyKitty

PyKitty es un script en python que te permite cambiar el los temas de tu terminal Kitty con una interfaz CLI.

## Configuracion

Para configurar, por el momento no es tan automatico como sera en un futuro

Primero deberas buscar la carpeta donde se guarda Kitty, usualmente es en

```bash
.config/kitty
```

Una vez ubicada la carpeta deberas de ponerlo dentro del archivo `pykitty.py`

De esta forma:

```py
ruta_archivo = '/home/USR/.config/HyprV/kitty/kitty.conf' # Aqui pon la ruta de tu archivo kitty.conf
pathThemes = r'.config/kitty/themes/' # Aqui pon la ruta de tu carpeta themes
```

## Comandos

|Completo  |Abreviacion |Funcion |
|-------|-------|-------|
|--help |-h  |Muestra esta tabla en la temrminal|
|--tema |-t  |Cambia el tema al que escribamos a su lado|
|--scan |-s  |Nos muestra todos los temas que tengamos en la carpeta `themes`|

## Uso

Para cambiar el tema deberomos poner el nombre del tema sin la terminacion `.conf`

```bash
sudo python pykitty.py -t 3024_Day
```

Esto nos dara una salida como esta

```bash
❯ python /home/USR/Proyects/PyKitty/pykitty.py -t 3023_Day

>>Se establecio 3023_Day como tema principal
Reinicia la terminal para ver los cambios
```
