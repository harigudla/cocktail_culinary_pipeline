"""Utililties module."""


def convert_dto_to_dict(dto_objects):
    """Converts dto objects to dictionary objects.

    Args:
        dto_objects (list): CocktailDTO objects.
    
    Returns:
        (list): List of Dictionary objects.

    """

    dict_list = []
    if not dto_objects:
        return dict_list
    for dto in dto_objects:
        dict_list.append(dto.__dict__)
    return dict_list