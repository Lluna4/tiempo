import psutil
import time
i = 0
while True:
    if "Code.exe" in (i.name() for i in psutil.process_iter()):
        pass
    else:
        i = time.perf_counter()
        break


try:
    with open("stats.txt", "r") as r:
        min = float(r.read())
        with open("stats.txt", "w") as w:
            min = i/60 + min 
            min = str(min)
            w.write(min)
            
except IOError:
    with open("stats.txt", "x") as t:
        t.write(str(i/60))
print(f"Has estado programando {i/60} minutos")
input(f"has estado en total {min} minutos")


        