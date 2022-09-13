import sqlite_rsm
import flask

@sqlite_rsm.app.route('/')
def serve_db():
    """main route for interacting with the db."""
    pass