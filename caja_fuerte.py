import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

GPIO.cleanup() #se reinician pines de la raspberry
GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(21,GPIO.OUT)    #Ponemos el pin 21 como salida
servomotor = GPIO.PWM(21,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
servomotor.start(40)               #Enviamos un pulso del 7.5% para centrar el servo

def PrenderLedVerde():
    GPIO.output(7,True)
def ApagarLedVerde():
    GPIO.output(7,False)
def PrenderLedRojo():
    GPIO.output(11,True)
def ApagarLedRojo():
    GPIO.output(11,False)
def AbrirCerradura():
    servomotor.ChangeDutyCycle(11.0)
def CerrarCerradura():
    servomotor.ChangeDutyCycle(5.0)

try:
    #iniciamos el ciclo
    

except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    servomotor.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
