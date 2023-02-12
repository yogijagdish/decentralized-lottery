from brownie import Lottery

def deploy_lottery():
    lottery = Lottery.deploy({"from":account})