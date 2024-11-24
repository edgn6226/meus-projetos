import random
def com (combinacoes):
  print("Você gostaria de escolher uma dessas combinações automaticamente? (sim/não)")
  combinaçao_aut = input("sim ou não")
  if combinaçao_aut == "sim" and combinacoes:
     senha_aleatoria = random.choice(combinacoes)
  print(f"Sua senha escolhida automaticamente é: {senha_aleatoria}")
  if combinaçao_aut== "não":
    print("nenhuma cambinaçao disponivel")
senha=[]
combinaçoes= []
quantidade_de_digitos_da_senha = int(input("Quantos caracteres tem sua senha (EX: 2 = '12'): "))


if quantidade_de_digitos_da_senha == 2:
  
  for i in range(2):
      quantidade_de_digitos_da_senha2 = int(input())
      senha.append(quantidade_de_digitos_da_senha2)
  print(f"Temos:\n2 opções para o primeiro dígito ({senha[0]}, {senha[1]}).\n2 opções para o segundo dígito ({senha[0]}, {senha[1]}).\nAssim, o número total de combinações possíveis é 2×2 = 4.")
  total_combinacoes = 2 * 2
  print(f"Essas são as possibilidades: {total_combinacoes}")

  for i in senha:
      for o in senha:
          print(f"{i}{o}")
          conbinçoao=(f"{i}{o}")

  com(combinaçoes)

if quantidade_de_digitos_da_senha ==3:
  separados=input("seu numeros vao poder si repitir")
  if separados : "sim"
  for i in range(3):
    quantidade_de_digitos_da_senha_3=int(input("quais sao seus numeros"))
  senha.append(quantidade_de_digitos_da_senha_3)
  print(f"Temos:\n2 opções para o primeiro dígito ({senha[0]}, {senha[1]},({senha[2]}).\n opções para o segundo dígito ({senha[0]}, {senha[1]},({senha[2]}).\nopções para o terceiro digito ({senha[0]},({senha[1]}),({senha[2]}) Assim, o número total de combinações possíveis é 3x3x3 = 27.")
  for i in senha:
    for o in senha:
      for p in senha:
        print(f"{i}{o}{p}")
     