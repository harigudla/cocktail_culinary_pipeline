"""Cocktail Data Transfer class."""


class CocktailDTO:
    """
    A data transfer object representing a Cocktail.

    """

    def __init__(
        self,
        cocktail_id: int,
        cocktail_name: str,
        glass_type: str,
        is_alcoholic: str,
        preparation_notes_en: str,
        ingredients: str,
    ):
        """Initialize CocktailDTO class.

        Args:
            cocktail_id (int): Unique cocktail identification number.
            cocktail_name (str): Cocktail name.
            glass_type (str): Glass type used for cocktail.
            is_alcoholic (str): Yes/No, is cocktail alcholic?.
            preparation_notes_en (str): Preparation notes in english.
            ingredients (str): Ingredients used.

        """
        self.cocktail_id = cocktail_id
        self.cocktail_name = cocktail_name
        self.glass_type = glass_type
        self.is_alcoholic = is_alcoholic
        self.preparation_notes_en = preparation_notes_en
        self.ingredients = ingredients

    def __lt__(self, other):
        """Less than operator overloaded for sorting instances.

        Args:
            other (CocktailDTO): Instance to be compared.

        Returns:
            boolean : Return true if condition is valid else false.

        """
        return self.cocktail_name < other.cocktail_name
