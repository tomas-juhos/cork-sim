"""Main script to facilitate testing."""

from .load_contracts import main as lc
from .load_tokens import main as lt


def main():
    c = lc()
    t = lt()

    bal = t['wstETH'].balanceOf(c['cork_module_core'].address) / 10**t['wstETH'].decimals()

    print(f'Balance of wstETH in Cork Module Core: {bal}')
