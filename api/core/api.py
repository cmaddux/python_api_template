import json
import time
import logging

from flask import Flask, request, g
from flask_restful import Resource, Api

handler = logging.FileHandler(filename='api.log')
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

app = Flask('__name__')

for logger in (app.logger, logging.getLogger('api')):
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

api = Api(app)

@app.teardown_request
def teardown_request(exception=None):
    diff = time.time() - g.start
    app.logger.info('Request took %.2fs', diff)

class Hello(Resource):
    def get(self):
        g.start = time.time()
        return '{ title: "hello" }'

api.add_resource(Hello, '/')

if __name__ == '__main__':
    app.run(debug=True)
