'''File for launching the rsm fragment.'''

import pathlib
import sqlite3
import flask
import sqlite_rsm.node as node

# steps to initialize:
# fetch schema from url using token
# download it
# start the sqlite db
# connect to a master if one exists



class Node:

    def __init__(self) -> None:

        # file that holds schema
        self.schema = node.app.config['SITE_ROOT'] / 'sql' / 'schema.sql'
        print("\tstarting node")
        print("\tnode start complete")
        # check if db file exists
        self.db = node.app.config['DATABASE_FILENAME']

        self.init_db()


        # init complete. start serving node
        node.app.run(port=8000)

    def get_schema(self):
        """Post http request to fetch schema from site."""

    def init_db(self):
        """Create db file if not exists."""

        db_file = pathlib.Path(self.db)
        if not db_file.is_file():
            db_file.touch()

        # start the db (this step might be wrong)
        self.get_db()

    def get_db(self):
        """Open a new database connection.

        Flask docs:
        https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
        """
        with node.app.app_context():
            if 'sqlite_db' not in flask.g:
                db_filename = node.app.config['DATABASE_FILENAME']
                flask.g.sqlite_db = sqlite3.connect(str(db_filename))
                flask.g.sqlite_db.row_factory = dict_factory
                # Foreign keys have to be enabled per-connection.  This is an sqlite3
                # backwards compatibility thing.
                flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")
            return flask.g.sqlite_db


def dict_factory(self, cursor, row):
    """Convert database row objects to a dictionary keyed on column name.

    This is useful for building dictionaries which are then used to render a
    template.  Note that this would be inefficient for large queries.
    """
    return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}



def main():

    Node()


if __name__ == "__main__":
    main()
