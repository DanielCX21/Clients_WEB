import socket

IP_adress = "0.tcp.sa.ngrok.io"
port = 15669

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    print(f"Tentando conexão a {IP_adress}:{port}...")
    client.connect((IP_adress, port))  # Conecta ao servidor remoto
    print("Conectado ao servidor")

    #exemplo de requisição
    #request = f"GET / HTTP/1.1\r\nHOST: {IP_adress}\r\n\r\n"
    #o www.google.com responderia essa requisição positivamente 
    #e mandaria o código HTML para o navegador carregar o front-end

    j = 0
    while True:
        try:
            j += 1
            mensagem = input(f"Digite uma mensagem {j}: ")
            client.send(mensagem.encode())

            resposta = client.recv(1024).decode()
            print(f"Resposta do servidor {j}: ", resposta)
        except:
            print("Nao conseguimos enviar mensagem ou receber")

    client.close()

except Exception as error:
    print("Erro:", error)
    client.close()
