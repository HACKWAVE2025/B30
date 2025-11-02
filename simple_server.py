from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    print("📡 Received request!")
    try:
        data = request.get_json(force=True)
        print(f"📥 Data: {data}")
        
        response = {
            "status": "success",
            "message": "Data received!",
            "received": data
        }
        print(f"✅ Sending response: {response}")
        return jsonify(response)
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return "AquaSense Server Running! 🌱"

if __name__ == '__main__':
    print("🚀 Starting simple test server...")
    app.run(host='0.0.0.0', port=5000)