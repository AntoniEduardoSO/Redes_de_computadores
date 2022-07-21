import threading
import socket

clientes = []

def init():
    IP = 'localhost'
    PORT = 5000
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind((IP, PORT))
        servidor.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        print('')
        cliente, addr = servidor.accept()
        clientes.append(cliente)
        thread = threading.Thread(target=mensagem_do_cliente, args=[cliente])
        thread.start()

def mensagem_do_cliente(cliente):
    while True:
        try:
            msg = cliente.recv(2048)
            bate_papo(msg, cliente)
        except:
            print('Cliente Retirado!')
            deletarCliente(cliente)
            break

def bate_papo(msg, cliente):
    for clienteItem in clientes:
        if clienteItem != cliente:
            try:
                clienteItem.send(msg)
            except:
                print('Cliente Retirado!')
                deletarCliente(clienteItem)

def deletarCliente(cliente):
    clientes.remove(cliente)

init()
