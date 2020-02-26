# from models.item import Item
#
# item = Item("https://www.amazon.com/gp/product/B07CMS5Q6P?pf_rd_p=ab873d20-a0ca-439b-ac45-cd78f07a84d8&pf_rd_r=DPX114HGMBYXCDS1TAR4",
#             "span",
#             {"id": "priceblock_ourprice"})
# item.save_to_mongo()
#
# items_loaded = Item.all()
# print(items_loaded)
# print(items_loaded[0].load_price())



# from models.alert import Alert
#
# alert = Alert("4427cc2083134283919cf10f14dc6963", 50)
# alert.save_to_mongo()
import json
import os

from flask import Flask, render_template
from views.alerts import alert_blueprint
from views.stores import store_blueprint
from views.users import user_blueprint


app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)

@app.route('/')
def home():
    return render_template('home.html')

app.register_blueprint(alert_blueprint, url_prefix='/alerts')
app.register_blueprint(store_blueprint, url_prefix='/stores')
app.register_blueprint(user_blueprint, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)