import json
api_response = '''
{
    "req_id": "req_012", 
    "status": "success",
    "result": {
        "text": "Hello world", 
        "confidence": 0.85
    }
 }
  '''
        
parsed_response = json.loads(api_response)
print(parsed_response)
print(f"Request ID: {parsed_response["req_id"]}")
print(f"Status: {parsed_response["status"]}")
print(f"Text: {parsed_response["result"]["text"]}")
print(f"Confidence: {parsed_response["result"]["confidence"]}")

if parsed_response["result"] ["confidence"] < 0.9:
    print("Warning: confidence is low")

follow_up = {
    "req_id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.95,
    }
}

with open("response.json", "w") as f:
    f.write(json.dumps(follow_up))