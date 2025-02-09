from backend.api.blockchain_integration import connect_to_blockchain, deploy_contract, add_victim_data

def main():
    web3 = connect_to_blockchain()
    contract_path = "backend/blockchain/contracts/RescueID.sol"
    contract_address = deploy_contract(web3, contract_path)

    # Load ABI from compiled contract
    with open("backend/blockchain/contracts/RescueID.json", "r") as file:
        abi = json.load(file)["abi"]

    # Example: Add victim data
    result = add_victim_data(web3, contract_address, abi, "John Doe", "1234567890", "Asthma", "Peanuts")
    print("Transaction Receipt:", result)

if __name__ == "__main__":
    main()
