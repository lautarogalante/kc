#!/usr/bin/env python3.10 
import argparse 
from pathlib import Path


PROGRAM_NAME = 'kc'
FONT_FAMILY = 'font_family'
BACKGROUND = "background"
FOREGROUND = "foreground"
FONT_SIZE = "font_size"
BACKGROUND_OPACITY = "background_opacity"



p = (Path().home() / '.config' / 'kitty' / 'kitty.conf')

def save_values(dictionary):
    try:
        with open(p, 'r') as fInPut:
            lineas = fInPut.readlines()
        with open(p, 'w') as fOutPut:
            for linea in lineas:
                partes = linea.split()
                if len(partes) >= 2 and partes[0] in dictionary and dictionary[partes[0]] is not None:
                    new_value = dictionary[partes[0]]
                    if partes[0] in ['background', 'foreground']:
                        new_value = "#" + new_value
                        linea_nueva = f"{partes[0]} {new_value}\n"
                        fOutPut.write(linea_nueva)
                else:
                    fOutPut.write(linea)
        print("Succesfully updated congfig... ")
    except OSError as err:
        print("Os Error:", err)

def main():

    parser = argparse.ArgumentParser(
        prog='kc',
        description='Change config for the terminal'
    )
    parser.add_argument('-ff', '--font-family',
        help="This option is used to change the font family",
        type=str
    )
    parser.add_argument('-b', '--background-color',
        help='This option is used to change background color',
        type=int
    )
    parser.add_argument('-f', '--foreground-color',
        help='This option is used to change foreground',
        type=int
    ) 
    parser.add_argument('-s', '--font-size', 
        help='This option is used to change font size',
        type=float or int 
    )
    parser.add_argument('-o', '--background-opacity', 
        help='This option is used to change opacity values',
        type=float or int 
    ) 
    args = parser.parse_args()
    ffArg = args.font_family
    bcArg = args.background_color
    fcArg = args.foreground_color
    fsArg = args.font_size
    boArg = args.background_opacity

    def load_values():
        dictionary = {FONT_FAMILY: ffArg, BACKGROUND:bcArg, FOREGROUND:fcArg, FONT_SIZE:fsArg, BACKGROUND_OPACITY:boArg}
        save_values(dictionary)


    argument = [ffArg, bcArg, fcArg, fsArg, boArg]
    for arg in argument:
        if arg is not None:
            is_none = False
            break
        elif arg is None:
            is_none = True

    
    if is_none:
        print('You must send an argument, try: {} -h or --help'.format(PROGRAM_NAME))
    else:
        load_values()

if __name__ == "__main__":
   main() 

