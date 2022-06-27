import socket
import os
IP = input('The ip of the host machine:- ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, 8080))
s.listen()

print('listening.........')
cli, ip = s.accept()
print(f'connection from {ip}!')


while True:
    file_name = input("Enter the name of the file you want to send(press q to quit):-")

    if file_name == "q" or file_name == "quit":
        cli.send(file_name.encode())
        break

    elif os.path.exists(file_name):
        cli.send(file_name.encode())
        file = open(file_name, 'rb')
        file_data = file.read()
        cli.send(file_data)
        file.close()

    else:
        print('file does not exist')


