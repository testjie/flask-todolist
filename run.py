from app.models.ext import db
from app import create_app



app = create_app("DevelopConfig")
db.init_app(app)



if __name__ == "__main__":
    app.run(host="0.0.0.0")

