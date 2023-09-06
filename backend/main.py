from __future__ import absolute_import
from src.create_app import create_app, db
from src.models.user import User
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = create_app(os.getenv("FLASK_ENV", "development"))


@app.shell_context_processor
def shell():
    return {"db": db, "User": User}


if __name__ == "__main__":
    app.run(debug=True)
