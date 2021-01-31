from env.infra import app
from env.logger import logger

if __name__ == '__main__':
    try:
        app.run(port=app.config['PORT'])
    except Exception as e:
        logger.error(e)
