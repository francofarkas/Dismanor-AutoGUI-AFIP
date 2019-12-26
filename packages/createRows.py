from os import system
import xlrd
from packages import *

def createRows(loc):
    system("cls")
    print("Extrayendo informacion del archivo...")
    while True:
        try:
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            break
        except FileNotFoundError:
            print("Archivo con nombre: " + loc + " no encontrado.")
            loc = importExcel()
    
    lista_fecha = []
    unleap = [31,59,90,120,151,181,212,243,273,304,334,365]
    leap = [31,60,91,121,152,182,213,244,274,305,335,366]
    yeartoday = loc[2:6]
    monthtoday = loc[:2]
    for i in range (1,sheet.nrows-1):
        fecha = sheet.cell_value(i,0)
        yearexcel = ((int(yeartoday) - 1900) * 365) + ((int(yeartoday) - 1900)//4) + 1
        if (int(yeartoday)-1900)%4 == 0:
            monthexcel = leap[int(monthtoday)-2]
        else:
            monthexcel = unleap[int(monthtoday)-2]
        day = int(fecha) - yearexcel - monthexcel
        if day < 10:
            lista_fecha.append("0"+str(day)+monthtoday+yeartoday)
        else:
            lista_fecha.append(str(day)+monthtoday+yeartoday)
    print("Lista de Fechas creada")   
    lista_comp = []
    for i in range (1,sheet.nrows-1):
        comp = sheet.cell_value(i,1)
        comp = str(comp)
        if "-" in comp:
            scomp = comp
        else:
            scomp = comp[:3] + "-" + comp[3:-2]
        if comp[:1] != "0":
            scomp = "0" + scomp
        lista_comp.append(scomp)
    print("Lista de Comprobantes creada")
    lista_monto = []
    for i in range(1,sheet.nrows-1):
        monto = sheet.cell_value(i,6)
        fm = float(monto)*-1
        lista_monto.append(round(fm,2))
    print("Lista de Montos creada")
    return lista_fecha,lista_comp,lista_monto