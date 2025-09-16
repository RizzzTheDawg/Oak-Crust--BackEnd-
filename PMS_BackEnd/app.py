from flask import Flask
from application.product_api import product_bp
from application.category_api import category_bp
from application.order_api import order_bp

app = Flask(__name__)
app.register_blueprint(product_bp)
app.register_blueprint(category_bp)

app.register_blueprint(order_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5080)
