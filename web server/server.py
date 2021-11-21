import socket

def tcp_server():
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

        response = handle_request()

        sock_clint.send(response.encode())


        sock_clint.close()


    #end
    
    sock_server.close()



def handle_request():

    response_line = 'HTTP/1.1 200 OK\r\n'
    content_type = 'Content Type: Text/html\r\n\r\n'

    file = open("filehtml/index.html",'r')
    message_body = file.read()
    file.close()


    response = response_line+content_type+message_body
    return response




if __name__ == '__main__':
    tcp_server()

