import RPi.GPIO as GPIO
import time

sw = 20
led = 21

GPIO.setmode(GPIO.BCM)

#GPIO.setup(sw, GPIO.IN)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

swinfo = GPIO.input(sw)


lighthis = ['his0', 'his1', 'his2', 'his3', 'his4', 'his5', 'his6', 'his7', ]

his0 = 0
his1 = 0
his2 = 0
his3 = 0
his4 = 0
his5 = 0
his6 = 0
his7 = 0

pinponflag = False

def PinPonDetect(pinponflag):
  if pinponflag == False:
    pinponflag = True
    print('PinPonDetected!')
    time.sleep(60)
    pinponflag = False
  else:
    pass


while True:
  try:
    #print('LoopStart!')
    for i in range(8):
      execcom = 'his' + str(i) + ' = GPIO.input(sw)'
      exec(execcom)
      #print(GPIO.input(sw))

      if his0 == his1 == his4 == his5 == 0 and his2 == his3 == his6 == his7 == 1:
        PinPonDetect()
      if his0 == his1 == his4 == his5 == 1 and his2 == his3 == his6 == his7 == 0:
        PinPonDetect()
      if his1 == his2 == his5 == his6 == 1 and his0 == his3 == his4 == his7 == 0:
        PinPonDetect()
      if his1 == his2 == his5 == his6 == 0 and his0 == his3 == his4 == his7 == 1:
        PinPonDetect()
      if i == 7:
        print('LoopReset!(Scanned 8 times so reset the loop.)')

      
      time.sleep(0.0625)
  except KeyboardInterrupt:
    GPIO.cleanup()
    break

    

#while True:
#  try:
#    print(GPIO.input(sw))
#    GPIO.output(led, GPIO.input(sw))
#    time.sleep(0.0625)
#  except KeyboardInterrupt:
#    GPIO.cleanup()
#    break