from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def serve():
    # Stress the CPU to the specified usage
    if request.method == 'POST':
        # Create a subprocess to run the stress_cpu.py script
        subprocess.Popen(["python3", "stress_cpu.py"])
        return 'stated'

    elif request.method == 'GET':
        return socket.gethostbyname()

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 (accessible from outside) and port 5000
    app.run(host='0.0.0.0', port=5000)
