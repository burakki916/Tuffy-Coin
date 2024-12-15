# Create n agents who will be attempting to send and recieve money 
# each user has their own version of ledger that they will be updating 
# So we need a user script, which simulates how the users will be interacting with the program 
# The goal of this file is to just create the users and provide an interface for them to interact with each other 
from agent import Agent

if __name__ == "__main__":
    agentNames = ["Alice", "Bob", "Charlie", "David" ] 
    agentPorts = [5000, 5001, 5002, 5003]
    agents = []
    for agent in agentNames: 
        agents.append(Agent(agent, agentPorts.pop(0)))
