from bluetooth import *
import donneeDAO

while True:
    HOST = ''
    PORT = 3
    socket=BluetoothSocket( RFCOMM )

    socket.bind((HOST, PORT))
    socket.listen(1)

    connexion, addresse = socket.accept()
    data = ""
    data = donneeDAO.recupererValeurDifferee()
    print ('Connecte a : ', addresse)
    pretEnvoyer = None

    if addresse is not None :
        while pretEnvoyer is None:
            pretEnvoyer = connexion.recv(1024)

        if pretEnvoyer is not None:
            connexion.send(data)
            data = ""            
            pretEnvoyer = None
            
        connexion.close()

    