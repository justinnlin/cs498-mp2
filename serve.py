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
        hostname = socket.gethostname()
        return f"push EC2 instance {socket.gethostbyname(hostname)} to maximum CPU utilization"

    elif request.method == 'GET':
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 (accessible from outside) and port 5000
    app.run(debug=True,host='0.0.0.0', port=5000)
