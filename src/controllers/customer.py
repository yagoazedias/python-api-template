import os
from config import ns
from flask_restplus import Resource

from loguru import logger


@logger.catch
@ns.route('/customer')
class Customer(Resource):

    def post(self):
        logger.debug(dict(os.environ))
        return {"status": "doing"}
