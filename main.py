from flask import Flask
import os

app = Flask(__name__)

port = int(os.getenv("PORT", 9099))

@app.route('/v1/demo')
def demo():
   return 'Hello World! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0))


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
