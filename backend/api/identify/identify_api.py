from flask import Blueprint, request, jsonify
from backend.api.facial_recognition import recognize_face
from backend.api.blockchain_integration import connect_to_blockchain, deploy_contract, add_victim_data
from backend.database.models import User, HealthRecord
from backend.database.db_config import get_postgresql_engine, get_mongodb_client
import json

# Create a Blueprint for the identify API
identify_api = Blueprint('identify_api', __name__)

# Initialize database connections
postgresql_engine = get_postgresql_engine()
mongodb_client = get_mongodb_client()

# Connect to blockchain
web3 = connect_to_blockchain()
contract_path = "backend/blockchain/contracts/RescueID.sol"
contract_address = deploy_contract(web3, contract_path)

# Load ABI from compiled contract
with open("backend/blockchain/contracts/RescueID.json", "r") as file:
    abi = json.load(file)["abi"]

@identify_api.route('/identify', methods=['POST'])
def identify_user():
    data = request.json
    image_path = data.get('image_path')

    # Step 1: Recognize face
    face_result = recognize_face(image_path)
    if face_result["status"] != "success":
        return jsonify(face_result), 400

    # Step 2: Query database
    thai_id = data.get('thai_id')
    query = f"SELECT * FROM users WHERE thai_id = '{thai_id}'"
    user_data = postgresql_engine.execute(query).fetchone()

    if not user_data:
        return jsonify({"status": "error", "message": "User not found in database"}), 404

    # Step 3: Query health records from MongoDB
    health_records = mongodb_client.health_records.find_one({"user_id": user_data["user_id"]})

    # Step 4: Store data on Blockchain
    result = add_victim_data(
        web3,
        contract_address,
        abi,
        user_data["name"],
        user_data["thai_id"],
        health_records["medical_history"],
        health_records["allergies"]
    )

    return jsonify({
        "status": "success",
        "face_result": face_result,
        "user_data": dict(user_data),
        "health_records": health_records,
        "blockchain_result": result
    })
