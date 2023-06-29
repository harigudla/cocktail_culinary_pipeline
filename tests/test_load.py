"""Test load.py module."""

import pytest

from etl.load import process
from etl.cocktail_dto import CocktailDTO
from etl.db import SQLite3Connection


# Arrange
@pytest.fixture
def dtos():
    """Create and return CocktailDTO objects.

    Returns:
         list: List of dto objects.
    """
    dtos = [
        CocktailDTO(11007, "Margarita", "Cocktail glass", "Yes", None, None),
        CocktailDTO(12322, "Strawberry Margarita", "Cocktail glass", "Yes", None, None),
    ]
    return dtos


# Arrange
@pytest.fixture
def sqlite_conn():
    """Create and return in-memory sqlite3 connection.

    Returns:
        obj: Instance of SQLite3Connection.

    """
    sqlite_conn = SQLite3Connection()
    return sqlite_conn


def test_process_success(dtos, sqlite_conn):
    """Test loading process.


    Args:
        dtos (list): List of CocktailDTO objects.
        sqlite_conn (obj): Instance of SQLite3Connection class.

    """

    # Act
    process(dtos, sqlite_conn)
    results = sqlite_conn.get_data()

    # Assert
    assert results is not None


def test_process_exception(dtos):
    """Test loading process for exception.


    Args:
        dtos (list): List of CocktailDTO objects.

    """

    # Assert
    with pytest.raises(Exception):
        process(dtos, None)
