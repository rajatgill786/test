from app import app, db  # Import the app and db instances

with app.app_context():
    db.create_all()  # Create all tables defined in the models
