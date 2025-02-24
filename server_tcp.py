import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_local = "0.0.0.0"  # Aceita conexões de qualquer IP local
porta_local = 8080     # Escolha uma porta livre
#Após isso o Ngrok irá levar a porta 8080 ao mundo
#Para isso o Ngrok precisa estar na mesma rede

try:
    server.bind((IP_local, porta_local))
    server.listen(5)
    print(f"Servidor rodando em {IP_local}:{porta_local}")
    #Tento criar o bind, se for sucesso continuaremos

    while True:
        #Para aceitarmos diversas conexões
        client_socket, address = server.accept()
        print("Conexão recebida de:", address)
        #Vamos descobrir quem conectou em nós
        while True:
            data = client_socket.recv(1024).decode()
            print("Mensagem recebida:", data)
            if data == "sair\n":
                break

            resposta = input("De uma resposta:")
            client_socket.send(resposta.encode())

    server.close()

except Exception as error:
    print("Erro:", error)
    server.close()

