import socket


localhost = '127.0.0.1'
port = 8080




sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
sock_server.bind((localhost,port))



sock_server.listen()
print('server ready...')


while True:
    sock_clint, client_address = sock_server.accept()
    request = sock_clint.recv(1024).decode()

    print(f'request dari clinet {request}')


    response = f"ini dari server: {request}"


    sock_clint.send(response.encode())


    sock_clint.close()


#end
sock_server.close()
