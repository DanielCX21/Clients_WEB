import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_local = "0.0.0.0"  # Aceita conexões de qualquer IP local
porta_local = 8500    # Escolha uma porta livre
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
        try:
            client_socket.send(b"Bem vindo!")
        except:
            pass

        while True:
            try:
                data = client_socket.recv(1024).decode()
                print("Mensagem recebida: ", data)
            except:
                pass
            if data.strip() == "sair":
                print("Cliente encerrou conexão")
                client_socket.send(b"Adeus!")
                client_socket.close()
                break
            try:
                resposta = input("Digite a resposta: ")
                client_socket.send(resposta.encode())
            except:
                pass
            if resposta.strip() == "fechar":
                client_socket.send(b"Adeus!")
                server.close()

    server.close()

except Exception as error:
    print("Erro:", error)
    server.close()
