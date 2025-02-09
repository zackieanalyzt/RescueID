from flask import Flask
from backend.api import api_blueprint
from backend.database.db_config import get_postgresql_engine, get_mongodb_client
from backend.api.blockchain_integration import connect_to_blockchain, deploy_contract
import os

# Initialize Flask Application
app = Flask(__name__)

# Initialize Database Connections
postgresql_engine = get_postgresql_engine()
mongodb_client = get_mongodb_client()

# Connect to Blockchain Network
web3 = connect_to_blockchain()
contract_path = os.path.join(os.getcwd(), "backend", "blockchain", "contracts", "RescueID.sol")
contract_address = deploy_contract(web3, contract_path)

# Register API Blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')

# Home Route (Welcome Message)
@app.route('/')
def home():
    return "Welcome to RescueID - A system for identifying accident victims using Facial Recognition, Blockchain, and Government Databases."

if __name__ == '__main__':
    # Run the application on the specified host and port
    app.run(host='0.0.0.0', port=5000, debug=True)
