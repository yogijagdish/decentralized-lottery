from brownie import accounts,config,network,MockV3Aggregator
from web3 import Web3

DECIMAL = 18
INITIAL_ANSWER = 2000

def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"Currently we are active on Network ${network.show_active()}")
    print("Deploying mocks")
    mockAddress = MockV3Aggregator.deploy(DECIMAL,Web3.toWei(INITIAL_ANSWER,"ether"),{"from":get_account()})
    print("Mocks deployed")
    return mockAddress.address