"""
File: app/domain/interfaces/connection_interface.py
Responsibility: Contract for database connection validation
"""

from abc import ABC, abstractmethod


class ConnectionInterface(ABC):

    @abstractmethod
    def check_connection(self) -> bool:
        pass
