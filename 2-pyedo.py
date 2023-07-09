# ----------------------------------------------------------------------------------------------------
# Questo programma utilizza la libreria PyEdo: https://github.com/Comau/pyedo
# ----------------------------------------------------------------------------------------------------

from pyedo_local import eduedo
from time import sleep

# ----------------------------------------------------------------------------------------------------
# Funzione di movimentazione: Scrivere qui i comandi da fare eseguire all'e.DO
# ----------------------------------------------------------------------------------------------------

def run_edo(myedo):        
    print("[INFO] Running.")
    sleep(10)
    # print("[INFO] L'e.DO si sta muovendo alla posizione SAFE.")
    # myedo.moveJoints(0, 60, 30, 0, 80, 0)
    # myedo.gripperOpen()
    

# ----------------------------------------------------------------------------------------------------
# Programma MAIN: codice di setup (NON MODIFICARE)
# ----------------------------------------------------------------------------------------------------
if __name__=="__main__":
    ip_address = "192.168.12.1"
    try: 
        myedo = eduedo(ip_address)
        if myedo.client.is_connected:
            if True:
                try:
                    run_edo(myedo)
                except KeyboardInterrupt:
                    print("[INFO] Received KeyboardInterrupt.")
                    myedo.moveHome()
                    myedo.moveCancel()
                    myedo.disconnectMyedo()
    except KeyboardInterrupt:
        print("[INFO] Received KeyboardInterrupt.")
    except Exception as e:
        print(f"[ERROR] {e}")