"""Tests for db.py module."""

import os
import sqlite3
import tempfile
import pytest
from etl.db import SQLite3Connection


# Arrange
@pytest.fixture(scope="module")
def db_file():
    """Create database file.

    Returns:
        str: database file name.

    """
    tmp_dir = tempfile.mkdtemp()
    db_filename = os.path.join(tmp_dir, "test.db")
    return db_filename


# Arrange
@pytest.fixture(scope="module")
def db_connection(db_file):
    """Create & return SQLite3Connection class instance.

    Args:
        db_file (str): Database file name.

    Returns:
        obj: Return SQLite3Connection instance.

    """
    sqlite_connection = SQLite3Connection(db_file)
    return sqlite_connection


# Arrange
@pytest.fixture
def input_data():
    """Prepare input data.

    Returns:
        list: Dictionary objects.

    """
    return [
        {
            "cocktail_id": "1",
            "cocktail_name": "Margarita",
            "glass_type": "Cocktail glass",
            "is_alcoholic": "Yes",
            "preparation_notes_en": "",
            "ingredients": "",
        },
        {
            "cocktail_id": "2",
            "cocktail_name": "WhiteCap Margarita",
            "glass_type": "Cocktail glass",
            "is_alcoholic": "Yes",
            "preparation_notes_en": "",
            "ingredients": "",
        },
    ]


def test_sqliteconnection_init(db_connection):
    """The test performs database initializing.

    Args:
        db_connection (obj): SQLite3Connection class instance.

    """
    assert db_connection is not None


def test_create_tables(db_file):
    """Test create tables.

    Args:
        db_file (str): Database file name.

    """
    _connection = sqlite3.connect(db_file)
    _cursor = _connection.execute(
        "select count(*) from sqlite_master where type='table'"
    )
    (tables_count,) = _cursor.fetchone()
    _cursor.close()
    _connection.close()
    _connection = None
    assert tables_count >= 1


def test_load_data(db_connection, input_data, db_file):
    """Test load data into tables.

    Args:
        db_connection (obj): SQLite3Connection class instance.
        input_data (list): Dictionary objects.
        db_file (str): Database filename.

    """
    # load data
    db_connection.load_data(input_data)

    _connection = sqlite3.connect(db_file)
    _cursor = _connection.execute("select count(*) from cocktails_menu")
    (rows_count,) = _cursor.fetchone()
    _cursor.close()
    _connection.close()
    _connection = None
    assert rows_count >= 1
