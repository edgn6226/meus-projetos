#banco de dados
lista = []
lista_numeros = []
lista_operação = []

#apresentação das perguntas e sua escolha
especificação_de_while = 0
while especificação_de_while == 0:
    print("1 = soma/subtração")
    print("2 = mutiplicação/divisão")
    print("3 = equação do 2°grau")
    o_que_você_quer = int(input("qual vai querer?:"))
    if 4 > o_que_você_quer > 0  :
        especificação_de_while += 1
    else:
        não_existe = ("não existe esta resposta\ntente novamente")
        print (não_existe)