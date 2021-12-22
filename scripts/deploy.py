from brownie import accounts, config, SimpleStorage, network
from dotenv import load_dotenv
import os

load_dotenv()


def deploy_simple_storage():
    acc = get_account()
    simp_storage = SimpleStorage.deploy({"from": acc})
    stored_value = simp_storage.retrieve()
    txn = simp_storage.store(69, {"from": acc})
    txn.wait(1)
    updated_val = simp_storage.retrieve()
    print(updated_val)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
