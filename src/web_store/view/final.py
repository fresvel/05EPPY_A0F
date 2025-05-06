from flask import Blueprint
from flask import session, render_template, request
from flask import url_for, redirect

view_final=Blueprint("view_final", __name__)


@view_final.route('/building')
def building():
    if "usuario" in session:
        return render_template('building.html')
    return render_template('login.html')


@view_final.route('/bought', methods=["POST"])
def bought():
    if "usuario" in session:
        address = request.form.get("address")
        total = request.form.get("total")
        currency = "USD"
        session["basket"]={}

        return render_template(
            "bought.html",
            shipping_address=address,
            total_price=total,
            currency=currency
        )
    return render_template('login.html')
