from bluetooth import *

HOST = ''
PORT = 3
socket=BluetoothSocket( RFCOMM )

socket.bind((HOST, PORT))
socket.listen(1)

connexion, addresse = socket.accept()

print ('Connecte a : ', addresse)

while True:
    data = "coucou"
    if not data: break
    connexion.send(data)

connexion.close()