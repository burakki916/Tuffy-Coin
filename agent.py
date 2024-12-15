import socket 
import threading 
import hashing
#Importshashing.py 

class Agent:  
    
    def __init__(self, uid : string, port: int): 
        # Generate the user, and begin their p2p network 
        self.uid = uid
        self.port = port 

