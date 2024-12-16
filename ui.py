# Make a ui for each person to interact with the network 
from user import User
import os
def tranfer_menu(): 
    print("\n")
    print("Transfer Menu")
    print("Amount : ")
    amount = float(input()) 
    print( "Recipeint Public Address : ")
    recipient = input()
    user.transfer(amount, recipient)
def toggle_miner(): 
    user.toggle_miner() 

if __name__ == "__main__":
    print("Welcome to Tuffy Coin!")
    config_path = "config.json"
    if !os.path.exists(config_path):
        print("Config file not found")
        exit(1)
    config = json.load(open(config_path))
    print("Config file loaded") 
    user = User(config["username"], config["port"])

    while True: 
        print("Balance : ", user.getBalance())
        if user.miner == True:
            print("Minning : On")
        else:
            print("Minning : Off")
        
        print("1. Transfer")
        print("2. Toggle Miner")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            transfer_menu()
        elif choice == 2:
            toggle_miner()
        elif choice == 3:
            break
        else: