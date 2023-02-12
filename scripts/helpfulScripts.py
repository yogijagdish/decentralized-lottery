from brownie import accounts,config,networks

def get_account():
    if networks.show_active == "development":
        account = accounts[0]
    else:
        account = 