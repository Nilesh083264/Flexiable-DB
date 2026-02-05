"""
File: tests/api/test_backup_api_negative.py
Responsibility:
- Validate client-side error handling for Backup APIs
- Ensure invalid or missing inputs are rejected cleanly
"""

# -----------------------
# Trigger Backup API
# -----------------------

def test_trigger_backup_missing_db_type(client):
    """
    Missing db_type should return validation error (422)
    """
    response = client.post("/api/backup/start")

    assert response.status_code == 422


def test_trigger_backup_invalid_db_type(client):
    """
    Invalid db_type should be rejected by FastAPI validation (422)
    """
    response = client.post(
        "/api/backup/start",
        params={"db_type": "mysql"},
    )

    assert response.status_code == 422


# -----------------------
# List Backups API
# -----------------------

def test_list_backups_missing_db_type(client):
    """
    Missing db_type should return validation error (422)
    """
    response = client.get("/api/backup/list")

    assert response.status_code == 422


def test_list_backups_invalid_db_type(client):
    """
    Invalid db_type should be rejected by FastAPI validation (422)
    """
    response = client.get(
        "/api/backup/list",
        params={"db_type": "oracle"},
    )

    assert response.status_code == 422
