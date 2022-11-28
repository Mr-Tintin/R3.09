import socket
import threading
import platform

OS = "os?"

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('45.154.99.5', 18618))

# Listening to Server and Sending Nickname
def receive():
    message = client.recv(1024).decode()
    sys = platform.system()
    release = platform.release()
    while message != OS:
        try:
            
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
            if message == 'os?':
                client.send(sys.encode())
                client.send(release.encode())
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
    return message    

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode())

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()