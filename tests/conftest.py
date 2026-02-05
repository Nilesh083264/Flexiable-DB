"""
File: tests/conftest.py
Responsibility: Shared pytest fixtures for the test suite
"""

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture(scope="session")
def client():
    """
    Provides a TestClient instance for API tests
    """
    return TestClient(app)
