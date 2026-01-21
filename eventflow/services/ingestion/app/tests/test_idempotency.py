def test_idempotent_ingest(client):
    payload = {
        "event_id": "550e8400-e29b-41d4-a716-446655440000",
        "timestamp": "2025-01-01T00:00:00Z",
        "payload": {"user_id": 123}
    }

    r1 = client.post("/v1/events/user_signup", json=payload)
    r2 = client.post("/v1/events/user_signup", json=payload)

    assert r1.json()["status"] == "accepted"
    assert r2.json()["status"] == "duplicate"