"""Module for file operations."""

import csv


def write_to_csv_file(csv_file_path, data):
    with open(csv_file_path, "w", encoding="UTF8") as csv_file:
        writer = csv.writer(csv_file)
        for dto in data:
            writer.writerow(
                [
                    dto.cocktail_id,
                    dto.cocktail_name,
                    dto.glass_type,
                    dto.is_alcoholic,
                    dto.preparation_notes_en,
                    dto.ingredients,
                ]
            )
