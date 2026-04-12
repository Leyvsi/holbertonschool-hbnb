from app import create_app, db
from config import DevelopmentConfig
from app.models.user import User

app = create_app(DevelopmentConfig)

def seed_admin():
    admin_email = "admin@hbnb.io"
    existing_admin = User.query.filter_by(email=admin_email).first()

    if not existing_admin:
        print("Creating admin user...")

        admin = User(
            first_name="Admin",
            last_name="HBnB",
            email=admin_email,
            password="admin1234",
            is_admin=True
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created:", admin.email)
    else:
        print("Admin already exists")

with app.app_context():
    db.create_all()
    seed_admin()

if __name__ == '__main__':
    app.run(debug=True)