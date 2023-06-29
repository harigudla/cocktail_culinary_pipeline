"""Test for transform.py module."""

import pytest
import requests

from etl.cocktaildb_api import CocktailDBAPI
from etl.cocktail_dto import CocktailDTO
from etl.transform import enrich_menu, enrich_cocktail


# Arrange
@pytest.fixture
def cocktaildb_api():
    """Initialize and return CocktailDBAPI class instance."""

    cocktaildb_api = CocktailDBAPI()
    return cocktaildb_api


# Arrange
@pytest.fixture
def dtos():
    """Create and return CocktailDTO objects.

    Returns:
         list: List of dto objects.
    """
    dtos = [
        CocktailDTO(None, "Margarita", None, None, None, None),
        CocktailDTO(None, "Strawberry Margarita", None, None, None, None),
    ]
    return dtos


# Arrange
@pytest.fixture
def json_data():
    """Create and return json data.

    Returns:
        str: json formatted string.
    """

    data = {
        "drinks": [
            {
                "idDrink": "11007",
                "strDrink": "Margarita",
                "strAlcoholic": "Alcoholic",
                "strGlass": "Cocktail glass",
                "strInstructions": "Rub the rim of the glass with the lime slice to make the salt stick to it. Take care to moisten only the outer rim and sprinkle the salt on it. The salt should present to the lips of the imbiber and never mix into the cocktail. Shake the other ingredients with ice, then carefully pour into the glass.",
            },
            {
                "idDrink": "12322",
                "strDrink": "Strawberry Margarita",
                "strAlcoholic": "Alcoholic",
                "strGlass": "Cocktail glass",
                "strInstructions": "Rub rim of cocktail glass with lemon juice and dip rim in salt. Shake schnapps, tequila, triple sec, lemon juice, and strawberries with ice, strain into the salt-rimmed glass, and serve.",
            },
        ]
    }
    return data


def test_enrich_menu_success(dtos):
    """Test enrich menu items.

    Args:
        dtos (list): List of CocktailDTO objects.

    """
    # Act
    transformed_data = enrich_menu(dtos)

    # Assert
    assert transformed_data
    assert len(transformed_data) == 2

    for cocktail_dto in transformed_data:
        assert cocktail_dto.cocktail_id in (11007, 12322)
        assert cocktail_dto.cocktail_name in ("Margarita", "Strawberry Margarita")
        assert cocktail_dto.is_alcoholic == "Yes"


def test_enrich_menu_failure_unknown_name():
    """Test enrich menu for name not found by api."""

    # Arrange
    dtos = [CocktailDTO(None, "Unknown", None, None, None, None)]

    # Act
    transformed_data = enrich_menu(dtos)

    # Assert
    assert transformed_data
    assert len(transformed_data) == 1

    cocktail_dto = transformed_data[0]
    assert cocktail_dto.cocktail_id is None
    assert cocktail_dto.is_alcoholic is None


def test_enrich_menu_api_error(mocker):
    """Test enrich menu for api error.

    Args:
        mocker (obj): Fixture for mocking methods.

    """
    # Arrange
    mocker.patch("etl.cocktaildb_api.requests.get")
    requests.get.return_value.status_code = 404

    end_point = "search.php"
    params = {"s": "margarita"}

    # Assert
    with pytest.raises(Exception):
        cocktaildb_api.get_cocktail_by_name(end_point, params)

    # Arrange
    dtos = [CocktailDTO(None, "Cosmopolitan", None, None, None, None)]

    # Assert
    with pytest.raises(Exception):
        enrich_menu(dtos)


def test_enrich_cocktail_success(json_data, dtos):
    """Test enrich cocktail method.

    Args:
        json_data (dict): json formatted string in dictionary object.
        dtos (list): List of CocktailDTO objects.

    """
    # Arrange
    dto = dtos[0]

    # Act
    transformed_dto = enrich_cocktail(dto, json_data)

    # Assert
    assert transformed_dto
    assert transformed_dto.cocktail_id == dto.cocktail_id
    assert transformed_dto.cocktail_name == dto.cocktail_name


def test_enrich_cocktail_failure(json_data):
    """Test enrich cocktail method for unknown drink name.

    Args:
        json_data (dict): json formatted string in dictionary object.

    """
    # Arrange
    dto = CocktailDTO(
        cocktail_id=None,
        cocktail_name="Cosmopolitan",
        glass_type=None,
        is_alcoholic=None,
        preparation_notes_en=None,
        ingredients=None,
    )

    # Act
    transformed_dto = enrich_cocktail(dto, json_data)

    # Assert
    assert transformed_dto
    assert transformed_dto.cocktail_id is None


def test_process(dtos):
    """Test transformation process.

    Args:
        dtos (list): List of CocktailDTO objects.

    """

    # Act
    transformed_data = enrich_menu(dtos)

    # Assert
    assert transformed_data
    assert len(transformed_data) == 2

    for dto in transformed_data:
        assert dto.cocktail_id is not None
        assert dto.cocktail_name is not None
