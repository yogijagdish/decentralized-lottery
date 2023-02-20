from brownie import accounts,config,network, MockV3Aggregator
from web3 import Web3

DECIMAL = 18
INITIAL_ANSWER = 2000

def get_account(id=None,index=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if network.show_active == "development":
        return accounts[5]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"Currently we are active on Network ${network.show_active()}")
    print("Deploying mocks")
    mockAddress = MockV3Aggregator.deploy(DECIMAL,Web3.toWei(INITIAL_ANSWER,"ether"),{"from":get_account()})
    print("Mocks deployed")
    return mockAddress.address

def get_contract():
    if network.show_active() == "development":
        priceFeedAddress = deploy_mocks()
    else:
        priceFeedAddress = config["networks"][network.show_active()]["eth_usd_conversion"]

    return priceFeedAddress