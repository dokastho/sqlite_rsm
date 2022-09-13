'''File for launching the rsm fragment.'''

import pathlib
import sqlite_rsm


# fetch schema from url using token
# download it
# start the sqlite db
# connect to a master if one exists

def main():

    # check if db file exists
    db = sqlite_rsm.app.config['DATABASE_FILENAME']

    db_file = pathlib.Path(db)
    if not db_file.is_file():
        db_file.touch()


    sqlite_rsm.app.run(port=0)


if __name__ == "__main__":
    main()
