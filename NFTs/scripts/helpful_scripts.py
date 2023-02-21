from brownie import network,config,accounts

def get_account(id= None,index=None):
    if index:
        account = accounts[index]
    if id:
        account = accounts.load(id)

    if network.show_active() == "development":
        account = accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])
    
    return account