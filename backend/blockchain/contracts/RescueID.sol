// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RescueID {
    // Struct to store victim data
    struct VictimData {
        uint256 userId; // Unique ID for each victim
        string name; // Name of the victim
        string thaiId; // Thai National ID
        string medicalHistory; // Medical history (e.g., conditions, surgeries)
        string allergies; // Allergies (e.g., food, medicine)
        string emergencyContact; // Emergency contact information
        bool isRegistered; // Flag to check if the user is registered
    }

    // Mapping to store victim data by user ID
    mapping(uint256 => VictimData) public victims;
    uint256 public victimCount; // Counter for unique user IDs

    // Event to log when a new victim is added
    event VictimAdded(uint256 indexed userId, string name, string thaiId);

    // Event to log when victim data is updated
    event VictimUpdated(uint256 indexed userId, string name, string thaiId);

    // Modifier to ensure only registered users can access certain functions
    modifier onlyRegistered(uint256 _userId) {
        require(victims[_userId].isRegistered, "User is not registered.");
        _;
    }

    // Add new victim data to the blockchain
    function addVictim(
        string memory _name,
        string memory _thaiId,
        string memory _medicalHistory,
        string memory _allergies,
        string memory _emergencyContact
    ) public {
        victimCount++; // Increment the victim counter
        victims[victimCount] = VictimData({
            userId: victimCount,
            name: _name,
            thaiId: _thaiId,
            medicalHistory: _medicalHistory,
            allergies: _allergies,
            emergencyContact: _emergencyContact,
            isRegistered: true
        });

        // Emit an event to log the addition
        emit VictimAdded(victimCount, _name, _thaiId);
    }

    // Update existing victim data
    function updateVictim(
        uint256 _userId,
        string memory _name,
        string memory _thaiId,
        string memory _medicalHistory,
        string memory _allergies,
        string memory _emergencyContact
    ) public onlyRegistered(_userId) {
        victims[_userId].name = _name;
        victims[_userId].thaiId = _thaiId;
        victims[_userId].medicalHistory = _medicalHistory;
        victims[_userId].allergies = _allergies;
        victims[_userId].emergencyContact = _emergencyContact;

        // Emit an event to log the update
        emit VictimUpdated(_userId, _name, _thaiId);
    }

    // Get victim data by user ID
    function getVictim(uint256 _userId)
        public
        view
        onlyRegistered(_userId)
        returns (
            string memory,
            string memory,
            string memory,
            string memory,
            string memory
        )
    {
        VictimData memory victim = victims[_userId];
        return (
            victim.name,
            victim.thaiId,
            victim.medicalHistory,
            victim.allergies,
            victim.emergencyContact
        );
    }

    // Check if a user is registered
    function isUserRegistered(uint256 _userId) public view returns (bool) {
        return victims[_userId].isRegistered;
    }
}
