import config
from flask import Flask
from flask_cors import CORS as use_cors
from common import R

app = Flask(__name__)
app.app_context().push()

if __name__ == '__main__':
    use_cors(app, resources=r'/*')
    app.config.from_object(config)
    app.register_error_handler(Exception, lambda e: R.error(str(e)))
    from router.app_blueprint import bp as app_blueprint

    app.register_blueprint(app_blueprint)
    app.run(host='0.0.0.0', port=80, debug=True)
