"""ETL Process - Main module."""

import click

import extract
import transform
import load
import os

from file_utils import write_to_csv_file
from etl_exceptions import EtlExecutionException
from db import SQLite3Connection


@click.command()
@click.option(
    "--input_dir",
    envvar="INPUT_DIR",
    default="input",
    help="Input folder path, Default input.",
)
@click.option(
    "--ip_filename",
    envvar="IP_FILENAME",
    default="cocktail_menu.json",
    help="File name to read menu data, Default ´cocktail_menu.json´.",
)
@click.option(
    "--output_dir",
    envvar="OUTPUT_DIR",
    default="output",
    help="Output folder path, Default ´output´.",
)
@click.option(
    "--op_filename",
    envvar="OP_FILENAME",
    default="final_menu.csv",
    help="File name to write data, Default ´final_menu.csv´.",
)
def main(input_dir, ip_filename, output_dir, op_filename):
    """Extract, transform and load data.

    Check README.md file for more information about this pipeline.

    Args:
        input_dir (str): Input directory for file to read.
        ip_filename (str): Input filename to read data.
        output_dir (str): Output directory to write files.
        op_filename (str): Output filename to write data.

    Raises:
        EtlExecutionException (`obj`): Raise exception if any method fails.

    """

    sqlite_conn = None
    try:
        # extract
        ip_file_path = os.path.join(input_dir, ip_filename)
        source_data = extract.process(ip_file_path)

        # transform
        trasformed_data = transform.process(source_data)

        # load --> Write to db.
        sqlite_conn = SQLite3Connection("database/warehouse.db")
        load.process(trasformed_data, sqlite_conn)

        # load --> Write to file.
        op_file_path = os.path.join(output_dir, op_filename)
        write_to_csv_file(op_file_path, trasformed_data)

    except EtlExecutionException as error:
        raise error
    finally:
        if sqlite_conn is not None:
            sqlite_conn.close()
        sqlite_conn = None


if __name__ == "__main__":
    main()
