from os import system
import time
import pyautogui as py
py.PAUSE = 0.2
py.FAILSAFE = False

def inputBills(lf,lc,lm):
    print("Para inicializar el sistema, las unicas dos ventanas abiertas deben ser Sigma y este programa.")
    print("Sigma debe tener en foco la ventana de carga de comprobantes, con el puntero en la caja de 'Cuenta:'")
    print("Si esto no esta de esta manera, la automatizacion NO funcionara.")
    print("La empresa no se hace responsable por ingresos mal hechos.")
    print("Cantidad de Facturas: ",len(lf))
    print("Tiempo aproximado de la tarea: ",round((0.4+(18.4*len(lf)))//60,0), " minutos con ",round((0.4+(18.4*len(lf)))%60,2)," segundos.")
    input("Una vez que todo este establecido correctamente, presione cualquier tecla para continuar...")
    py.hotkey('altleft', 'tab')
    for i in range (len(lf)):
        py.typewrite("13",0.10)
        py.press("enter")
        time.sleep(1)
        py.press("tab")
        py.typewrite(lf[i],0.10)
        py.press("enter")
        time.sleep(1)
        py.typewrite(lf[i],0.10)
        py.press("enter")
        time.sleep(1)
        py.press("enter")
        py.press("down")
        time.sleep(1)
        py.press("tab")
        py.press("tab")
        py.typewrite(lc[i],0.10)
        py.press("enter")
        time.sleep(1)
        py.press("tab")
        py.press("tab")
        py.press("tab")
        py.press("tab")
        py.press("tab")
        py.press("tab")
        py.typewrite("8007",0.10)
        py.press("enter")
        py.typewrite("piv",0.10)
        py.press("enter")
        por3 = round(lm[i]*0.03,2)
        py.typewrite(str(por3),0.10)
        py.press("enter")
        py.press("enter")
        py.typewrite("8008",0.10)
        py.press("enter")
        py.typewrite("i21",0.10)
        py.press("enter")
        por21 = round(lm[i]*0.21,2)
        py.typewrite(str(por21),0.10)
        py.press("enter")
        py.press("enter")
        py.typewrite("11001",0.10)
        py.press("enter")
        py.typewrite("g21",0.10)
        py.press("enter")
        py.typewrite(str(lm[i]),0.10)
        py.press("enter")
        py.press("enter")
        py.press("tab")
        py.press("enter")
        time.sleep(1)
        py.press("left")
        py.press("enter")
        time.sleep(5)
    py.hotkey('altleft', 'tab')
    print("Ingreso finalizado")
    input("Presione cualquier tecla para continuar...")
        
        
        
        
        
    
    
    
