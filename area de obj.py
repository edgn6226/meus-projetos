print("qual dessas areas vc gostaria de calcular  1 quadrado / 2 retabgulo / 3 triângulo / 4 trapezio")
X = ["_" * 40, "-" * 20]
print("\n".join(X))
b=input("qual ?")

if b=="1":
    n=int(input("qual a altura"))
    n1=n**2
    print(X)
    print(f"a area do seu cubo e de {n1}")
    print(X)

if b=="2":
    L=int(input("altura?"))
    print(X)
    L1=int(input("largura?"))
    L2=L*L1
    print(X)
    print(f"a sua area e de {L2}")
    print(X)
if b=='3':
    
    A1=int(input("qual o seu raio"))
    print(X)
    A2=int(input("qula a altura"))
    print(X)
    A3=(A1*2*A2)/2
    print(F"a sua area e de {A3}") 
    
if b=='4':
    B=int(input("qual a sua altura"))
    print(X)
    B1=int(input("qual sua base menor"))
    print(X)
    B2=int(input("qual sua base maior"))
    B3=((B2+B1)*B)/2
    print(X)
    print(f"sua area e de{B3}")