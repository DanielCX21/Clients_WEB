import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_ngrok = "0.tcp.sa.ngrok.io"  # Endereço gerado pelo Ngrok
porta_ngrok = 15016  # Porta gerada pelo Ngrok

try:
    client.connect((IP_ngrok, porta_ngrok))  # Conecta ao servidor remoto
    print("Conectado ao servidor")

    j = 0
    while True:
        try:
            j += 1
            mensagem = input(f"Digite uma mensagem{j}")
            client.send(mensagem.encode())

            resposta = client.recv(1024).decode()
            print(f"Resposta do servidor{j}", resposta)
        except:
            print("Nao conseguimos enviar mensagem ou receber")

    client.close()

except Exception as error:
    print("Erro:", error)
    client.close()