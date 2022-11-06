from aiohttp.test_utils import TestClient

async def test_ping_handler(client: TestClient):
    response = await client.get('/ping')
    assert response.status == 200
