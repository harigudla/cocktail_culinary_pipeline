"""Test for file_utils.py module."""

import pytest
import os
import csv

from etl.cocktail_dto import CocktailDTO
from etl.file_utils import write_to_csv_file


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
def csv_file(tmpdir):
    """Fixture to return filename path.

    Args:
        tmpdir (obj): Pytest fixture for temporary directory.

    Returns:
        str: Filename path.

    """
    csv_file = os.path.join(tmpdir, "final_menu.csv")
    return csv_file


def test_write_to_csv_file(csv_file, dtos):
    """Test write to csv file method.

    Args:
        csv_file (str): Filename path.
        dtos (list): List of DTO objects.

    """
    # Act
    write_to_csv_file(csv_file, dtos)

    # Assert if file exists.
    assert os.path.isfile(csv_file)

    # Assert file contents
    with open(csv_file, "r") as csv_file_read:
        reader = csv.reader(csv_file_read)
        rows = list(reader)
        assert rows == [
            ["11007", "Margarita", "Cocktail glass", "Yes", "", ""],
            ["12322", "Strawberry Margarita", "Cocktail glass", "Yes", "", ""],
        ]
