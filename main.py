import config
from flask import Flask
from flask_cors import CORS as use_cors

from im import socket
from common import R

# 实例化app
app = Flask(__name__)
# app入栈
app.app_context().push()
# 接口跨域
use_cors(app, resources=r'/*')
# 配置
app.config.from_object(config)
# 初始化socket-io
socket.init_app(app, async_mode="threading", cors_allowed_origins='*')
# 全局异常捕获
app.register_error_handler(Exception, lambda e: R.error(str(e)))

# 注册接口路由
from router.app_blueprint import bp as app_blueprint

app.register_blueprint(app_blueprint)

if __name__ == '__main__':
    socket.run(app, host='0.0.0.0', port=80, debug=True)
