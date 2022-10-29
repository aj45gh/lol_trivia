from flask import Flask

from champions.database import init_db, db_session


def create_app():
    app = Flask(__name__)
    init_db()

    @app.teardown_appcontext
    def shutdown_session():
        db_session.remove()

    from champions.models.user import User

    # u = User(username='notaj', password='notmypass')
    # db_session.add(u)
    # db_session.commit()
    print(User.query.all())

    return app
