# Dockerfile.dev
FROM ghcr.io/apeworx/ape:latest

# 1) Become root to install deps
USER root

# 2) Install OS packages
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl git \
 && rm -rf /var/lib/apt/lists/*

# 3) Tell Docker where Foundry will live, and put it on PATH
ENV FOUNDRY_HOME=/root/.foundry
ENV PATH=${FOUNDRY_HOME}/bin:${PATH}

# 4) Install Foundry (forge & anvil) and immediately run foundryup
RUN curl -L https://foundry.paradigm.xyz | bash \
 && foundryup

WORKDIR /app

# 5) Copy in your code & entrypoint
COPY --chown=ape:ape . /app
COPY --chown=ape:ape entrypoint.sh /usr/local/bin/entrypoint.sh

# 6) Make sure entrypoint is executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# 7) Expose the Anvil RPC port
EXPOSE 8545

# 8) Kick off Anvil then hang so the container stays alive
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
