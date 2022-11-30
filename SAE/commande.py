import subprocess
import platform
import psutil

os = platform.system()

if os == "Windows":
    print("Windows")

    x = ""
    while x != "bye":
        x = str(input("commande: "))
        if x == "RAM":
            ramtotal = psutil.virtual_memory().total/ 1024 / 1024 / 1024
            ramlibre = psutil.virtual_memory().free/ 1024 / 1024 / 1024
            ramutil = psutil.virtual_memory().used/ 1024 / 1024 / 1024
            print(f"RAM totale: {round(ramtotal, 2)} Go, RAM libre: {round(ramlibre, 2)} Go, RAM utilisée: {round(ramutil, 2)} Go")

        if x != "bye":
            p = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)

            try:
                outs, errs = p.communicate(None, 10)
            except subprocess.TimeoutExpired:
                print(f"Timeout on command {x}")
            else:
                txt = outs.decode(errors = 'ignore').rstrip("\r\n")
                print(txt)

elif os == "Linux":
    print("Linux")

    x = ""
    while x != "bye":
        x = str(input("commande: "))
    
        if x != "bye":
            p = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)

            try:
                outs, errs = p.communicate(None, 10)
            except subprocess.TimeoutExpired:
                print(f"Timeout on command {x}")
            else:
                txt = outs.decode(errors='ignore').rstrip("\r\n")
                print(txt)

elif os == "Darwin":
    print("MacOS")

    x = ""
    while x != "bye":
        x = str(input("commande: "))
    
        if x != "bye":
            p = subprocess.Popen(x, stdout=subprocess.PIPE, shell=True)

            try:
                outs, errs = p.communicate(None, 10)
            except subprocess.TimeoutExpired:
                print(f"Timeout on command {x}")
            else:
                txt = outs.decode(errors='ignore').rstrip("\r\n")
                print(txt)