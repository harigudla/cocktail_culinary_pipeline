"""Tests for cocktaildb_api.py module. """

from etl.cocktaildb_api import CocktailDBAPI
import pytest
import requests


# Arrange
@pytest.fixture
def cocktaildb_api():
    """Initialize and return CocktailDBAPI class instance."""

    cocktaildb_api = CocktailDBAPI()
    return cocktaildb_api


# Arrange
@pytest.fixture
def output_data():
    """Prepare and return output data."""

    return {
        "drinks": [
            {
                "idDrink": "17196",
                "strDrink": "Cosmopolitan",
                "strDrinkAlternate": "",
                "strTags": "IBA,ContemporaryClassic",
            },
            {
                "idDrink": "14133",
                "strDrink": "Cosmopolitan Martini",
                "strDrinkAlternate": "",
                "strTags": "",
            },
        ]
    }


def test_cocktail_api_initialization(cocktaildb_api):
    """Test cocktaildb_api instance initialization.

    Args:
        cocktaildb_api (obj): Pytest fixture for cocktail api instance.

    """
    assert cocktaildb_api is not None


def test_cocktail_api_init_error():
    """Test cocktail api initialization error."""

    with pytest.raises(TypeError):
        CocktailDBAPI(invalid_param="https://www.thecocktaildb.com/api/json/v1/1/")


def test_cocktail_api_end_point(cocktaildb_api):
    """Test cocktaildb_api end point.

    Args:
        cocktaildb_api (obj): Pytest fixture for cocktail api instance.

    """

    end_point = "search.php"
    params = {"s": "margarita"}
    data = cocktaildb_api.get_cocktail_by_name(end_point, params)
    assert data is not None
    assert data


def test_cocktail_api_end_point_error(cocktaildb_api):
    """Test cocktaildb_api end point.

    Args:
        cocktaildb_api (obj): Pytest fixture for cocktail api instance.

    """

    end_point = "unknown.php"
    params = {"s": "margarita"}
    with pytest.raises(Exception):
        cocktaildb_api.get_cocktail_by_name(end_point, params)


def test_get_cocktail_by_name_status_code_failure(mocker, cocktaildb_api):
    """Mock the requests library to return a failure status code.

    Args:
        mocker (obj): Fixture for mocking methods.
        cocktaildb_api (obj): Pytest fixture for cocktail api instance.

    """

    # Arrange
    mocker.patch("etl.cocktaildb_api.requests.get")
    requests.get.return_value.status_code = 404

    end_point = "search.php"
    params = {"s": "margarita"}

    with pytest.raises(Exception):
        cocktaildb_api.get_cocktail_by_name(end_point, params)


def test_get_cocktail_by_name(mocker, cocktaildb_api, output_data):
    """Mock the cocktaildb api to return expected result.

    Args:
        mocker (obj): Fixture for mocking methods.
        cocktaildb_api (obj): Pytest fixture for cocktail api instance.
        output_data (str): json string.
    """

    # Arrange
    mocker_get_cocktail_by_name = mocker.patch(
        "etl.cocktaildb_api.CocktailDBAPI.get_cocktail_by_name",
        return_value=output_data,
    )

    expected_result = {
        "drinks": [
            {
                "idDrink": "17196",
                "strDrink": "Cosmopolitan",
                "strDrinkAlternate": "",
                "strTags": "IBA,ContemporaryClassic",
            },
            {
                "idDrink": "14133",
                "strDrink": "Cosmopolitan Martini",
                "strDrinkAlternate": "",
                "strTags": "",
            },
        ]
    }

    # Act
    end_point = "search.php"
    params = {"s": "margarita"}
    result = cocktaildb_api.get_cocktail_by_name(end_point, params)

    # Assert
    assert result == expected_result
    mocker_get_cocktail_by_name.assert_called_once()
