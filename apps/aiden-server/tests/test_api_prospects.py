import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_prospect(client: AsyncClient):
    response = await client.post(
        "/api/v1/prospects/",
        json={
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "linkedin_url": "https://linkedin.com/in/testuser",
            "company_name": "TestCorp"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

@pytest.mark.asyncio
async def test_read_prospects(client: AsyncClient):
    response = await client.get("/api/v1/prospects/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.asyncio
async def test_trigger_research_nonexistent(client: AsyncClient):
    response = await client.post("/api/v1/prospects/99999/research")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_trigger_research_valid(client: AsyncClient):
    # Create one to be sure
    await client.post(
        "/api/v1/prospects/",
        json={
            "email": "test2@example.com",
            "first_name": "Test2",
            "last_name": "User2",
            "linkedin_url": "https://linkedin.com/in/testuser2",
            "company_name": "TestCorp2"
        },
    )
    # Get its ID
    prospects_response = await client.get("/api/v1/prospects/")
    prospects = prospects_response.json()
    p_id = prospects[-1]["id"]

    response = await client.post(f"/api/v1/prospects/{p_id}/research")
    assert response.status_code == 200
    assert "task_id" in response.json()
