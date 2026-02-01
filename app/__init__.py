from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class=None):
    app = Flask(__name__)
    
    # 設定の読み込み
    if config_class:
        app.config.from_object(config_class)
    else:
        # デフォルト設定
        app.config['SECRET_KEY'] = 'dev-secret-key'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
    #拡張機能の初期化
    db.init_app(app)
    jwt.init_app(app)

    #Blueprintの登録
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    # アプリケーションコンテキスト内でのデータベース初期化
    with app.app_context():
        db.create_all()
    
    return app