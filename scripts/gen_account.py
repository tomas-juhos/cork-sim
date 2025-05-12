from ape import accounts

def main():
    # 1) generate an unfunded test account
    acct = accounts.test_accounts.generate_test_account()
    # 2) fund it with 1 ETH (in wei)
    acct.balance += 10**18
    # 3) spit out the address
    print(f"New test account: {acct.address}")
    print(f"Funded with {acct.balance / 10**18} ETH on your fork")

main()