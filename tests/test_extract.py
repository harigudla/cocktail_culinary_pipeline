"""Tests for extract.py module. """

import pytest
from pytest_mock import mocker
import os

from etl.extract import read_cocktail_menu, get_cocktail_objects, process
from etl.etl_exceptions import EtlExecutionException
from etl.cocktail_dto import CocktailDTO


# Arrange
@pytest.fixture(scope="module")
def json_data():
    """Prepare sample json input data."""

    return [
        {
            "ingredients": ["Vodka", "Cointreau", "Cranberry juice"],
            "name": "Cosmopolitan",
        },
        {"ingredients": ["Lime juice", "White rum", "Soda"], "name": "Mojito"},
    ]


# Arrange
@pytest.fixture(scope="module")
def expected_dto_list():
    """Prepare and return CocktailDTO objects list."""

    dto_list = [
        CocktailDTO(
            None, "Cosmopolitan", None, None, None, "Vodka:Cointreau:Cranberry juice"
        ),
        CocktailDTO(None, "Mojito", None, None, None, "Lime juice:White rum:Soda"),
    ]
    sorted_list = dto_list.sort()
    return sorted_list


# Arrange
@pytest.fixture(scope="function")
def json_invalid_data():
    """Prepare sample json input invalid data."""

    return ["one", "two"]


# Arrange
@pytest.fixture()
def json_file():
    """Return json input file path.

    Returns:
        str: Filename path.

    """
    filename_path = os.path.join("input", "cocktail_menu.json")
    return filename_path


def test_read_cocktail_menu(json_file):
    """Test to read cocktail menu items from url.

    Args:
        json_file (str): json filename path.

    """
    cocktail_menu = read_cocktail_menu(json_file)
    assert cocktail_menu is not None
    assert cocktail_menu


def test_get_cocktail_objects(json_data, expected_dto_list):
    """Test to get CocktailDTO list from json input data.

    Args:
        json_data (list): List of dictionary objects.
        expected_dto_list (list): List of CocktailDTO objects.

    """

    cocktail_dto_list = get_cocktail_objects(json_data)
    assert cocktail_dto_list is not None
    assert cocktail_dto_list
    assert len(cocktail_dto_list) == 2

    # Compare objects in list.
    sorted_cocktail_dto_list = cocktail_dto_list.sort()
    assert sorted_cocktail_dto_list == expected_dto_list


def test_get_cocktail_objects_for_no_data():
    """Test to get CocktailDTO list from json input data."""

    cocktail_dto_list = get_cocktail_objects(None)
    assert cocktail_dto_list is None


def test_get_cocktail_objects_for_wrong_data(json_invalid_data):
    """Test to get CocktailDTO list from json input data."""

    with pytest.raises(Exception):
        get_cocktail_objects(json_invalid_data)


def test_process(json_file):
    """Test extraction process.

    Args:
        json_file (str): json filename path.

    """

    dto_list = process(json_file)
    assert dto_list is not None
    assert dto_list


def test_process_with_mock(json_data, expected_dto_list, mocker, json_file):
    """Test extraction process with mock objects.

    Args:
        json_data (list): JSON array.
        expected_dto_list (list): List of CocktailDTO objects.
        mocker (Obj): Fixture for mocking objects.
        json_file (str): json filename path.

    """

    # Arrange
    mocker_read_cocktail_menu = mocker.patch(
        "etl.extract.read_cocktail_menu", return_value=json_data
    )
    mocker_get_cocktail_objects = mocker.patch(
        "etl.extract.get_cocktail_objects", return_value=expected_dto_list
    )

    # Act
    result = process(json_file)

    # Assert
    assert result == expected_dto_list
    mocker_read_cocktail_menu.assert_called_once()
    mocker_get_cocktail_objects.assert_called_once()
