###############################################################################
#                                                                             #
# InstInt                                                                     #
#                                                                             #
###############################################################################

import time
import board
import neopixel
from gpiozero import Button, MotionSensor, Motor
import csv
from datetime import datetime
import signal
import sys

###############################################################################
#                                                                             #
# SETUP                                                                       #
#                                                                             #
###############################################################################

prototipo = True

# Neopixels
if prototipo is True:
    pixels_count = 10
    pixels_count_fita = 1
    pixels_count_matriz = 5

else:
    pixels_count = 766
    pixels_count_fita = 90
    pixels_count_matriz = 256

pixels = neopixel.NeoPixel(
    board.D12,
    pixels_count,
    auto_write=True,
    pixel_order=neopixel.GRB
)

inicio_fita_1 = pixels_count_matriz
fim_fita_1 = inicio_fita_1 + pixels_count_fita

inicio_fita_2 = pixels_count_matriz + pixels_count_fita
fim_fita_2 = inicio_fita_2 + pixels_count_fita

inicio_fita_3 = pixels_count_matriz + pixels_count_fita * 2
fim_fita_3 = inicio_fita_3 + pixels_count_fita

inicio_fita_4 = pixels_count_matriz + pixels_count_fita * 3
fim_fita_4 = inicio_fita_4 + pixels_count_fita

inicio_fita_5 = pixels_count_matriz + pixels_count_fita * 4
fim_fita_5 = inicio_fita_5 + pixels_count_fita

BRANCO = (160, 160, 160)  # brilho reduzido
PRETO = (0, 0, 0)  # desligado
VERMELHO = (255, 0, 0)
CARMESIM = (220, 20, 60)
PINK = (255, 192, 203)
PINKPROFUNDO = (255, 20, 147)
LARANJA = (255, 165, 0)
SALMAO = (255, 160, 122)
AMARELO = (255, 255, 0)
DOURADO = (255, 215, 0)
ROXO = (128, 0, 128)
MAGENTA = (255, 0, 255)
VERDE = (0, 255, 0)
CERCETA = (0, 128, 128)
AZUL = (0, 0, 255)
CIANO = (0, 255, 255)
MARROM = (165, 42, 42)
CHOCOLATE = (210, 105, 30)

pixels.fill(BRANCO)

# Toque
toque_fita_1 = Button(10, pull_up=False)
toque_fita_2 = Button(9, pull_up=False)
toque_fita_3 = Button(11, pull_up=False)
toque_fita_4 = Button(0, pull_up=False)
toque_fita_5 = Button(5, pull_up=False)

# Presença
presenca_ir_1 = MotionSensor(8)
presenca_ir_2 = MotionSensor(7)
presenca_ir_3 = MotionSensor(1)
presenca_microondas = MotionSensor(23)

# Movimento
motor_vertical = Motor(21, 20)
velocidade_vertical = 1  # confirmar
motor_rotacao = Motor(16, 26)
velocidade_rotacao = 0.5  # confirmar
fim_abertura = Button(24, pull_up=False)
fim_fechamento = Button(25, pull_up=False)


# Logs de Sistema
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = "log_{}.csv".format(agora)


def log_data(event):
    print(event)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([now, event])


def signal_handler(signal, frame):
    log_data("Encerrando a aplicação")
    pixels.fill(PRETO)
    motor_vertical.stop()
    motor_rotacao.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

###############################################################################
#                                                                             #
# Comportamento Fitas                                                         #
#                                                                             #
###############################################################################


def fita_tocada_1():
    log_data("Toque na Fita 1")
    pixels[inicio_fita_1:fim_fita_1] = [CARMESIM] * pixels_count_fita
    estimulo()


def fita_tocada_2():
    log_data("Toque na Fita 2")
    pixels[inicio_fita_2:fim_fita_2] = [DOURADO] * pixels_count_fita
    estimulo()


def fita_tocada_3():
    log_data("Toque na Fita 3")
    pixels[inicio_fita_3:fim_fita_3] = [MAGENTA] * pixels_count_fita
    estimulo()


def fita_tocada_4():
    log_data("Toque na Fita 4")
    pixels[inicio_fita_4:fim_fita_4] = [CIANO] * pixels_count_fita
    estimulo()


def fita_tocada_5():
    log_data("Toque na Fita 5")
    pixels[inicio_fita_5:fim_fita_5] = [CHOCOLATE] * pixels_count_fita
    estimulo()


toque_fita_1.when_pressed = fita_tocada_1
toque_fita_2.when_pressed = fita_tocada_2
toque_fita_3.when_pressed = fita_tocada_3
toque_fita_4.when_pressed = fita_tocada_4
toque_fita_5.when_pressed = fita_tocada_5


def fita_solta_1():
    log_data("Fim do toque na Fita 1")
    pixels[inicio_fita_1:fim_fita_1] = [BRANCO] * pixels_count_fita


def fita_solta_2():
    log_data("Fim do toque na Fita 2")
    pixels[inicio_fita_2:fim_fita_2] = [BRANCO] * pixels_count_fita


