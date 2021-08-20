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


while True:
  try:
    for i in range(8):
      exec(his' + str(i) + ' = GPIO.input(sw)):
      time.sleep(0.0625)
  
      if his0 = his1 = his4 = his5 = 0 and his2 = his3 = his6 = his7 = 1:
        print('PinPonDetected!')
      if his0 = his1 = his4 = his5 = 1 and his2 = his3 = his6 = his7 = 0:
        print('PinPonDetected!')
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