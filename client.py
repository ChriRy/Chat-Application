#-----------------------------------------------------------------------------IMPORTS-------------------------------------------------------------------------------
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

#-----------------------------------------------------------------------------CONSTANTS-----------------------------------------------------------------------------
# Creating a socket object
# AF_INET means indicates using ipv4 ip addresses
# SOCK_STREAM means indicates using TCP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST, PORT = '127.0.0.1', 5000

# Colors (replace with sandstone style color scheme)
DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = '#FFFFFF'

# Fonts
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

#-----------------------------------------------------------------------------FUNCTIONS--------------------------------------------------------------------------------

def connect():
    # Connect to the server
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server {HOST}: {PORT}")
        add_message("[SERVER] Successfully connected to the server")
    except:
        print(f"Unable to connect to server {HOST}: {PORT}")
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST}: {PORT}")

    # Get a username from the user
    username = username_textbox.get()
    if username != '':
        # Send the username over to the server
        client.sendall(username.encode())
    else:
        message_box.showerror("Invalid username", "Username cannot be empty")

    # Create a new thread to listen for messages from the server
    threading.Thread(target = listen_for_messages_from_server, args = (client, )).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)


def send_message():
        # Wait for the message from the user
        message = message_textbox.get()
        if message != '':
            # Send the message to the server (utf-8 is default for encode, so we don't have to type it)
            client.sendall(message.encode())
            message_textbox.delete(0, len(message)) # clears out the textbox after a message is sent
        else:
            messagebox.showerror("Empty message", "Message cannot be empty")


# Function that adds the given message to the next line in the message box
def add_message(message):
    message_box.config(state = tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state = tk.DISABLED)


# Function to handle listening for messages from the server
def listen_for_messages_from_server(client):
    
    while 1:
        # Receive the message from the server
        message = client.recv(2048).decode("utf-8")
        if message != '':
            # Uses the '~' character to split between username and the actual message
            username = message.split("~")[0]
            content = message.split("~")[1]

            add_message(f"[{username}]: {content}")
        else:
            print("Message received from client is empty")

def main():
    
    # Starts the Tkinter main loop
    root.mainloop()



#--------------------------------------------------------------------------------GUI--------------------------------------------------------------------------------
root = tk.Tk()
root.geometry("600x600")        # Sets the width and height of the window (in pixels)
root.title("Pachinko")          # Changes the title of the application
root.resizable(False, False)    # Keeps the user from resizing the window by width or height

# Configure grid to help the frames stay constant
root.grid_rowconfigure(0, weight = 1) # height has to be 1/6
root.grid_rowconfigure(1, weight = 4) # height has to be 4/6
root.grid_rowconfigure(2, weight = 1) # height has to be 1/6

# Create the different frames and position them
top_frame = tk.Frame(root, width = 600, height = 100, bg = DARK_GREY)
top_frame.grid(row = 0, column = 0, sticky = tk.NSEW)

middle_frame = tk.Frame(root, width = 600, height = 400, bg = MEDIUM_GREY)
middle_frame.grid(row = 1, column = 0, sticky = tk.NSEW)

bottom_frame = tk.Frame(root, width = 600, height = 100, bg = DARK_GREY)
bottom_frame.grid(row = 2, column = 0, sticky = tk.NSEW)

# Top frame widgets
username_label = tk.Label(top_frame, text = "Enter username: ", font = FONT, bg = DARK_GREY, fg = WHITE)
username_label.pack(side = tk.LEFT, padx = 10)  # align the label to the left, horizontal padding = 10 pixels

username_textbox = tk.Entry(top_frame, font = FONT, bg = MEDIUM_GREY, fg = WHITE, width = 23)   
username_textbox.pack(side = tk.LEFT)

username_button = tk.Button(top_frame, text = "Join", font = FONT, bg = OCEAN_BLUE, fg = WHITE, command = connect)
username_button.pack(side = tk.LEFT, padx = 15)

# Middle frame widgets

message_box = scrolledtext.ScrolledText(middle_frame, font = SMALL_FONT, bg = MEDIUM_GREY, fg = WHITE, width = 67, height = 26.5) # lets the user scroll in the middle frame
message_box.config(state = tk.DISABLED) # disables the middle frame so the user can't write on it
message_box.pack(side = tk.TOP)

# Bottom frame widgets
message_textbox = tk.Entry(bottom_frame, font = FONT, bg = MEDIUM_GREY, fg = WHITE, width = 38)
message_textbox.pack(side = tk.LEFT, padx = 10)

message_button = tk.Button(bottom_frame, text = "Send", font = BUTTON_FONT, bg = OCEAN_BLUE, fg = WHITE, command = send_message)
message_button.pack(side = tk.LEFT, padx = 10)





    
if __name__ == "__main__":
    main()