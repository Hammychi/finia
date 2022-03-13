from flask import Flask
import base64

base = base64.b64encode('Horizen'.encode('ascii')) 
print(base)
def create():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = base

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')
    
    return app

def wumpus():
    print('fuckyous')
    
