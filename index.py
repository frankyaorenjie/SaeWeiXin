from bottle import Bottle, request
import hashlib

app = Bottle()

TOKEN='zabbix'

@app.route('/')
def hello():
    timestamp =  request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce', '')
    wx_sha1_ret = request.GET.get('signature', '')
    echostr = request.GET.get('echostr', '')
    token = TOKEN
    l = [timestamp, nonce, token]
    l.sort()
    sha1_ret = hashlib.sha1(''.join(l))
    return sha1_ret + '?=' + wx_sha1_ret