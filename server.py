#cd desktop stuff/BYUI Fall 2024/CSE 310/Module_4
#-----------------------------------------------------------------------------IMPORTS-------------------------------------------------------------------------------
import socket
import threading
import sys

#-----------------------------------------------------------------------------CONSTANTS-----------------------------------------------------------------------------
# Port can be anywhere between 0 and 65535
HOST, PORT = '127.0.0.1', 5000
# Max amount of connections the server will allow
LISTENER_LIMIT = 4
# List of all currently connected users
active_clients = []


#-----------------------------------------------------------------------------FUNCTIONS-----------------------------------------------------------------------------
# Function to listen for incoming messages from a client
def listen_for_messages(client, username):
    
    while 1:

        response = client.recv(2048).decode('utf-8')
        if response != "":
            
            final_msg = username + "~" + response
            send_messages_to_all(final_msg)
        else:
            print(f"The message sent from {username} is empty")


# Function to send a message to a single client
def send_message_to_client(client, message):
    client.sendall(message.encode())


# Function to send any new message to all the current clients
def send_messages_to_all(message): 
    for user in active_clients:
        send_message_to_client(user[1], message)


# Function to handle client
def client_handler(client):
    
    # Server will listen for client message that will
    # cotain the username. 
    while 1:
        
        username = client.recv(2048).decode('utf-8')
        if username != " ":
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} has joined the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target = listen_for_messages, args = (client, username, )).start()


# Main function
def main():

    # Creating the socket class object
    # AF_INET means indicates using ipv4 ip addresses
    # SOCK_STREAM means indicates using TCP protocol
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try/catch block
    try:
        # Provide the server with an address in the form of host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST}: {PORT}")
    except:
        print(f"Unable to bind to host {HOST}: {PORT}")

    # Set server limit
    server.listen(LISTENER_LIMIT)
 
    # This while loop will keep listening to client connections
    while 1:

        client, address = server.accept()
        print(f"Successfully connected to client {address[0]}{address[1]}")

        threading.Thread(target = client_handler, args = (client, )).start()


if __name__ == '__main__':
    main()