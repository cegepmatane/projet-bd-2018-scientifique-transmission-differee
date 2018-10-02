import simplejson as json
from socketIO_client_nexus import SocketIO, LoggingNamespace
import donneeDAO


def on_connect(msg):
	print(json.loads(msg))

def on_send():
    print("data sent")

    connexion = SocketIO('vps202433.vps.ovh.ca', 8080, LoggingNamespace)
    #print('hello')
    connexion.on('salutation', on_connect)

    while True:
        StringToSend = donneeDAO.listerDonnee()
        print(StringToSend)
        connexion.emit('aaa', json.dumps(StringToSend))
        print("sent")
        connexion.wait(0.5)
