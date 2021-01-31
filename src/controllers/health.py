from env.infra import ns, app
from flask_restplus import Resource

from loguru import logger


@logger.catch
@ns.route('/health')
class Health(Resource):

    def get(self):
        logger.debug(dict(app.config))
        return {"status": "ok"}
