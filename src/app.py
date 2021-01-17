from config.infra import app
from controllers.health import Health

# Using for live reload
# https://stackoverflow.com/a/56974220/6516044
if __name__ == '__main__':
    app.run(port=app.config['PORT'])
