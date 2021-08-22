from subprocess import call
import RPi.GPIO as GPIO
import time
import datetime
import threading
import notify

#GPIO pin set
lightsensor = 20
callsw = 17
led = 21

#Setmode set
GPIO.setmode(GPIO.BCM)

#GPIO setup
GPIO.setup(lightsensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(callsw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

#GPIO interrupt setting
GPIO.add_event_detect(callsw, GPIO.RISING, bouncetime=1000)

GPIO.add_event_callback(callsw)

#sensor history, flag init
swinfo = GPIO.input(lightsensor)

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

#Setting func

def PinPonNotify():
  global pinponflag
  pinponflag = True
  print('PinPonDetected!', datetime.datetime.now())
  notify.linenotify('ピンポンテスト')
  #notify.alexanotify()
  time.sleep(10)
  pinponflag = False
  print('PinPonReset!')

def PinPonDetect():
  global pinponflag
  if pinponflag == False:
    notfy = threading.Thread(target=PinPonNotify)
    notfy.start()
  else:
    pass

def CallNotify():
  notify.linenotify('ボタンテスト')


#Main roop
while True:
  try:
    #print('LoopStart!')
    for i in range(8):
      execcom = 'his' + str(i) + ' = GPIO.input(lightsensor)'
      exec(execcom)
      #print(GPIO.input(sw))

      if his0 == his1 == his4 == his5 == 0 and his2 == his3 == his6 == his7 == 1:
        PinPonDetect()
        #print('PinPon!')
      if his0 == his1 == his4 == his5 == 1 and his2 == his3 == his6 == his7 == 0:
        PinPonDetect()
        #print('PinPon!')
      if his1 == his2 == his5 == his6 == 1 and his0 == his3 == his4 == his7 == 0:
        PinPonDetect()
        #print('PinPon!')
      if his1 == his2 == his5 == his6 == 0 and his0 == his3 == his4 == his7 == 1:
        PinPonDetect()
        #print('PinPon!')
      #if i == 7:
        #print('LoopReset!(Scanned 8 times so reset the loop.)')

      
      time.sleep(0.0625)
  except KeyboardInterrupt:
    GPIO.cleanup()
    break

    
#Trash code

#while True:
#  try:
#    print(GPIO.input(sw))
#    GPIO.output(led, GPIO.input(sw))
#    time.sleep(0.0625)
#  except KeyboardInterrupt:
#    GPIO.cleanup()
#    break