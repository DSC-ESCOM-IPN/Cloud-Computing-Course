import os
import json
import datetime
import decimal
from apis import api
from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix


class JSONEncoder(json.JSONEncoder):
    def default(self, o):  # pylint: disable=E0202
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, (datetime.datetime, datetime.date)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
cors = CORS(app)
api.init_app(app)

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
#app.json_encoder = JSONEncoder
app.config["RESTPLUS_JSON"] = {"cls": JSONEncoder}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000),
            debug=os.getenv('FLASK_DEBUG', 0))
