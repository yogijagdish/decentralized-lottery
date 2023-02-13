from brownie import Lottery,network,config

from scripts.helpfulScripts import get_account,deploy_mocks

def deploy_lottery():

    account = get_account()

    if network.show_active() == "development":
        priceFeedAddress = deploy_mocks()
    else:
        priceFeedAddress = config["networks"][network.show_active()]["eth_usd_conversion"]
    lottery = Lottery.deploy(priceFeedAddress,{"from":account})
    print(f"Contracts deployed to ${lottery.address}")

def main():
    deploy_lottery()