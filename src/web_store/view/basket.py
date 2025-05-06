from flask import Blueprint
from flask import session, render_template, request
from flask import redirect, url_for

view_basket =Blueprint("view_basket", __name__)

@view_basket.route("/")
def basket():
    if "usuario" not in session:
        return redirect(url_for("login"))

    # Simulación de productos disponibles con precios
    catalog = {
        "altavoz": {"product_name": "Altavoz", "price": 50},
        "headset": {"product_name": "Headset", "price": 80},
        "laptop": {"product_name": "Laptop", "price": 1200},
        "mouse": {"product_name": "Mouse", "price": 25},
        "televisor": {"product_name": "Televisor", "price": 900}
    }

    basket_raw = session.get("basket", {})
    basket_items = []
    basket_total = 0

    for key, quantity in basket_raw.items():
        if key in catalog:
            item_data = catalog[key]
            price = item_data["price"]
            total_price = price * quantity
            basket_items.append({
                "id": key,  # usamos el nombre del producto como id para eliminar
                "product_name": item_data["product_name"],
                "quantity": quantity,
                "price": price,
                "total_price": total_price
            })
            basket_total += total_price

    return render_template("basket.html", basket_items=basket_items, basket_total=basket_total)
