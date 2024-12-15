import socket 
import threading 

# local Imports 
from ledger import Ledger
from wallet import Wallet
#
class Agent:  
    # Data 
    wallet  : Wallet
    directory : string
    uid :stirng 
    port : int  
    ip : string 
    peers : list 
    path : string  
    ledger : Ledger 

    # Methods 
    def __init__(self, uid : string, port: int): 
        # Generate the user, and begin their p2p network 
        self.uid = uid
        self.port = port 
    def add_peer(self, peer : Peer): 
        # Add a peer to the network 
        self.peers.append(peer) 
    def remove_peer(self, peer : Peer):
        # Remove a peer from the network 
        self.peers.remove(peer)
    def send(self, peer : Peer, amount : float):
        # Send money to a peer 
        
    
