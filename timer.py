from plyer import notification
import time
import random


def calcular_descanso(tempo_estudo):
    descanso = tempo_estudo * 0.25
    return min(max(descanso, 5), 30)

estudar = float(input("quantos minutos de estudos: "))

tempo_estudar_max = estudar * 60
tempo_pausa_max = calcular_descanso(estudar) * 60

tempo_estudos1 = random.randint(
    int(tempo_estudar_max * 0.3),
    int(tempo_estudar_max * 0.7)
)

tempo_estudos2 = tempo_estudar_max - tempo_estudos1


def notificacao_de_estudos():
    notification.notify(title="tempo de estudar",
                        message="tempo de estudar",
                        timeout=12)

def notificacao_de_pausa():
    notification.notify(title="tempo livre",
                        message=f"tempo livre {tempo_pausa_max :.1f} minutos",
                        timeout=12)

def notificacao_de_fim():
    notification.notify(title="acabou",
                        message="acabou",
                        timeout=12)


notificacao_de_estudos()
print("estudar")
time.sleep(tempo_estudos1)

notificacao_de_pausa()
print("pausa")
time.sleep(tempo_pausa_max)

notificacao_de_estudos()
print("estudar")
time.sleep(tempo_estudos2)

notificacao_de_fim()
print("fim")