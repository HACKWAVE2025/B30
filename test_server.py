
"""
Simple script to test the Flask server with the same data your ESP8266 sends
"""
import requests
import json


test_data = {
    "temp": 27.20,
    "humidity": 58.00,
    "soil_moisture": 0.00,
    "distance": -1.00,
    "soil_type": "Sandy"
}

print("🧪 Testing Flask server locally...")
print(f"📤 Sending data: {json.dumps(test_data, indent=2)}")

try:
    # Test the server
    response = requests.post(
        "http://localhost:5000/data",
        json=test_data,
        timeout=5
    )
    
    print(f"🌐 Response Code: {response.status_code}")
    print(f"📥 Response Content: {response.text}")
    
    if response.status_code == 200:
        print("✅ SUCCESS! Server is working correctly")
        try:
            json_response = response.json()
            print(f"📊 Analysis: {json_response.get('analysis', 'No analysis')}")
        except:
            print("Response is not JSON format")
    else:
        print("❌ ERROR! Server returned error status")
        
except requests.exceptions.ConnectionError:
    print("❌ ERROR! Cannot connect to server. Is it running on localhost:5000?")
except Exception as e:
    print(f"❌ ERROR! {e}")

print("\n" + "="*50)
print("🔍 Next steps:")
print("1. If this test works, your ESP8266 should work too")
print("2. If this fails, check the Flask server terminal for error messages")
print("3. Make sure Flask is running on http://localhost:5000")