import socket
IP = input('The ip of the host machine:-')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, 9592))
print('connected')


while True:
    fn = s.recv(500)
    if fn.decode() == 'q' or fn.decode() == 'quit':
        break
    else:
        while True:
            print('name has been received')
            s.settimeout(10)
            file = open(fn.decode(), 'wb')
            data = s.recv(5000)
            print('please wait')
            while data:
                file.write(data)
                try:
                    data = s.recv(5000)
                except socket.timeout:
                    break
            s.settimeout(None)
            file.close()
            print('done')
            break



