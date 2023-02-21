from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io/assests/{}/{}"

def deploy_simpleCollectable():
    account = get_account()
    simple_collectable = SimpleCollectible.deploy({"from":account})
    tx = simple_collectable.publicCollectible(sample_token_uri,{"from": account})
    tx.wait(1)
    print(f"deployed!!! you can view your NFT at {OPENSEA_URL.format(simple_collectable.address,simple_collectable.tokkenCollector()-1)}")

def main():
    deploy_simpleCollectable()