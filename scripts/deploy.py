from brownie import Lottery

from scripts.helpfulScripts import get_account,get_contract

def deploy_lottery():

    account = get_account()
    contract = get_contract()

    lottery = Lottery.deploy(contract,{"from":account})
    print(f"Contracts deployed to ${lottery.address}")


def deploy_start_lottery():

    lottery = Lottery[-1]
    tx_wait = lottery.startLottery({"from": get_account()})
    tx_wait.wait(1)
    print("Lottery has started")

def deploy_enter():
    lottery = Lottery[-1]
    value = lottery.entranceFee()
    print(value)
    tx_wait = lottery.Enter({"from":get_account(),"value": 26})
    tx_wait.wait(1)
    print("you have entered for the lottery")

def deploy_get_rates():
    lottery = Lottery[-1]
    value = lottery.entranceFee()
    print(value)

def main():
    deploy_lottery()
    deploy_start_lottery()
    deploy_get_rates()
    deploy_enter() 
