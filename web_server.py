#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:21:56 2017

@author: root
"""
# First of all we import socket library

import socket

# Next create a socket object
s = socket.socket()
print ("Socket successfully created ")

# Reserve a port number
port = 12345

# Bind to the port
s.bind(('',port))
print("Socket binded to %s " %(port))

# Put the socket into listening mode
s.listen(5)
print("Socket is now listening ")

# Forever loop untill we exit
# Or an error occurs

while True:
# Establish connection with client
    c, addr = s.accept()
    print ("Got connection from: ", addr)
    
    
    

