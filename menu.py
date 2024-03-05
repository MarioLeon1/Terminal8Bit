import os
import pygame

def irACarpeta():
    carpeta = input("\033[92m\tNombre de la carpeta:  \033[0m")
    os.chdir(carpeta)

def crearCarpeta():
    nombre_carpeta = input("\033[92m\tNombre de la carpeta a crear:  \033[0m")
    os.makedirs(nombre_carpeta)

def crearArchivo():
    nombre_archivo = input("\033[92m\tNombre del archivo a crear:  \033[0m")
    with open(nombre_archivo, 'w'):
        pass # Para crear el archivo vacío
    os.system("code " + nombre_archivo)  # Abre el archivo con Visual Studio Code

def salir():
    pygame.mixer.music.stop()
    exit(1)

if __name__ == "__main__":

      pygame.init()
      pygame.mixer.music.load("8bit song.mp3")
      pygame.mixer.music.play(-1) # Esto hace que no haya que poner una duración para el tiempo que sonará, sino que simplemente reproduce el audio entero

      while True:
            print("""\033[92m

            ███╗   ███╗ █████╗ ██████╗ ██╗ ██████╗ 
            █████╗ ████║██╔══██╗██╔══██╗██║██╔═══██╗
            ██╔████╔██║███████║██████╔╝██║██║   ██║
            ██║╚██╔╝██║██╔══██║██╔══██╗██║██║   ██║
            ██║ ╚═╝ ██║██║  ██║██║  ██║██║╚██████╔╝
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ 
                                                   
            \033[0m""")

            print("""\033[92m\t Menú:
            
            1. Ir a carpeta
            2. Crear carpeta
            3. Crear archivo
            4. Salir
                                                   
            \033[0m""")

            opcion = input("\033[92m\t--------> Opción: \033[0m")

            if opcion == '1':
                irACarpeta()
            elif opcion == '2':
                crearCarpeta()
            elif opcion == '3':
                crearArchivo()
            elif opcion == '4':
                salir()
            else:
                print("Opcion incorrecta")
