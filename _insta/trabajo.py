tiempos_totales = []

Oro_cont = 347.914 
Plata_cont = 361.13
Bronce_cont = 363.607 

vueltas = input("n: ")
vueltas = int(vueltas)

inc = 0
while inc < vueltas:
    inc += 1
    t = input("tiempo "+ str(inc) + ": ")
    t = t.replace(",", ".").split(":")
    totales = 0
    
    cnt = 0
    while cnt < len(t):
        totales += float(t[cnt]) * 60 ** (len(t) - cnt - 1)
        cnt += 1
    tiempos_totales.append(totales)
    
tiempos_ord = sorted(tiempos_totales)
mej = tiempos_ord[0]
min = mej // 60
segu = mej - (min * 60)
segu = round(segu, 3)
if int(segu) < 10:
    segu = "0" + str(segu)
print("Mejor tiempo: " + str(int(min)) + ":" + str(segu))


peor_t = tiempos_totales[-1]
ptmin = peor_t // 60
seg = peor_t - (ptmin * 60)
seg = round(seg, 3)
if int(seg) < 10:
    seg = "0" + str(seg)
print("Peor tiempo: " + str(int(ptmin)) + ":" + str(seg))


oro = 0
plata = 0
bronce = 0
recor = 0

while recor < len(tiempos_totales):
    if tiempos_totales[recor] <= Oro_cont:
        oro += 1
    elif tiempos_totales[recor] <= Plata_cont:
        plata += 1
    elif tiempos_totales[recor] <= Bronce_cont:
        bronce += 1
    recor += 1

oro = str(oro)
bronce = str(bronce)
plata = str(plata)



print("Oro: " + oro)
print("Plata: " + plata)
print("Bronce: " + bronce)