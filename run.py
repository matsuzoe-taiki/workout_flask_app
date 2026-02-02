import os
from app import create_app
from app.config import config

# 環境変数から設定を取得（デフォルトはdevelopment）
config_name = os.environ.get('FLASK_ENV') or 'development'

app = create_app(config[config_name])

if __name__ == '__main__':
    app.run()