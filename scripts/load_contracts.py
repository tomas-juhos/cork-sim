
import time

from ape import Contract

from .addresses import ContractAddresses


def main():
    cork_config = Contract(ContractAddresses.CORK_CONFIG.value)
    cork_flashswap_router = Contract(ContractAddresses.CORK_FLASHSWAP_ROUTER.value)
    time.sleep(1)
    cork_module_core = Contract(ContractAddresses.CORK_MODULE_CORE.value)
    cork_hook = Contract(ContractAddresses.CORK_HOOK.value)
    time.sleep(1)
    cork_token_factory = Contract(ContractAddresses.CORK_TOKEN_FACTORY.value)
    cork_liquidity_token = Contract(ContractAddresses.CORK_LIQUIDITY_TOKEN.value)
    time.sleep(1)
    cork_exchange_rate_provider = Contract(ContractAddresses.CORK_EXCHANGE_RATE_PROVIDER.value)
    cork_withdrawl = Contract(ContractAddresses.CORK_WITHDRAWL.value)
    time.sleep(1)
    uniswap_v4_universal_router = Contract(ContractAddresses.UNISWAP_V4_UNIVERSAL_ROUTER.value)
    uniswap_v4_pool_manager = Contract(ContractAddresses.UNISWAP_V4_POOL_MANAGER.value)
    time.sleep(1)

    contracts = {
        'cork_config': cork_config,
        'cork_flashswap_router': cork_flashswap_router,
        'cork_module_core': cork_module_core,
        'cork_hook': cork_hook,
        'cork_token_factory': cork_token_factory,
        'cork_liquidity_token': cork_liquidity_token,
        'cork_exchange_rate_provider': cork_exchange_rate_provider,
        'cork_withdrawl': cork_withdrawl,
        'uniswap_v4_universal_router': uniswap_v4_universal_router,
        'uniswap_v4_pool_manager': uniswap_v4_pool_manager,
    }

    print("Cork Protocol contracts loaded")
    return contracts
