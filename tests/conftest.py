# tests/conftest.py
import pytest
from authz.authz import create_app

@pytest.fixture(scope="session")
def app():
    """یک app مستقل برای کل جلسه‌ی تست می‌سازد."""
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    """یک test client برای هر تست فراهم می‌کند."""
    return app.test_client()

