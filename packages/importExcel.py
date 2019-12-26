from os import system
import xlrd

def importExcel():
    print("Copie el libro de compra en carpeta.")
    print("El formato de nombre del archivo es 'MMAAAA' Ej: 092019")
    input("Presione cualquier tecla cuando el archivo este cargado...")
    system("cls")
    while True:
        try:
            loc = (input("Ingrese nombre del archivo: "))
            if len(loc) != 6 or loc.isdigit() is False:
                print("Nombre ingresado inválido. (Formato: 'MMAAAA' Ej: 092019)")
            else:
                loc = loc+".xls"
                input("Nombre de archivo valido. Presione cualquier tecla para continuar...")
                return loc
        except ValueError:
            print("Nombre ingresado inválido. (Formato: 'MMAAAA' Ej: 092019)")