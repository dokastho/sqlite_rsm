import sqlite_rsm.node as node
import flask

@node.app.teardown_appcontext
def close_db(error):
    """Close the database at the end of a request.

    Flask docs:
    https://flask.palletsprojects.com/en/1.0.x/appcontext/#storing-data
    """
    assert error or not error  # Needed to avoid superfluous style error
    sqlite_db = flask.g.pop('sqlite_db', None)
    if sqlite_db is not None:
        sqlite_db.commit()
        sqlite_db.close()

# @node.app.route('/', methods=['POST'])
@node.app.route('/')
def serve_db():
    """main route for interacting with the db."""
    return flask.jsonify({
        "foo": "bar"
    }), 200


