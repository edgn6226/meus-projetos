tarefas =[{'nome': 'comer', 'terminar' : False },
        { "nome" : 'dormir', 'terminar' : False}]


def exibir_menu():
 opicãos = ['1. Adicionar tarefa', '2. Remover tarefa', '3. Exibir todas as tarefas' , '4. Marcar tarefa como concluída']
 print("\n". join (opicãos))
def exibir_tarefas():
    if not tarefas:
        print("Nenhuma tarefa para exibir.")
    else:
        for idx, tarefa in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa['terminar'] else "Pendente"
            print(f"{idx}. {tarefa['nome']} - {status}")
while True:
    exibir_menu() 
    coisa = input("\nescolha um numero de 1 a 5")    
    if coisa == "1":
        a = input("adicione uma tarefa ")
        tarefas.append({'nome': a,"terminar": False })
        print(f"tarefas *{a}*  adicionada")
        print (tarefas)