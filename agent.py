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
    private_key : string 
    public_key : string 
    public_address : string 
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
    def send(self, recipent_address : string, amount : float):
        # Send money to a peer 
    def generateKeys(self): 
        # Generate the keys for the user
    def generateAddress(self):
        if(self.public_key == None):
            print("Please generate keys before generating an address") 
            return 
    def gossip(self): 
        for peer in self.peers: 
            # gossip
    def listen(self):
        
    
