import requests

port = "http://localhost:8000/ascii"
test_json = {}
test_json["message"] = "Test Message"
test_json["sprite"] = False

# Test ASCII text generation
response = requests.post(port, json=test_json)
if ("error" in response.json()): 
    print("POST Response (Error): ", response.json())
else: 
    response_dict = response.json()
    print("POST Response:\n", response_dict["message"])



# Test ASCII sprite generation
test_json["sprite"] = True
response = requests.post(port, json=test_json)
if ("error" in response.json()): 
    print("POST Response (Error): ", response.json())
else: 
    response_dict = response.json()
    print("POST Response:\n", response_dict["message"])