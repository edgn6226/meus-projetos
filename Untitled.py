from datetime import datetime
agora=datetime . now()
tempo1=agora. hour + agora. minute 
tempo2=float(input("quando temos que ir(no formato de 24)"))
 
tempo3= tempo2-tempo1

if tempo3 <= 0:
    print(f"vc esta{tempo3}atrazado")
else:
    print(f"vc tem {tempo3}para chegar")

