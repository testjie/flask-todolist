from app.models.ext import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app
from app.models.tbl_content_type import ContentType
from app.models.tbl_content import Content
from app.models.tbl_user import User



manager = Manager(app)
mirgrate = Migrate(app,db)
# 添加迁移命令到manager中
manager.add_command("db", MigrateCommand)



if __name__ == "__main__":
    manager.run()