def fita_solta_3():
    log_data("Fim do toque na Fita 3")
    pixels[inicio_fita_3:fim_fita_3] = [BRANCO] * pixels_count_fita


def fita_solta_4():
    log_data("Fim do toque na Fita 4")
    pixels[inicio_fita_4:fim_fita_4] = [BRANCO] * pixels_count_fita


def fita_solta_5():
    log_data("Fim do toque na Fita 5")
    pixels[inicio_fita_5:fim_fita_5] = [BRANCO] * pixels_count_fita


toque_fita_1.when_released = fita_solta_1
toque_fita_2.when_released = fita_solta_2
toque_fita_3.when_released = fita_solta_3
toque_fita_4.when_released = fita_solta_4
toque_fita_5.when_released = fita_solta_5

###############################################################################
#                                                                             #
# Comportamento Presença                                                      #
#                                                                             #
###############################################################################


def presenca_detectada_1():
    log_data("Presença no Sensor IR 1")
    presenca_detectada()


def presenca_detectada_2():
    log_data("Presença no Sensor IR 2")
    presenca_detectada()


def presenca_detectada_3():
    log_data("Presença no Sensor IR 3")
    presenca_detectada()


def presenca_detectada_microondas():
    log_data("Presença no Sensor Microondas")
    presenca_detectada()


def presenca_detectada():
    estimulo()

presenca_ir_1.when_motion = presenca_detectada_1
presenca_ir_2.when_motion = presenca_detectada_2
presenca_ir_3.when_motion = presenca_detectada_3
presenca_microondas.when_motion = presenca_detectada_microondas

###############################################################################
#                                                                             #
# Comportamento Movimento                                                     #
#                                                                             #
###############################################################################


def abrir(velocidade=velocidade_vertical):
    if fim_abertura.is_pressed is False:
        log_data("Abrindo")
        motor_vertical.forward(speed=velocidade)


def fechar(velocidade=velocidade_vertical):
    if fim_fechamento.is_pressed is False:
        log_data("Fechando")
        motor_vertical.backward(speed=velocidade)


def parar_abertura():
    log_data("Parando abertura")
    motor_vertical.stop()


def parar_fechamento():
    log_data("Parando fechamento")
    motor_vertical.stop()

fim_abertura.when_pressed = parar_abertura
fim_fechamento.when_pressed = parar_fechamento


def girar_direita(velocidade=velocidade_rotacao):
    log_data("Girando no sentido horário")
    motor_rotacao.forward(speed=velocidade)


def girar_esquerda(velocidade=velocidade_rotacao):
    log_data("Girando no sentido anti-horário")
    motor_rotacao.backward(speed=velocidade)


def parar_giro():
    log_data("Parando giro")
    motor_rotacao.stop()

###############################################################################
#                                                                             #
# Estados                                                                     #
#                                                                             #
###############################################################################

estado = 'parado'


def estimulo():
    global teve_estimulo
    global estado
    teve_estimulo = True
    if estado == "parado":
        log_data("Mudança de estado: de 'parado' para 'direita_1'")
        abrir()
        time.sleep(5)  # tempo para abrir, verificar
        girar_direita(0.5)
        estado = 'direita_1'
        return

    elif estado == "direita_1":
        log_data("Mudança de estado: de 'direita_1' para 'direita_2'")
        girar_direita(1)
        estado = 'direita_2'
        return

    elif estado == "direita_2":
        log_data("...")
        # o que fazer? Matriz?
        # pixels[0:pixels_count_matriz] = [BRANCO] * pixels_count_matriz
        return

    elif estado == "esquerda_1":
        log_data("Mudança de estado: de 'esquerda_1' para 'esquerda_2'")
        girar_esquerda(1)
        estado = 'esquerda_2'
        return

    elif estado == "esquerda_2":
        log_data("...")
        # o que fazer?
        return

    else:
        log_data("Mudança de estado: de #ERRO para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return


def falta_de_estimulo():
    global estado
    if estado == "parado":
        log_data("Estado mantido em 'parado'")
        return

    elif estado == "direita_1":
        log_data("Mudança de estado: de 'direita_1' para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return

    elif estado == "direita_2":
        log_data("Mudança de estado: de 'direita_2' para 'esquerda_1'")
        girar_esquerda(0.5)
        estado = 'esquerda_1'
        return

    elif estado == "esquerda_1":
        log_data("Mudança de estado: de 'esquerda_1' para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return

    elif estado == "esquerda_2":
        log_data("Mudança de estado: de 'esquerda_2' para 'direita_1'")
        girar_direita(0.5)
        estado = 'direita_1'
        return

    else:
        log_data("Mudança de estado: de #ERRO para 'parado'")
        estado = 'parado'
        parar_giro()
        fechar()
        return


###############################################################################
#                                                                             #
# Loop                                                                        #
#                                                                             #
###############################################################################

while True:
    teve_estimulo = False
    time.sleep(10)
    if teve_estimulo is False:
        falta_de_estimulo()
