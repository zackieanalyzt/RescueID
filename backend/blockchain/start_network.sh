#!/bin/bash

# Generate cryptographic material
cryptogen generate --config=./crypto-config.yaml

# Generate genesis block
configtxgen -profile TwoOrgsOrdererGenesis -channelID system-channel -outputBlock ./channel-artifacts/genesis.block

# Start the network
docker-compose -f docker-compose.yaml up -d
