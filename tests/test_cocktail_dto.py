"""Test for cocktail_dto.py module."""

from etl.cocktail_dto import CocktailDTO
import pytest


# Arrange
@pytest.fixture(scope="module")
def cocktail_dto():
    """Prepare & return CocktailDTO instance."""

    cocktail_dto = CocktailDTO(
        1, "Majito", "Cocktail Glass", "Yes", "", "Lime Juice:Soda"
    )
    return cocktail_dto


def test_cocktail_dto_instance_check(cocktail_dto):
    """Test for CocktailDTO class.

    Args:
        cocktail_dto: Pytest fixture for CocktailDTO instance.

    """
    assert isinstance(cocktail_dto, CocktailDTO)


def test_cocktail_dto_members_check(cocktail_dto):
    """Test for dto instances field values.

    Args:
        cocktail_dto: Pytest fixture for CocktailDTO instance.

    """
    assert cocktail_dto.cocktail_id == 1
    assert cocktail_dto.cocktail_name == "Majito"
    assert cocktail_dto.glass_type == "Cocktail Glass"
    assert cocktail_dto.is_alcoholic == "Yes"
    assert cocktail_dto.preparation_notes_en == ""
    assert cocktail_dto.ingredients == "Lime Juice:Soda"


def test_cocktail_dto_data_type_check(cocktail_dto):
    """Test for dto instances fields data type.

    Args:
        cocktail_dto: Pytest fixture for cocktail_dto instance.

    """
    assert isinstance(cocktail_dto.cocktail_id, int)
    assert isinstance(cocktail_dto.cocktail_name, str)
    assert isinstance(cocktail_dto.glass_type, str)
    assert isinstance(cocktail_dto.is_alcoholic, str)
    assert isinstance(cocktail_dto.preparation_notes_en, str)
    assert isinstance(cocktail_dto.ingredients, str)


def test_cocktail_dto_unknown_field(cocktail_dto):
    """Test with uknown field initialization.

    Args:
        cocktail_dto: Pytest fixture for cocktail_dto instance.

    """

    with pytest.raises(TypeError):
        CocktailDTO(cocktail_id=1, unknown_field="")


def test_cocktail_dto_mismatch_data_type(cocktail_dto):
    """Test for mismatch data type assignment.

    Args:
        cocktail_dto: Pytest fixture for cocktail_dto instance.

    """

    with pytest.raises(TypeError):
        CocktailDTO(cocktail_id="One")
