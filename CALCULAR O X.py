print("1 adiçãa\n2 subritração\n3 multipicaçaon\n4 diviação")
a=int(input("..."))
resultado= None

if a==1:
    Q=int(input("qual e a suas contante antes do = ?"))
    Q1=int(input("qual e a suas contante depois do = ? "))
    Q2=Q1-Q

elif a == 2:
    W=int(input("qual e a suas contante antes do = ?"))
    W1=int(input("qual e a suas contante depois do = ? "))
    W2=W+W1


elif a== 3:
    E=int(input("qual e a suas contante antes do = ?"))
    E1=int(input("qual e a suas contante depois do = ? "))
    E2=E1/E
    

elif a==4:
    R=int(input("qual e a suas contante antes do = ?"))
    R1=int(input("qual e a suas contante depois do = ? "))
    R2=R*R1
   
if resultado is not None:
    print(f"Essa é sua variável: {resultado}")


#fazer ter mais de um numero para calcular
