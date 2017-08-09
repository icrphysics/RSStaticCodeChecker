from flask import Flask

app = Flask(__name__)           # The WSGI compliant web application object

# Setup Flask-Script

# Initialize Flask Application
def init_app(app, extra_config_settings={}):
    """
    Initializes the application
    """
    # Read common settings from 'app/settings.py'
    app.config.from_object('app.settings')

    # Read environment-specific settings from 'app/local_settings.py'
    try:
        app.config.from_object('app.local_settings')
    except ImportError:
        print("The configuration file 'app/local_settings.py' does not exist.\n"+
              "Please copy app/local_settings_example.py to app/local_settings.py\n"+
              "and customize its settings before you continue.")
        exit()

    # Add/overwrite extra settings from parameter 'extra_config_settings'
    app.config.update(extra_config_settings)
    if app.testing:
        app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF checks while testing
    
    import sys
    print app.config["STATICCODESCANNERPATH"]
    sys.path.append(app.config["STATICCODESCANNERPATH"])

    with app.app_context():
        from views import main