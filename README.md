# The Story
I am the host of a small cocktail party for my friends. While I was wondering what would be the best menu to make, got a reference from internet.

The reference can be found in ´input/cocktail_menu.json´

But unfortunately, its not complete. It misses the instruction on how to prepare the cocktail, and what kind of cocktail glass you need (suitable glass). 
Luckily, I found a website/api https://www.thecocktaildb.com/api.php that contains this information, so that I can extend menu list with the required information.

## Solution
The solution extracts the cocktail menu, enrichs the menu with API reference like adding preparation notes and suitable glass. At the end, you find a information database that can be further used by Data Analytics team, check ´database´ folder. Finally, you will find all the information in ´output´ folder.

Happy Partying!

## Dependencies
- [click - package for creating beautiful command line interfaces in a composable way with as little code as necessary.](https://palletsprojects.com/p/click//)


## Installation & Usage instructions
1. Checkout from git
2. Install package with `pip install .`
3. Invoke command with options: `python etl/start.py --input_dir <> --input_file <> --output_dir <> --output_file <>`
4. Invoke command with default options: `python etl/start.py`
5. To get help: `python etl/start.py --help`


## Development
1. The pyproject.toml file contains minimal configuration settings for flake8, isort and black in Python projects.
2. The .pydocstyle file contains configuration setting for checking compliance with Python docstring conventions.