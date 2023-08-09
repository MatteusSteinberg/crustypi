validation_rule = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["timestamp"],
        "properties": {
            "timestamp": {"bsonType": "string"},
            "humidity": {"bsonType": "number"},
            "temperature": {"bsonType": "number"},
            "pressure": {"bsontype": "number"}
        }
    }
}
