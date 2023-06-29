"""CocktailDB API class."""

import requests
from etl_exceptions import EtlExecutionException

# # Initialze logging.
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = logging.StreamHandler(sys.stderr)
# formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
# handler.setFormatter(formatter)
# logger.addHandler(handler)

API_BASE_URL = "https://www.thecocktaildb.com/api/json/v1/1/"


class CocktailDBAPI:
    """To initialize and make connection to CocktailDB API.

    Initialization of CocktailDB API class instance with parameters
    for quering the data.

    """

    def __init__(self, base_url=API_BASE_URL):
        """Initialize CocktailDB API.

        Args:
            base_url (str): API Base URL.

        """
        self.base_url = base_url

    def get_cocktail_by_name(self, endpoint, params=None):
        """Search cocktail by name.

        Args:
            endpoint (str): API endpoint.
            params (dict): API parameters in search query.

        Raises:
            EtlExecutionException: Raises error if status code failure.

        Returns:
            data (list): Json object array.

        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, headers=None, params=params)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                raise EtlExecutionException(
                    f"Failed to extract from url {self.base_url}, status code {response.status_code}"
                )
        except Exception as error:
            raise EtlExecutionException(error)
