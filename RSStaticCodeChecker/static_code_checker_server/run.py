from app.init_app import app, init_app

# Start a development web server, processing extra command line parameters. E.g.:
if __name__ == "__main__":
    init_app(app)

print "Trying to start on port {}".format(app.config["PORT"])
app.run(port = app.config["PORT"])
