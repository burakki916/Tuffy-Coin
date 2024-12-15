# Create n agents who will be attempting to send and recieve money 
# each user has their own version of ledger that they will be updating 
# So we need a user script, which simulates how the users will be interacting with the program 
# The goal of this file is to just create the users and provide an interface for them to interact with each other 
from agent import Agent
agentFolder = "./agents"
if __name__ == "__main__":
    agent_names = ["Makaio", "Lev", "Lens", "Kian", "Carrera", "Jacob" ,"mchll"]   
    agentPorts = 
    {
        Makaio: 3000,
        Lev: 3001,
        Lens: 3002,
        Carrera: 3003
    }
    agent_public_address = {}
    agents = {}
    # Create the seeders 
    # Create the first user 
    adam = Agent("Adam", 3004) 
    adam.miner = True 
    adam.generateKeys()
    adam.generateLegder()
    adam.start_minning() 

    # Create the gensis Block 


    # Create the agents
    for agent_name in agent_names:
        # Check to see if the agent folder exists, if not create it. if it does exist, then we can create the agent from that 

        agentFolder = "./agents/" + agent
        if not os.path.exists(agentFolder):
            os.mkdir(agentFolder)
        agent = Agent(agent_name, agentPorts[agent])
        agents[agent_name] = agent 
        adam.send(agent.public_address, 100) 

    
    # Have 
