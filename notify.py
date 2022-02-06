import requests
import subprocess
import datetime

misskeysendcommand = 'curl -H "Content-Type: application/json" -X POST -d ' + '\'{"i": "", "text": "@sim1222@misskey.io お客様が来てますよ！"}\'' + ' https://simkey.net/api/notes/create'

def linenotify(massage):
    TOKEN = ''
    api_url = 'https://notify-api.line.me/api/notify'
    send_contents = massage

    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)
    print('LINE Notify sent.', massage, datetime.datetime.now())

def alexanotify(massage):
    subprocess.run('~/alexa_remote_control.sh -e "speak:' + massage + '"', shell=True)
    print('Alexa speak command sent.', massage ,datetime.datetime.now())

def homebridgenotify():
    subprocess.run("curl -X POST -d 'ding=dong&dong=ding' http://192.168.1.12:9999", shell=True)
    print('HomeBridge request sent.', datetime.datetime.now())

def misskeynotify():
    print(misskeysendcommand)
    subprocess.run(misskeysendcommand, shell=True)
    print('Misskey sent.', datetime.datetime.now())