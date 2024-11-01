from datetime import datetime
agora=datetime . now()
tempo1=agora. hour + agora. minute /60
tempo2=float(input("quando temos que ir(no formato de 24)"))
 
tempo3= tempo2-tempo1

print("-" * 30)

if tempo3 <= 0:
     print(f"Você está {abs(tempo3):.2f} horas atrasado.")
else:
    print(f"vc tem {(tempo3): .2f}para chegar")

print("-" * 30)

distância=float(input("vc está a quantos km do seu destino"))
KMH= float(input("qual sera sua velocidade meida? (km/h)"))


tempo5=distância/KMH
print("-" * 30)
print(f"vc vai chegar em {(tempo5): .2f}horas")
if tempo5 > tempo3:
    print(f"Você não vai chegar a tempo! Você precisaria de {tempo5:.2f} horas.")
else:
    print(f"Você chegará em {tempo5:.2f} horas, a tempo!")
