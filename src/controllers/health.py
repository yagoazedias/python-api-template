import os
from config.infra import ns
from flask_restplus import Resource

from loguru import logger


@logger.catch
@ns.route('/health')
class Health(Resource):

    def get(self):
        logger.debug(dict(os.environ))
        return {"status": "ok"}
