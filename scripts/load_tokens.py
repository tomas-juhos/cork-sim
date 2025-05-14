from .addresses import TokenAddresses

from ape import Contract


def main():
    wstETH = Contract(TokenAddresses.wstETH.value)

    tokens = {
        'wstETH': wstETH,
    }

    print("Token contracts loaded")
    return tokens
