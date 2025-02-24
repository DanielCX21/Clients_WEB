import paramiko

host = "127.0.0.1"
user = "kali"
passwd = "kali"

#protocolo de comunicação mais seguro e criptografado
#permite executar comandos => podemos pensar
#em shell reversa
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(host, username=user, password=passwd)
    while True:
        stdin, stdout, stderr = client.exec_command(input("Comando: "))

        for line in stdout.readLines():
            print(line.strip())

        erros = stderr.readlines()
        if erros:
            print(erros)
except:
    print("nao conectou")
