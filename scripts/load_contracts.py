from scripts.addresses import ContractAddresses

from ape import Contract


def main():
    cork_config = Contract(ContractAddresses.CORK_CONFIG)
