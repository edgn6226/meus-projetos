
from datetime import datetime
agora=datetime . now()
tempo1=agora . hour 
tempo2=int(input("quando temos que ir(no formato de 24)"))
 
tempo3= tempo2-tempo1

if tempo3 <= 0:
    print(f"vc esta{tempo3}atrazado")
else:
    print(f"vc tem {tempo3}para chegar")

#distância=float(input("vc está a quantos km do seu destino"))
#KMH= float(input("qual sera sua velocidade meida? (km/h)"))

#tempo4=KMH/tempo3
#tempo5=distância/tempo4

#print(f"vc vai chegar em {tempo5 * (-1)}horas")