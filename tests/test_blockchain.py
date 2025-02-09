import unittest
from backend.api.blockchain_integration import connect_to_blockchain, deploy_contract, add_victim_data
import json

class TestBlockchainIntegration(unittest.TestCase):
    def setUp(self):
        self.web3 = connect_to_blockchain()
        self.contract_path = "backend/blockchain/contracts/RescueID.sol"
        self.contract_address = deploy_contract(self.web3, self.contract_path)
        with open("backend/blockchain/contracts/RescueID.json", "r") as file:
            self.abi = json.load(file)["abi"]

    def test_add_victim_data(self):
        result = add_victim_data(self.web3, self.contract_address, self.abi, "John Doe", "1234567890", "Asthma", "Peanuts")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
