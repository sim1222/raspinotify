import requests
import subprocess

def linenotify():
    TOKEN = ''
    api_url = 'https://notify-api.line.me/api/notify'
    send_contents = 'てすと'

    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)

def alexanotify():
    subprocess.run('~/alexa_remote_control.sh -e "speak:テスト"')
