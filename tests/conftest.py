import pytest
from aiohttp.test_utils import TestClient, TestServer

from internal.__main__ import setup_app


@pytest.fixture
async def client() -> TestClient:
    app = setup_app()
    test_server = TestServer(app)
    test_client = TestClient(test_server)
    await test_client.start_server()
    try:
        yield test_client
    finally:
        await test_client.close()
