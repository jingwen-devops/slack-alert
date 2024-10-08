from crypt import methods

from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route('/get_alert_json',methods=['POST'])
def get_alert_json():
    data = request.json
    print(data)


if __name__ == '__main__':
    app.run()
