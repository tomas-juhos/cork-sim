#!/usr/bin/env bash
# entrypoint.sh

# 1) Start Anvil (forked) in the background
anvil \
  --fork-url "${MAINNET_RPC}" \
  --fork-block-number "${FORK_BLOCK:-latest}" \
  --host 0.0.0.0 \
  --port 8545 &

# 2) Keep the container alive
exec tail -f /dev/null
