import time

from ape import Contract

from .addresses import TokenAddresses



def main():
    # LV = Contract(TokenAddresses.LV)
    wstETH = Contract(TokenAddresses.wstETH)
    time.sleep(1)
    WETH = Contract(TokenAddresses.WETH)
    sUSDe = Contract(TokenAddresses.sUSDe)
    time.sleep(1)
    sUSDS = Contract(TokenAddresses.sUSDS)
    wstUSR = Contract(TokenAddresses.wstUSR)
    time.sleep(1)
    USDe = Contract(TokenAddresses.USDe)
    USDN = Contract(TokenAddresses.USDN)

    CT = Contract(TokenAddresses.CT)
    DS = Contract(TokenAddresses.DS)

    tokens = {
        # "LV": LV,
        "wstETH": wstETH,
        "WETH": WETH,
        "sUSDe": sUSDe,
        "sUSDS": sUSDS,
        "wstUSR": wstUSR,
        "USDe": USDe,
        "USDN": USDN,
    }

    print("Token contracts loaded")
    return tokens
