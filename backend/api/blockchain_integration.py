from web3 import Web3
import json

# Connect to a local Ethereum node (e.g., Ganache)
def connect_to_blockchain():
    web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    if web3.isConnected():
        print("Connected to Blockchain!")
    return web3

# Compile and deploy the smart contract
def deploy_contract(web3, contract_path):
    with open(contract_path, "r") as file:
        contract_source_code = file.read()

    # Compile the contract (requires solc installed locally)
    compiled_sol = compile_source(contract_source_code)
    contract_interface = compiled_sol['<stdin>:RescueID']

    # Deploy the contract
    account = web3.eth.accounts[0]
    contract = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
    tx_hash = contract.constructor().transact({'from': account})
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Contract deployed at address: {tx_receipt.contractAddress}")
    return tx_receipt.contractAddress

# Interact with the smart contract
def add_victim_data(web3, contract_address, abi, name, thai_id, medical_history, allergies):
    account = web3.eth.accounts[0]
    contract = web3.eth.contract(address=contract_address, abi=abi)

    # Add victim data
    tx_hash = contract.functions.addVictim(name, thai_id, medical_history, allergies).transact({'from': account})
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return receipt
