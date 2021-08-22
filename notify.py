import requests
import subprocess

def linenotify(massage):
    TOKEN = ''
    api_url = 'https://notify-api.line.me/api/notify'
    send_contents = massage

    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)
    print('LINE Notify sent.')

def alexanotify(massage):
    subprocess.run('~/alexa_remote_control.sh -e "speak:' + massage + '"')
    print('Alexa speak command sent.')
