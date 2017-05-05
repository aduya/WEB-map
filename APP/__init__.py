from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)

app.config.from_object('config')
#创建数据库对象
db = SQLAlchemy(app)

#创建登录对象
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'


from APP import views
from .api import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api')