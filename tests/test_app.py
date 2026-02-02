import pytest
from app import create_app
from app.config import TestingConfig

@pytest.fixture
def app():
    # テスト用アプリケーションインスタンス
    app = create_app(TestingConfig)
    return app

@pytest.fixture
def client(app):
    # テストクライアント
    return app.test_client()

def test_home_page(client):
    # ホームページのテスト
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_api_endpoint(client):
    # APIエンドポイントのテスト
    response = client.get('/api/items')
    assert response.status_code == 200
    assert response.is_json