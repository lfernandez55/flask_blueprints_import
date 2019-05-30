from flask import Flask, request, render_template
import os



# Class-based application configuration
class ConfigClass(object):
    AUTHORS_NAME = "Luke"



def create_app(extra_config_settings={}):
    """ Flask application factory """

    # Create Flask app load app.config
    app = Flask(__name__)

    # app.config.from_object(__name__+'.ConfigClass')
    app.config.from_object('app.settings')
    print(app.config['AUTHORS_NAME'])




    # @app.route('/')
    # def home_page():
    #     return render_template('index.html')
    from api.api import api
    app.register_blueprint(api)





    return app


# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=7000, debug=True)
