from __future__ import absolute_import
from flask import url_for


import os
import sys


from src.create_app import create_app, db_manager
from src.database.models import user


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db_manager, "User": user}


if __name__ == "__main__":
    app.run(debug=True)
