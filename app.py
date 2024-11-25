from flask import Flask, jsonify
  from website import create_app
app = Flask(__name__)

@app.route('/troubleshoot', methods=['GET'])
def troubleshoot():
    try:
        # Simulate some processing
        large_array = [i for i in range(1_000_000)]  # Adjust as necessary
        return jsonify({"message": "Troubleshooting function executed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


  

app = create_app()
application = app

# Remove debug mode for production
if __name__ == '__main__':
    app.run()