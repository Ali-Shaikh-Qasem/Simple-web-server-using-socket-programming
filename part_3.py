from socket import *

def send_error_file(connection_socket, client_ip, client_port):
    connection_socket.send('HTTP/1.1 404 Not Found \r\n'.encode())
    connection_socket.send('Content-Type: text/html; charset=utf-8\r\n'.encode())
    connection_socket.send('\r\n'.encode())
    page = f"""<html>
    <title>Error404</title>
    <body>
        <center>
        <h1 style="color: red;">The file is not found</h1> 
        <hr> 
        <p style="font-weight: bold;"><strong>Ali Shaikh Qasem</strong> - <strong>1212171</strong></p>
        <p style="font-weight: bold;"><strong>Abdelrahman Jaber</strong> - <strong>1211769</strong></p>
        <p style="font-weight: bold;"><strong>Ahmed Saqer</strong> - <strong>1210085</strong></p>
        <hr> 
        <h2> IP: {client_ip} , Port: {client_port} </h2>
        </center>
    </body>
</html>""" .encode()
    connection_socket.send(page)


# initialize the server
server_port = 6060
server_socket = socket(AF_INET, SOCK_STREAM) # sock_Stream for TCP connection
server_socket.bind(('', server_port)) # connect port to the socket
server_socket.listen(1) # wait for connection
print("The server is ready to receive requests")


# handling requests
while True:
    connection_socket, addr = server_socket.accept()
    client_ip = addr[0]
    client_port = addr[1]
    print("Got connection from IP = " + client_ip + "Port = " + str(client_port))
    sentence = connection_socket.recv(1024).decode()
    print("request is: " + sentence )


    # obtain the requset part from the whole received message 
    request = sentence.split()[1]
    # providing the approbriate file base on the request
    if  (request == '/' or request == '/index.html' or request == '/main_en.html' or request == '/en'):
        connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
        connection_socket.send('Content-Type: text/html \r\n'.encode())
        connection_socket.send('\r\n'.encode())
        with open("main_en.html", "rb") as f:
            content = f.read()
            connection_socket.send(content)

    elif  (request == '/ar'):
        connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
        connection_socket.send('Content-Type: text/html \r\n'.encode())
        connection_socket.send('\r\n'.encode())
        with open("main_ar.html", "rb") as f:
            content = f.read()
            connection_socket.send(content)

    elif  ( request.endswith('.html')):
        file_name = request[1:] # to remove the '/' cahracter
        try:
            with open(file_name, "rb") as f:
                connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
                connection_socket.send('Content-Type: text/html \r\n'.encode())
                connection_socket.send('\r\n'.encode())
                content = f.read()
                connection_socket.send(content)
        except FileNotFoundError:
            send_error_file(connection_socket, client_ip, client_port)
    
    elif  ( request.endswith('.css')):
        file_name = request[1:] # to remove the '/' cahracter
        try:
            with open(file_name, "rb") as f:
                connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
                connection_socket.send('Content-Type: text/css \r\n'.encode())
                connection_socket.send('\r\n'.encode())
                content = f.read()
                connection_socket.send(content)
        except FileNotFoundError:
            send_error_file(connection_socket, client_ip, client_port)
    
    elif  ( request.endswith('.png') and not request.startswith('/myform.html?name=')):
        file_name = "images/"+ request[1:] # to remove the '/' cahracter
        try:
            with open(file_name, "rb") as f:
                connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
                connection_socket.send('Content-Type: image/png \r\n'.encode())
                connection_socket.send('\r\n'.encode())
                content = f.read()
                connection_socket.send(content)
        except FileNotFoundError:
            send_error_file(connection_socket, client_ip, client_port)
    
    elif  ( request.endswith('.jpg') and not request.startswith('/myform.html?name=')):
        file_name ="images/"+ request[1:] # to remove the '/' cahracter
        try:
            with open(file_name, "rb") as f:
                connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
                connection_socket.send('Content-Type: image/jpg \r\n'.encode())
                connection_socket.send('\r\n'.encode())
                content = f.read()
                connection_socket.send(content)
        except FileNotFoundError:
            send_error_file(connection_socket, client_ip, client_port)
    elif (request.endswith('.png')):
        # Split the string using "=" as a delimiter
        parts = request.split("=")
        # Get the second part
        request = parts[1]
        try:
            with open('images/' + request, "rb") as f:
                connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
                connection_socket.send('Content-Type: image/png; charset=utf-8\r\n'.encode())
                connection_socket.send('\r\n'.encode())
                content = f.read()
                connection_socket.send(content)
        except FileNotFoundError:
            send_error_file(connection_socket, client_ip, client_port)

    elif (request.endswith('.jpg')):
        # Split the string using "=" as a delimiter
        parts = request.split("=")
        # Get the second part
        request = parts[1]
        try:
            with open('images/' + request, "rb") as f:
                connection_socket.send('HTTP/1.1 200 OK \r\n'.encode())
                connection_socket.send('Content-Type: image/jpg; charset=utf-8\r\n'.encode())
                connection_socket.send('\r\n'.encode())
                content = f.read()
                connection_socket.send(content)
        except FileNotFoundError:
            send_error_file(connection_socket, client_ip, client_port)


    elif  (request == '/so'):
        connection_socket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())
        connection_socket.send('Content-Type: text/html \r\n'.encode())
        connection_socket.send('Location: https://stackoverflow.com/ \r\n'.encode())

    elif  (request == '/itc'):
        connection_socket.send('HTTP/1.1 307 Temporary Redirect \r\n'.encode())
        connection_socket.send('Content-Type: text/html \r\n'.encode())
        connection_socket.send('Location: https://itc.birzeit.edu/ \r\n'.encode())

    else:
        send_error_file(connection_socket, client_ip, client_port)   
    # close the connection 
    connection_socket.close()
   





