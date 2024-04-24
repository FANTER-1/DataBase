from flask import json

class SubmitDataSerializer:
    @staticmethod
    def serialize(data):
        return json.dumps(data)

    @staticmethod
    def deserialize(json_data):
        return json.loads(json_data)
