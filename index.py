from bottle import Bottle, request, run
import bottle
import hashlib

bottle.debug(True)
app = Bottle()

TOKEN='frank'

@app.route('/')
def index():
    timestamp =  request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce', '')
    wx_sha1_ret = request.GET.get('signature', '')
    echostr = request.GET.get('echostr', '')
    token = TOKEN
    l = [timestamp, nonce, token]
    l.sort()
    sha1_ret = hashlib.sha1(''.join(l)).hexdigest()
    return sha1_ret + '!=' + wx_sha1_ret


if __name__ == '__main__':
    run(app=app, host='localhost', port=8000, reloader=True)
