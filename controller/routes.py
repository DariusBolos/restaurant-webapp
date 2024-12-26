from flask import render_template, url_for, request, flash, redirect, session
from controller.config import app, db, checkEmptyFields
from data.models.tables import CookedDish, Drink, Customer, Order


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('/index.html')


@app.route('/menu/', methods=['POST', 'GET'])
def menu():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        info = request.form['item-info'] if 'item-info' in request.form else None
        option = request.form['option'] if 'option' in request.form else None
        if not checkEmptyFields(name, price, info, option):
            flash("Please fill all the fields before submitting", "error")
            return redirect(url_for("menu"))
        else:
            typeOfItem = {
                "dish": CookedDish(name, price, info),
                "drink": Drink(name, price, info)
            }

            item = typeOfItem[option]
            db.session.add(item)
            db.session.commit()
            return redirect(url_for("menu"))

    return render_template('/menu.html')


@app.route('/menu/catalogue/', methods=['POST', 'GET'])
def catalogue():
    if request.method == 'POST':
        id = request.form['id']
        type = request.form['remove']
        session['type'] = type
        return redirect(url_for("delete", id=id, type=type))
    return render_template('/catalogue.html', dishes=CookedDish.query.all(), drinks=Drink.query.all())


@app.route('/menu/<int:id>', methods=['POST', 'GET'])
def delete(id):
    type = session["type"]

    objects = {
        "Remove Dish": CookedDish,
        "Remove Drink": Drink,
        "Remove Customer": Customer,
    }

    itemToDelete = objects[type].query.get_or_404(id)
    try:
        db.session.delete(itemToDelete)
        db.session.commit()
        return redirect(url_for("home"))
    except:
        return "The item could not be deleted from the database"


@app.route('/customers/', methods=['POST', 'GET'])
def customers():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']

        if not checkEmptyFields(name, address):
            flash("Please fill all the fields before submitting", "error")
            return redirect(url_for("customers"))
        else:
            customer = Customer(name, address)
            db.session.add(customer)
            db.session.commit()
            return redirect(url_for("customers"))

    return render_template('/customers.html')


@app.route('/customers/users', methods=['POST', 'GET'])
def displayUsers():
    if request.method == 'POST':
        id = request.form['id']
        type = request.form['remove']
        session['type'] = type
        return redirect(url_for("delete", id=id, type=type))
    return render_template('/users.html', customers=Customer.query.all())


@app.route('/order', methods=['POST', 'GET'])
def order():
    if request.method == 'POST':
        dishCount = CookedDish.query.count()
        drinkCount = Drink.query.count()
        dishIds = []
        drinkIds = []
        id = request.form['id'] if 'id' in request.form else None
        value = request.form['select']

        if value == "Select Dish":
            if id:
                session[f"{value}{id}"] = id
            else:
                for ind in range(1, dishCount + 1):
                    if session[f"{value}{ind}"]:
                        dishIds.append(ind)

        elif value == "Select Drink":
            if id:
                session[f"{value}{id}"] = id
            else:
                for ind in range(1, drinkCount + 1):
                    if session[f"{value}{ind}"]:
                        drinkIds.append(ind)
        else:
            customerID = request.form["user"]
            total = 0
            for id in dishIds:
                item = CookedDish.query.filter_by(id=id).first()
                total += item.price

            for id in drinkIds:
                item = Drink.query.filter_by(id=id).first()
                total += item.price

            orderInstance = Order(int(customerID), str(dishIds), str(drinkIds), total)
            db.session.add(orderInstance)
            db.session.commit()
            db.session.close()
            return redirect(url_for("home"))

    return render_template('/order.html', customers=Customer.query.all(),
                           dishes=CookedDish.query.all(), drinks=Drink.query.all())
