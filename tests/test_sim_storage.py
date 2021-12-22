from brownie import accounts, SimpleStorage


def test_deploy():
    """
    Testing is seperated in 3 categories:
    1. Arrange
    2. Act
    3. Assert

    for testing a single test,
    brownie test -k {test function name here}
    brownie test --pdb -> really important tool for checking values.
    brownie test -s -> tells the exact fault in code.
    """
    # arrange
    acc = accounts[0]
    # act
    sim_storage = SimpleStorage.deploy({"from": acc})
    starting_value = sim_storage.retrieve()
    expected = 0
    # assert
    assert starting_value == expected


def test_updting_storage():
    # arrange
    acc = accounts[0]
    sim_storage = SimpleStorage.deploy({"from": acc})
    # act
    expected = 69
    sim_storage.store(expected, {"from": acc})
    # assert
    assert 96 == sim_storage.retrieve()
