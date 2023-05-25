from flask import Flask
from flask import render_template
def create_app():
    app = Flask(__name__)
    @app.route("/")
    def home():
        return render_template('home.html')
    
    @app.route("/l3vpn")
    def l3vpn():
        return render_template('l3vpn.html')
    
    @app.route("/l2vpn")
    def l2vpn():
        return render_template('l2vpn.html')
    
    return app