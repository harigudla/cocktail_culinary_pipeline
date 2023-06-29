"""Load data into table."""

from etl_exceptions import EtlExecutionException
from db import SQLite3Connection
from util import convert_dto_to_dict


def process(data, sqlite_conn):
    """Load data into tables.

    Args:
        data (list): List of DTO objects.

    Raises:
        EtlExecutionException (`obj`): Raise exception if method fails.

    """

    try:
        dict_list = convert_dto_to_dict(data)
        sqlite_conn.load_data(dict_list)
    except Exception as error:
        raise EtlExecutionException("Cannot perform load operation.")
