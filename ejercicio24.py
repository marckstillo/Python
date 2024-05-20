import os
import time
for x in range(10):
    print(f"ABRIENDO APLICACIÓN {x*10}%")
    time.sleep(1)
    os.system("cls")
os.system("start https://instagram.com")