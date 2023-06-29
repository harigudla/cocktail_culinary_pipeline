"""SQLite3 Connection class."""

import sqlite3


class SQLite3Connection:
    """To initialize and make connection to SQLite3 Database file."""

    def __init__(self, db_name=":memory:"):
        """Initialize SQLite3Connection.

        Args:
            db_name: Database file name. Defaults to memory database.

        Raises:
            error (`obj`): Raise exception if method fails.

        """
        try:
            self._connection = sqlite3.connect(db_name)
            self.create_tables()
        except Exception as error:
            raise error

    def create_tables(self):
        """Create tables for cocktails menu"""

        _cursor = self._connection.cursor()
        _cursor.executescript(
            """
                drop table if exists cocktails_menu;
                create table cocktails_menu (
                        cocktail_id INTEGER primary key
                        ,cocktail_name text not null
                        ,glass_type text
                        ,is_alcoholic text
                        ,preparation_notes_en text
                        ,ingredients text
                )
            """
        )

        self._connection.commit()
        _cursor.close()

    def load_data(self, data):
        """Load data into table.

        Args:
            data (list): List of Dictionary objects.

        """
        _cursor = self._connection.cursor()
        _cursor.executemany(
            """
            insert into cocktails_menu (
                cocktail_id
                ,cocktail_name
                ,glass_type
                ,is_alcoholic
                ,preparation_notes_en
                ,ingredients) 
                values  (:cocktail_id, :cocktail_name, :glass_type, :is_alcoholic, :preparation_notes_en, :ingredients)""",
            data,
        )
        self._connection.commit()
        _cursor.close()

    def get_data(self):
        """Retrive data from table."""
        results = []
        _cursor = self._connection.cursor()
        _cursor.execute(
            """select 
                    cocktail_id
                    ,cocktail_name
                    ,glass_type
                    ,is_alcoholic
                    ,preparation_notes_en
                    ,ingredients
                from
                    cocktails_menu"""
        )
        rows = _cursor.fetchall()
        results.extend(rows)
        _cursor.close()
        return results

    def close(self):
        """Close connection."""

        self._connection.close()
        self._connection = None
