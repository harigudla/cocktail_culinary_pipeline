"""Tests for util.py module. """

import pytest
from etl.cocktail_dto import CocktailDTO
from etl.util import convert_dto_to_dict


# Arrange
@pytest.fixture(scope='function')
def input_data():
    return [
        CocktailDTO(1, 'Mojito', 'Cocktail Glass', 'Yes', 'Not Available', 'No Info')
        ,CocktailDTO(2, 'Mojito Classic', 'Cocktail Glass', 'Yes', 'Not Available', 'No Info')
    ]


def test_convert_dto_to_dict_for_empty_list():
    """Test for empty list input. """

    empty_list = []
    dict_list = convert_dto_to_dict(empty_list)
    assert not dict_list


def test_convert_dto_to_dict(input_data):
    """Test to convert dto objects to dict objects. 
    
    Args:
        input_data (fixture): Pytest fixture for DTO objects.
    
    """

    dict_list = convert_dto_to_dict(input_data)
    for object in dict_list:
        assert isinstance(object, dict)