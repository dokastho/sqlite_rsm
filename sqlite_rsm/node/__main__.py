'''File for launching the rsm fragment.'''

import pathlib
# import sqlite_rsm
import sqlite_rsm.node as node


# fetch schema from url using token
# download it
# start the sqlite db
# connect to a master if one exists


class Node:
    
    def __init__(self) -> None:
        pass

def main():

    # check if db file exists
    db = node.app.config['DATABASE_FILENAME']

    db_file = pathlib.Path(db)
    if not db_file.is_file():
        db_file.touch()


    node.app.run(port=0)


if __name__ == "__main__":
    main()
