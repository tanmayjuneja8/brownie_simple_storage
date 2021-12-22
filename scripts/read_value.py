from brownie import accounts, config, SimpleStorage, network


def read_contract():
    sim_storage = SimpleStorage[-1]
    """
    Brownie already knows the contract's abi and address.
    """
    print(sim_storage.retrieve())


def main():
    read_contract()
