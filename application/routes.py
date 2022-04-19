from flask import render_template, jsonify

from application import app
import service


@app.route('/items', methods=['GET'])
def show_items():
    error = ""
    items = service.get_all_items()
    if len(items) == 0:
        error = "There are no items to display"
    return render_template('item.html', items=items, message=error)


@app.route('/item/<int:item_id>', methods=['GET'])
def show_item(item_id):
    error = ""
    item = service.get_item_by_id(item_id)
    print(item.item_name, item.size, item.colour, item.rental_price)
    if not item:
        return jsonify("There is no items with id: " + str(item_id))
    return jsonify(item)


@app.route('/usersanditems/<int:user_id>', methods=['GET'])
def users_and_items(user_id):
    error = ""
    user = service.get_user_by_id(user_id)
    if not user:
        error = "There is no users with id: " + str(user_id)
    return render_template('users_and_items.html', user=user, message=error, title="Users and Items")


