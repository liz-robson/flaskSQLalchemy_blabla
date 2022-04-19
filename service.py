from application.models.items import Items
from application.models.users import Users
from application import db


def get_all_items():
    # alternatively, the db object from application may be used
    # items = db.session.query(Items)
    # return items
    return Items.query.all()


def get_item_by_id(item_id):
    if item_id > 0:
        return Items.query.get(item_id)
    else:
        return None


def get_user_by_id(user_id):
    if user_id < 100:
        return Users.query.get(user_id)
    else:
        return None
