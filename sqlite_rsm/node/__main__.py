'''File for launching the rsm fragment.'''

import pathlib
import sqlite3
import flask
import sqlite_rsm.node as node


# fetch schema from url using token
# download it
# start the sqlite db
# connect to a master if one exists


class Node:

    def __init__(self) -> None:
        print("\tstarting node")
        print("\tnode start complete")
        # check if db file exists
        db = node.app.config['DATABASE_FILENAME']

        db_file = pathlib.Path(db)
        if not db_file.is_file():
            db_file.touch()
        
        # start the db (this step might be wrong)
        self.get_db()

        node.app.run(port=0)
        
    def dict_factory(self, cursor, row):
        """Convert database row objects to a dictionary keyed on column name.

        This is useful for building dictionaries which are then used to render a
        template.  Note that this would be inefficient for large queries.
        """
        return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}



    def get_db(self):
        """Open a new database connection.

        Flask docs:
        https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
        """
        with node.app.app_context(self):
            if 'sqlite_db' not in flask.g:
                db_filename = node.app.config['DATABASE_FILENAME']
                flask.g.sqlite_db = sqlite3.connect(str(db_filename))
                flask.g.sqlite_db.row_factory = self.dict_factory
                # Foreign keys have to be enabled per-connection.  This is an sqlite3
                # backwards compatibility thing.
                flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")
            return flask.g.sqlite_db


    @node.app.teardown_appcontext
    def close_db(self, error):
        """Close the database at the end of a request.

        Flask docs:
        https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
        """
        assert error or not error  # Needed to avoid superfluous style error
        sqlite_db = flask.g.pop('sqlite_db', None)
        if sqlite_db is not None:
            sqlite_db.commit()
            sqlite_db.close()
            
    # @sqlite_rsm.app.route('/', methods=['POST'])
    @node.app.route('/', methods=['POST'])
    def serve_db(self):
        """main route for interacting with the db."""
        pass




def main():

    Node()


if __name__ == "__main__":
    main()
