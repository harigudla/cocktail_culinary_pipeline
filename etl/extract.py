"""Module to extract data."""

import requests
import json

from etl_exceptions import EtlExecutionException
from cocktail_dto import CocktailDTO


def read_cocktail_menu(filename_path):
    """Read cocktail menu json data from file.

    Ensure cocktail menu file is located in folder ´input´.

    Args:
        filename_path (str): Filename path to read file contents.

    Raises:
        EtlExecutionException: Raises exception if file not found.

    Returns:
        str: json data.

    """
    try:
        json_data = None
        with open(filename_path) as json_file:
            json_data = json.load(json_file)
        return json_data
    except Exception as error:
        raise EtlExecutionException(error)


def get_cocktail_objects(json_list):
    """Convert json objects into dto objects.

    Args:
        json_list (list): Cocktail items.


    Returns:
        list: Cocktail dto objects list.

    """
    try:
        if not json_list:
            return
        dto_list = []
        for data_dict in json_list:
            cocktail_dto = CocktailDTO(None, data_dict["name"], None, None, None, None)
            dto_list.append(cocktail_dto)
        return dto_list
    except Exception:
        raise EtlExecutionException(f"Cannot write into dto objects.")


def process(filename_path):
    """Extracts source data and returns DTO objects.

    Args:
        filename_path (str): Filename path to read file contents.

    Returns:
        list: Cocktail DTO objects.

    """

    # extract cocktail menu
    data = read_cocktail_menu(filename_path)

    # store into dto objects
    dto_list = get_cocktail_objects(data)
    return dto_list
