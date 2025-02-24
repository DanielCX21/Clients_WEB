import socket

IP_adress = "127.0.0.1"
porta = 4433

try:
    while True:
        mensagem = "mensagem"
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(mensagem.encode(), (IP_adress, porta))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "sair\n" or mensagem == "sair\n":
            break

    client.close()
except Exception as error:
    print("Erro!")
    print(error)
