import socket

ip_address_server = input('Ip address server :')
port = int(input('Port :'))


sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock_client.connect((ip_address_server,port))


request = input('Kirim ke server :')


sock_client.send(request.encode())


response = sock_client.recv(1024)


print(f'balasan server {response.decode()}')

sock_client.close()


