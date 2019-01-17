from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def respond_root():
    return 'Hello im working.'

@app.route('/files/<path:path>')
def send_js(path):
    return send_from_directory(static_file_dir, path)

if __name__ == '__main__':
    #schedule.every(5).seconds.do(job)
    #Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
