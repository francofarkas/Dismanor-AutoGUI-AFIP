from os import system
while True:
    try:
        import xlrd
        break
    except ModuleNotFoundError:
        system("python get-pip.py")
        system("pip install xlrd")
while True:
    try:
        import pyautogui
        break
    except ModuleNotFoundError:
        system("pip install PyAutoGUI")
from packages import *


def __main__():

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("*       Auto Libro IVA Compra       *")
    print("*                                   *")
    print("* ¿Qué desea hacer?:                *")
    print("*                                   *")
    print("*   '1':Iniciar Auto Libro          *")
    print("*   '2':Salir de Programa           *")
    print("*                                   *")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    while True:
        try:
            opcion = int(input("Ingrese elección: "))
            if opcion == 1 or opcion == 2:
                break
            else:
                print("Valor ingresado inválido")
        except ValueError:
            print("Valor ingresado inválido")
            continue
    if opcion == 1:
        system("cls")
        loc = importExcel()
        lista_fechas = []
        lista_comps = []
        lista_montos = []
        lista_fechas,lista_comps,lista_montos = createRows(loc)
        inputBills(lista_fechas,lista_comps,lista_montos)
        system("cls")
        print("Gracias por usar 'Auto Libro IVA Compra'")
        input("Para salir, presione cualquier tecla: ")
    else:
        system("cls")
        print("Gracias por usar 'Auto Libro IVA Compra'")
        input("Para salir, presione cualquier tecla: ")
        
if __name__ == "__main__":
    __main__()