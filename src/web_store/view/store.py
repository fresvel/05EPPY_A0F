from flask import Blueprint
from flask import session, render_template, request
from flask import redirect, url_for

view_store=Blueprint("view_store", __name__)

@view_store.route('/')
def store():
    if "usuario" in session:
        return render_template('store.html')
    return render_template('login.html')


@view_store.route("/add_item", methods=["POST"])
def add_item():
    print("Modificando carrito")
    if "usuario" in session:
        item = request.form.get("item")
        quantity = request.form.get("quantity", 1)
        if item:
            basket = session.get("basket", {})
            basket[item] = basket.get(item, 0) + int(quantity)
            session["basket"] = basket
            print(session["basket"])
        return redirect(url_for('view_store.store'))
    return render_template('login.html')

@view_store.route("/remove_item", methods=["POST"])
def remove_item():
    print("Modificando carrito")
    if "usuario" in session:
        item = request.form.get("item")
        if item:
            basket = session.get("basket", {})
            if item in basket:
                del basket[item]
                session["basket"] = basket
                print(session["basket"])
        return redirect(url_for('basket'))
    return render_template('login.html')