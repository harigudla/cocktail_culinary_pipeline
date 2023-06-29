"""Module to transform/enrich data."""

from cocktaildb_api import CocktailDBAPI
from etl_exceptions import EtlExecutionException


def enrich_menu(dtos):
    """Enrich cocktail menu items with additional information.

    Args:
        dtos (list): CocktailDTO objects.

    Returns:
        list: Enriched DTO objects with additional information.

    """
    transformed_data = []
    try:
        # initialize api
        cocktailDBAPI = CocktailDBAPI()
        endpoint = "search.php"

        for cocktail_dto in dtos:
            # call the api
            params = {"s": cocktail_dto.cocktail_name}
            cocktail_info = cocktailDBAPI.get_cocktail_by_name(endpoint, params)

            # enrich cocktail object.
            cocktail_dto = enrich_cocktail(cocktail_dto, cocktail_info)
            transformed_data.append(cocktail_dto)
    except Exception as error:
        raise EtlExecutionException(error)

    return transformed_data


def enrich_cocktail(cocktail_dto, cocktail_info):
    """Enrich cockinfo with additional information.

    Args:
        cocktail_dto (CocktailDTO): Cocktail DTO Object.
        cocktail_info (dict): Drinks with similar name.

    Returns:
        CocktailDTO: Enriched object with additional information.

    """

    drinks = cocktail_info["drinks"]
    if not drinks:
        return cocktail_dto
    name = cocktail_dto.cocktail_name
    for drink in drinks:
        if drink.get("strDrink") == name:
            cocktail_dto.cocktail_id = int(drink["idDrink"])
            cocktail_dto.is_alcoholic = (
                "Yes" if drink["strAlcoholic"] == "Alcoholic" else "No"
            )
            cocktail_dto.glass_type = drink["strGlass"]
            cocktail_dto.preparation_notes_en = drink["strInstructions"]

            # convert ingredients to string sep by ':'
            ingredeints_list = [
                value
                for key, value in drink.items()
                if key.startswith("strIngredient") and value is not None
            ]
            cocktail_dto.ingredients = ":".join(ingredeints_list)
            return cocktail_dto
    return cocktail_dto


def process(data):
    """Transform the source data.

    Args:
        data (list): Cocktail DTO Objects.

    Returns:
        list: Enriched CocktailDTO objects.

    """

    transformed_data = enrich_menu(data)
    return transformed_data
