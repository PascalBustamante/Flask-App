"""Global pytest fixtures."""
import pytest
from flask_migrate import upgrade as flask_migrate_upgrade
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import event, create_engine

from src.create_app import create_app, db_manager
from src.database.models.user import User
from tests.utils import EMAIL, PASSWORD


@pytest.fixture(scope="session")
def app(request):
    """Test session-wide test `Flask` application."""
    app = create_app("testing")
    app.config.update({"TESTING": True})

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="function")
def test_client(app):
    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture(scope="session")
def _connection(app):
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    connection = engine.connect()
    yield connection
    connection.close()


@pytest.fixture(scope="session")
def _scoped_session(app):
    Session = scoped_session(sessionmaker())  ##bind it?
    return Session


@pytest.fixture(autouse=True)
def db(_connection, _scoped_session, request):
    # Bind app's db session to the test session
    transaction = _connection.begin()
    Session = _scoped_session
    session = Session(bind=_connection)
    session.begin_nested()

    @event.listens_for(session, "after_transaction_end")
    def restart_savepoint(db_session, transaction):
        """Support tests with rollbacks.

        if the database supports SAVEPOINT (SQLite needs special
        config for this to work), starting a savepoint
        will allow tests to also use rollback within tests

        Reference: https://docs.sqlalchemy.org/en/14/orm/session_transaction.html#session-begin-nested  # noqa: E501
        """
        if transaction.nested and not transaction._parent.nested:
            # ensure that state is expired the way session.commit() at
            # the top level normally does
            session.expire_all()
            session.begin_nested()

    """
    Important. This step binds the app's db session to the test session
    to allow each individual test to be wrapped in a transaction
    and rollback to a clean state after each test
    """
    db_manager.session = session

    def teardown():
        Session.remove()
        transaction.rollback()

    request.addfinalizer(teardown)

    yield db_manager


'''
@pytest.fixture(scope="session")
def db(app, request):
    """Returns session-wide initialized database"""

    def teardown():
        _db.drop_all()

    _db.app = app

    with app.app_context():
        flask_migrate_upgrade(directory="src\\migrations")
        request.addfinalizer(teardown)
    return _db





@pytest.fixture(scope="function")
def session(db, request):
    db.session.begin_nested()

    def commit():
        db.session.flush()

    # patch commit method
    old_commit = db.session.commit
    db.session.commit = commit

    def teardown():
        db.session.rollback()
        db.session.close()
        db.session.commit = old_commit

    request.addfinalizer(teardown)
    return db.session

'''
'''
@pytest.fixture(scope="session")
def session(app, db, request):
    """Creates a new database session for each test, rolling back changes afterwards"""
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
'''


@pytest.fixture
def user(db):
    user = User(email=EMAIL, password=PASSWORD)
    db.session.add(user)
    db.session.commit()
    return user
