from brownie import accounts, config, TokenERC20
from scripts.helpful_scripts import get_account
import time


initial_supply = 1000000000000000000000000  # 1000000
token_name = "KUTUCOIN"
token_symbol = "KUTU"


def main():
    account = get_account()
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}, publish_source=True
    )

time.sleep(1)
