import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, request
from flask import redirect, url_for

from web_store.testing import TestWebStore
from flask_wtf.csrf import CSRFProtect
from web_store.view.store import view_store
from web_store.view.basket import view_basket
from web_store.view.login import view_login
from web_store.view.final import view_final

load_dotenv()

PATH= os.path.dirname(os.path.abspath(__file__))
PORT= os.getenv("SERVER_PORT") or 5000 

app = Flask(__name__, template_folder=os.path.join(PATH, 'templates'), static_folder=os.path.join(PATH, 'static'))
app.secret_key="kejjsbdnwilllshybxhajhdhgadgbdsxoehgbnc"

app.register_blueprint(view_login, url_prefix="/")
app.register_blueprint(view_store, url_prefix="/store")
app.register_blueprint(view_basket, url_prefix="/basket")
app.register_blueprint(view_final, url_prefix="/final")

#csrf = CSRFProtect(app) en html {{ csrf_token() }}




def main():
    print("Initiating Web Store")
    print(TestWebStore.test)
    app.run(host='0.0.0.0', port=PORT, debug=True)

if __name__ == "__main__":
    main()