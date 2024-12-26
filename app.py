from controller.config import app, db
from controller.routes import home, menu, customers

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000)
