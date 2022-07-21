import threading
import socket

def main():
    IP = 'localhost'
    PORT = 5000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((IP, PORT))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário: ')
    print('\nConectado!')

    thread1 = threading.Thread(target=receberMensagens, args=[cliente])
    thread2 = threading.Thread(target=sendMessages, args=[cliente, username])

    thread1.start()
    thread2.start()


def receberMensagens(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            cliente.close()
            break
            

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


main()
