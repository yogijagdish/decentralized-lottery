from brownie import accounts,config,networks

def get_account():
    if networks.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])