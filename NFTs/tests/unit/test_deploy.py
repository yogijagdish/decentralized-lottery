from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_simpleCollectable
import pytest
from brownie import network

def test_numberone():
    if network.show_active() != "development":
        pytest.skip()
    else:
        simpleCollected = deploy_simpleCollectable()
        assert simpleCollected.ownerOf(0) == get_account()