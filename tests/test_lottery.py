from brownie import accounts,network,config,Lottery
from scripts.helpfulScripts import get_account
from web3 import Web3

def test_lottery_entrance():
    account = get_account()
    lottery = Lottery.deploy(config["networks"][network.show_active()]["eth_usd_conversion"],{"from":account})

    assert lottery.entranceFee > Web3.toWei(0.03,"ether")
    assert lottery.entranceFee < Web3.toWei(0.035,"ether")