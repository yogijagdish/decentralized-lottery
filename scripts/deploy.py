from brownie import Lottery,networks,config

from scripts.helpfulScripts import get_account

def deploy_lottery():

    account = get_account()

    if networks.show_active() == "development":
        pass
    else:
        priceFeedAddress = config["networks"][networks.show_active()]["eth_usd_conversion"]
    lottery = Lottery.deploy(priceFeedAddress,{"from":account})