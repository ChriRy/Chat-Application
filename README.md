# Overview

{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}
This is a chat application for windows built using python. At the moment it's designed to work on local systems, but later there will be additions so that multiple computers can use it.
To get it running, first start up the server.py program and have that running. From there you can open up multiple chat windows, input a username, and join the chat room

In the past I've mostly written programs that only deal with data or simple user entries, so I wanted to try a project that had more of a real world application, and sending
data between computers seemed like a good way to expand my experience. 

[Software Demo Video](https://youtu.be/_e2yTOnUfvc)

# Network Communication

This program is designed to be a client/server system that connects to the server using port 5000. 
Messages are sent using the .encode and .decode functions with respect to utf-8. 

# Development Environment

This program was built in VS Code using the python language. 

This program uses socketserver, socket, and threading to handle the networking aspects, and the tkinter library was used for the GUI. 

# Useful Websites

[Python Networking Tutorial](https://www.youtube.com/watch?v=hBnOdIg0jAM)

# Future Work

* Improve the look of the GUI and make it more dynamic
* Redesign the program to work between multiple computers (currently its only in a test phase that works on one computer)
* Have a designated server (connect to internet?)
