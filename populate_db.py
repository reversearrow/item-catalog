from flask_script import Manager
from app.models import db, Categories, Items
from run import app
import uuid

manager = Manager(app)


@manager.command
def init_db_load():
    category1 = Categories(name="Soccer")
    category2 = Categories(name="Basketball")
    category3 = Categories(name="Baseball")
    category4 = Categories(name="Frisbee")
    category5 = Categories(name="Snowboarding")
    category6 = Categories(name="Rock Climbing")
    category7 = Categories(name="Foosball")
    category8 = Categories(name="Skating")
    category9 = Categories(name="Hockey")
    db.session.add(category1)
    db.session.commit()
    db.session.add(category2)
    db.session.commit()
    db.session.add(category3)
    db.session.commit()
    db.session.add(category4)
    db.session.commit()
    db.session.add(category5)
    db.session.commit()
    db.session.add(category6)
    db.session.commit()
    db.session.add(category7)
    db.session.commit()
    db.session.add(category8)
    db.session.commit()
    db.session.add(category9)
    db.session.commit()


@manager.command
def delete_all_categories():
    db.session.query(Categories).delete()
    db.session.commit()

# Test Scripts
# @manager.command
# def update_category():
#     category = Categories.query.filter_by(name='Soccer').first()
#     category.name = "Soccer123"
#     db.session.add(category)
#     db.session.commit()
#
#
# @manager.command
# def get_items():
#     item = Items.query.filter_by(name='Football').first()
#     print dir(item)
#
#
# @manager.command
# def get_categories():
#     result = Categories.query.all()
#     for r in result:
#         items = r.items
#         for i in items:
#             print i.name


if __name__ == "__main__":
    manager.run()
